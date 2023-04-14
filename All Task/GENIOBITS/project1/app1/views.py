from django.shortcuts import render, redirect
from .forms import JobListingForm, JobApplicationForm
from.models import JobApplication,JobListing

def create_job_listing(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_jobs') 
    else:
        form = JobListingForm()
    return render(request, 'app1/create_job_listing.html', {'form': form})


def all_job(request):
    form = JobListing.objects.all()
    template_name ='app1/all_jobs.html'
    context ={'form':form}
    return render(request,template_name,context)


def update_jobs(request,pk):
    jobs= JobListing.objects.get(pk=pk)
    form = JobListingForm(instance=jobs)
    template_name ='app1/create_job_listing.html'
    context ={'form':form}
    if request.method == 'POST':
        form= JobListingForm(request.POST, instance=jobs)
        if form.is_valid():
            form.save()
            return redirect('all_jobs')
    return render(request,template_name, context)
        

def delete_jobs(request,pk):
    jobs= JobListing.objects.get(pk=pk)
    template_name = 'app1/delete_confirm.html'
    context = {'jobs':jobs}
    if request.method == 'POST':
        jobs.delete()
        return redirect('all_jobs')
    return render(request,template_name,context)


def apply_for_job(request, pk):
    job = JobListing.objects.get(id=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_listing = job
            application.save()
            return redirect('applied_jobs') 
    else:
        form = JobApplicationForm()
    return render(request, 'app1/apply_for_job.html', {'form': form, 'job': job})

