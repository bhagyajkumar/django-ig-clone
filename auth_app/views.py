from django.shortcuts import render
from .forms import RegistrationForm


def signup(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "signup.html", {'form': form})
