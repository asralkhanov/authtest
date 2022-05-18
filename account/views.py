from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import redirect
# Create your views here.
def home(request):
	return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            account = user_form.save(commit=False)
            account.set_password(user_form.cleaned_data['password'])
            account.save()
            return redirect('/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
