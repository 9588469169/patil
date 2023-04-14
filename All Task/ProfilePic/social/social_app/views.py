from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserForm, CustomUpdateForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.http import HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

class CreateCustomUser(View):
    template_name = 'social_app/user.html'
    def get(self, request):
        form = CustomUserForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserForm(request.POST, request.FILES)
        print(request.POST.get('password'))
        if form.is_valid():
            form.save()
            return redirect('display')
        context = {'form':form}    
        return render(request, self.template_name, context)

class ListCustomUser(View):
    template_name = 'social_app/display.html'
    def get(self, request):
        users = CustomUser.objects.all()
        context = {'users':users}
        return render(request, self.template_name, context)

#_________________________LOGIN__________________________________________________________________

# def user_login_view(request):
#     template_name = 'social_app/login.html'
#     context = {}
#     if request.method == 'POST':
#         un = request.POST.get('un')
#         pw = request.POST.get('pass')

#         user = authenticate(username=un, password=pw)
#         if user is not None:
#             login(request, user)
#             return redirect('display')

#     return render(request, template_name, context)    

#_________________________________OR________________________________________________________________

def user_login_view(request):   
    fm = AuthenticationForm()               #its built in login_form
    template_name = 'social_app/login.html'
    context = {'form':fm}
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm  = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in successfully  !!')
                    return redirect('display')
            
        return render(request,template_name,context)
    else:
        return redirect('display')

#___________________________________LOGOUT__________________________________________________________________

def user_logout_view(request):
    logout(request)
    return redirect('login')


#____________________________________Change Password__________________________________________________________________
def user_change_pass(request):
    if request.user.is_authenticated:
        fm = PasswordChangeForm(user=request.user)
        template_name = 'social_app/changepass.html'
        context ={'form':fm}
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return redirect('display')
        return render(request, template_name, context)
    else:
        return redirect('login')

def update(request, pk):
    current_user = request.user
    if current_user.id == pk:
        user = CustomUser.objects.get(pk=pk)
        form = CustomUpdateForm(instance=user)
        template_name = 'social_app/update.html'
        context = {'form':form, 'user':user}
        if request.method == 'POST':
                form = CustomUpdateForm(request.POST,request.FILES, instance=user)
                context = {'form': form}
                print(request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('update', pk=user.id)
        return render(request, template_name, context)

    else:
        return HttpResponse('You do not have permission to edit this profile')


def delete(request, pk):
    if request.user.id == pk:
        user = CustomUser.objects.get(pk=pk)
        template_name = 'social_app/confirm.html'
        context = {}
        if request.method == 'POST':
            user.delete()
            return redirect('display')
        return render(request, template_name, context)
    
    return HttpResponse('You do nor have permission to delete this profile')

def remove_profile_pic(request,pk):
    user = CustomUser.objects.get(pk=pk)
    old_image = user.profile_pic
    old_image.delete()
    user.profile_pic = 'default.jpg'
    user.save()
    return redirect('update', pk=user.id)
    