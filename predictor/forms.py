from django import forms

class PredictionForm(forms.Form):
    GRADES = [('A', 'A'), ('B', 'B'), ('C', 'C')]
    INTERESTS = [
        ('Technology', 'Technology'),
        ('Art', 'Art'),
        ('Science', 'Science'),
        ('Problem Solving', 'Problem Solving'),
        ('Design', 'Design'),
        ('Helping People', 'Helping People'),
        ('Business', 'Business'),
        ('Management', 'Management'),
        ('Research', 'Research'),
        ('Writing', 'Writing'),
        ('Creative', 'Creative'),
        ('Visuals', 'Visuals'),
        ('Data', 'Data'),
        ('Statistics', 'Statistics'),
        ('Finance', 'Finance'),
        ('Numbers', 'Numbers'),
        ('Teaching', 'Teaching'),
        ('Mentoring', 'Mentoring'),
    ]

    math_grade = forms.ChoiceField(choices=GRADES, label='Math Grade')
    science_grade = forms.ChoiceField(choices=GRADES, label='Science Grade')
    art_grade = forms.ChoiceField(choices=GRADES, label='Art Grade')

    interests = forms.MultipleChoiceField(
        choices=INTERESTS, 
        widget=forms.CheckboxSelectMultiple, 
        label='Interests'
    )

    analytical = forms.IntegerField(min_value=1, max_value=10, label='Analytical (1-10)')
    creative = forms.IntegerField(min_value=1, max_value=10, label='Creative (1-10)')
    social = forms.IntegerField(min_value=1, max_value=10, label='Social (1-10)')
