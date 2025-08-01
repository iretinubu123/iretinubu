import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import ast
import logging

logger = logging.getLogger(__name__)

def get_career_predictions(user_data):
    logger.info(f"Received user data: {user_data}")
    # Load and preprocess data
    data = pd.read_csv('predictor/data/careers.csv')
    
    # Preprocess the data to handle complex types
    def parse_dict(s):
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            return {}

    def parse_list(s):
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            return []

    grades_df = data['Grades'].apply(parse_dict).apply(pd.Series).rename(columns=lambda c: f"{c}_Grade")
    interests_df = data['Interests'].apply(parse_list).apply(lambda x: pd.Series(1, index=x)).fillna(0)

    # Define interest groups
    interest_groups = {
        'Tech': ['Technology', 'Problem Solving', 'Data', 'Statistics'],
        'Artistic': ['Art', 'Design', 'Creative', 'Visuals'],
        'Scientific': ['Science', 'Research'],
        'Business': ['Business', 'Management', 'Finance', 'Numbers'],
        'Social': ['Helping People', 'Writing', 'Teaching', 'Mentoring']
    }

    # Create interest group columns
    for group, interests in interest_groups.items():
        data[group] = interests_df[interests].any(axis=1)

    personality_df = data['Personality'].apply(parse_dict).apply(pd.Series).rename(columns=lambda c: f"{c}_Score")
    
    processed_data = pd.concat([grades_df, personality_df, data[['Tech', 'Artistic', 'Scientific', 'Business', 'Social', 'Career']]], axis=1)
    processed_data.columns = processed_data.columns.astype(str)
    logger.info(f"Processed data head:\n{processed_data.head()}")

    # Define the model structure
    model_structure = [
        ('Math_Grade', 'Career'), ('Science_Grade', 'Career'), ('Art_Grade', 'Career'),
        ('Analytical_Score', 'Career'), ('Creative_Score', 'Career'), ('Social_Score', 'Career'),
        ('Tech', 'Career'), ('Artistic', 'Career'), ('Scientific', 'Career'), ('Business', 'Career'), ('Social', 'Career')
    ]

    model = DiscreteBayesianNetwork(model_structure)

    # Discretize continuous data for the model
    for col in ['Analytical_Score', 'Creative_Score', 'Social_Score']:
        processed_data[col] = pd.cut(processed_data[col], bins=3, labels=['Low', 'Medium', 'High'], include_lowest=True)

    # Fit the model
    model.fit(processed_data, estimator=MaximumLikelihoodEstimator)

    # Prepare evidence from user data
    evidence = {
        'Math_Grade': user_data['math_grade'],
        'Science_Grade': user_data['science_grade'],
        'Art_Grade': user_data['art_grade'],
        'Analytical_Score': pd.cut([user_data['analytical']], bins=3, labels=['Low', 'Medium', 'High'], include_lowest=True)[0],
        'Creative_Score': pd.cut([user_data['creative']], bins=3, labels=['Low', 'Medium', 'High'], include_lowest=True)[0],
        'Social_Score': pd.cut([user_data['social']], bins=3, labels=['Low', 'Medium', 'High'], include_lowest=True)[0]
    }
    # Set evidence for interest groups
    user_interests = set(user_data['interests'])
    for group, interests in interest_groups.items():
        evidence[group] = any(i in user_interests for i in interests)

    # Perform inference
    inference = VariableElimination(model)
    logger.info(f"Evidence for inference: {evidence}")
    try:
        prediction = inference.query(variables=['Career'], evidence=evidence)
        logger.info(f"Prediction object:\n{prediction}")
        
        # Get top 3 careers
        top_careers = sorted(zip(prediction.values, prediction.state_names['Career']), reverse=True)[:3]
        logger.info(f"Top 3 careers: {top_careers}")
        
        return top_careers
    except Exception as e:
        logger.error(f"An error occurred during inference: {e}")
        return []
