from django.shortcuts import render
from .forms import PredictionForm
from .bayesian_network import get_career_predictions

def predict_career(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            predictions = get_career_predictions(user_data)
            return render(request, 'results.html', {'predictions': predictions})
    else:
        form = PredictionForm()
    return render(request, 'index.html', {'form': form})

