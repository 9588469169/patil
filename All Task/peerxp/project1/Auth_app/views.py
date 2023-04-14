from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def signUpView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/signup.html'
    context ={'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request,template_name,context)


def loginView(request):
    template_name = 'AUTH_APP/login.html'
    context = {}
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')

        user = authenticate(username=u, password=p)

        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('create_department')
            else:
                return redirect('create_ticket')
        else:
            error_message = 'Invalid login credentials'
            return render(request, template_name, {'error_message': error_message})
    return render(request,template_name,context)


def logoutView(request):
    logout(request)
    return redirect('login_url')