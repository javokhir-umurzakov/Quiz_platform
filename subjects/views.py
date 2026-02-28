from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Subject
# Create your views here.
@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request,'subjects.html',{'subjects':subjects})

@login_required
def topic_list(request,subject_id):
    subject = get_object_or_404(Subject,id = subject_id)
    topics = subject.topics.all()
    return render(request,'topics.html',{'topics':topics})
