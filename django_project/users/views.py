from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            print(form)
            password = form.cleaned_data.get('password2')
            passwords = form.cleaned_data.get('password1')
            print(password,passwords)
            return redirect('blog-home')

    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})