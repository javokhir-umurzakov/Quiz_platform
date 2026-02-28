from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from quizzes.models import QuizSession

def dashboard(request):
    now = timezone.now()

    week = now - timedelta(days=7)
    month = now - timedelta(days=30)
    year = now - timedelta(days=365)

    weekly = QuizSession.objects.filter(user=request.user, created_at__gte=week)
    monthly = QuizSession.objects.filter(user=request.user, created_at__gte=month)
    yearly = QuizSession.objects.filter(user=request.user, created_at__gte=year)

    return render(request, 'dashboard.html', {
        "weekly": weekly.count(),
        "monthly": monthly.count(),
        "yearly": yearly.count(),
    })