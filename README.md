# Career Prediction Web App

This is a Django-based web application for predicting suitable careers using Bayesian networks.

## Project Structure

- `career_prediction/` - Django project settings and configuration.
- `predictor/` - Main app containing prediction logic, models, views, and templates.
  - `bayesian_network.py` - Implements Bayesian network logic for career prediction.
  - `data/careers.csv` - Dataset used for predictions.
  - `static/` - Static files (CSS, JS).
  - `templates/` - HTML templates.
- `db.sqlite3` - SQLite database.
- `requirements.txt` - Python dependencies.

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

3. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

4. **Access the app:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Dependencies

- Django
- pgmpy
- pandas

## Usage

- Fill out the form on the homepage to get a career prediction based on your input.

## License

This project is for educational purposes.