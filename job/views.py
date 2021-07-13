from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Categorie, Job
from .forms import ApplyForm, JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filter import JobFilter

def job_list(request):
    job_list = Job.objects.all()

    job_filter = JobFilter(request.GET, job_list)

    job_list = job_filter.qs

    paginator = Paginator(job_list, 2)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page('1')

    context = {
        'jobs':page_obj,
        'jobs_number':len(job_list),
        'filter':job_filter,
    }
    return render(request, 'job/jobs.html', context)

def job_detail(request, slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.job = job
            new_form.save()
            form = ApplyForm()

    else:
        form = ApplyForm()

    context = {
        'job':job,
        'form':form,
    }
    return render(request, 'job/job_details.html', context)

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            slug = new_form.slug
            form = JobForm()
            return redirect('job:job_detail', slug)

    else:
        form = JobForm()

    context = {
        'form':form,
    }
    return render(request, 'job/post_jop.html', context)