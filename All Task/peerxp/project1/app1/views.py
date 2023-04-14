from .forms import UserForm,NewTicketForm,DepartmentForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponse
from .models import User, Department,Ticket

from django.db import IntegrityError

#User Creation
@login_required(login_url='login_url')
#@user_passes_test(lambda User:User.is_superuser)
def users_create(request):
    form = UserForm()
    template_name='app1/user.html'
    context={'form':form}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_user')
    return render(request,template_name,context)

@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def show_data(request):
    user_data = User.objects.all()
    template_name ='app1/User_data.html'
    context ={'user_data':user_data}
    return render(request,template_name,context)

@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def create_department(request):
    form = DepartmentForm()
    template_name='app1/create_department.html'
    context={'form':form}
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments_list')
    return render(request,template_name,context)

@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def assign_department(request,pk):
    user1= User.objects.all()
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id)
        user.department = department
        user.save()
        return redirect('show_user')
    departments = Department.objects.all()
    return render(request, 'app1/assign_department.html', {'user': user, 'departments': departments})


@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'app1/departments_list.html', {'departments': departments})


@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def update_department(request, pk):
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments_list')
        return redirect('app1/departments_list')
    return render(request,'app1/create_department.html', {'form': form})


@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def delete_department(request,pk):
    try:
        department = Department.objects.get(pk=pk)
        if User.objects.filter(department=department).exists():
            #raise IntegrityError("Department is associated with users.")
            return HttpResponse("<h1> Department is associated with users</h1>")
        department.delete()
    except Department.DoesNotExist:
        raise ValueError("Department does not exist.")

    return redirect('departments_list')

'''
def update_department(request, pk):
    current_user = request.user
    if current_user.pk == pk:
        department = Department.objects.get(pk=pk)
        form = DepartmentForm(instance=department)
        context = {'form':form}
        if request.method == 'POST':
            form = DepartmentForm(request.POST, instance=department)
            if form.is_valid():
                form.save()
                return redirect('update_department', pk=department.id)
            #return redirect('app1/departments_list')
        return render(request,'app1/create_department.html', context)
    else:
        return HttpResponse('You do not have permission to edit this profile')


@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def delete_department(request, pk):
    if request.user.id == pk:
        department = Department.objects.get(pk=pk)
        if request.method == 'POST':
            department.delete()
            return redirect('display')
    return HttpResponse('You do nor have permission to delete this profile')

'''
@login_required(login_url='login_url')
def create_ticket(request,):
    users = User.objects.all()
    for i in users:
        if request.method == 'POST':
            form = NewTicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.email = i.email
                ticket.phone_number = i.phone_number
                ticket.save()
                return redirect('confirm_ticket_submission')
        else:
            form = NewTicketForm(initial={'email': i.email, 'phone_number': i.phone_number})
        return render(request, 'app1/create_ticket.html', {'form': form})
    return render(request,'app1/error_form.html')


def confirm_ticket_submission(request):
    return render(request, 'app1/confirm_ticket_submission.html')


@login_required(login_url='login_url')
@user_passes_test(lambda user:user.is_superuser)
def delete_ticket(request,pk):
    data = Ticket.objects.get(pk=pk)
    template_name='app1/delete.html'
    context= {'data':data}
    if request.method =='POST':
        data.delete()
        return redirect('show_user')
    return render(request,template_name,context)


@login_required(login_url='login_url')
def update_ticket(request,pk):
    data = Ticket.objects.get(pk=pk)
    form = NewTicketForm(instance=data)
    template_name ='app1/create_ticket.html'
    context= {'form' : form}
    if request.method == 'POST':
        form = NewTicketForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_user')
    return render(request,template_name,context)


@login_required(login_url='login_url')
def manage_tickets(request):
    if request.user:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'app1/manage_ticket.html', {'tickets': tickets})
