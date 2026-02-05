from django.shortcuts import redirect, render

from registration.forms import RegistrationForm


def registration_form(request):
    # """Handle registration form display and submission"""
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)

    #     if form.is_valid():
    #         print("Form is valid")
    #         return redirect('registration:form')
    # else:
    form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})