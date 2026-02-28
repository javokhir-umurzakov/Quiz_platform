import random
import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Question, QuizSession
from subjects.models import Topic


@login_required
def start_quiz(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = list(Question.objects.filter(topic=topic))
    random.shuffle(questions)

    if len(questions) > 10:
        questions = questions[:10]

    request.session['questions'] = [q.id for q in questions]
    request.session['index'] = 0

    session = QuizSession.objects.create(
        user=request.user,
        topic=topic,
        total_questions=len(questions)
    )

    request.session['quiz_id'] = session.id

    return redirect('quiz_question')

@login_required
def quiz_question(request):
    questions = request.session.get('questions')
    index = request.session.get('index')

    if index >= len(questions):
        return redirect('quiz_result')

    question = Question.objects.get(id=questions[index])

    return render(request, 'question.html', {'question': question})

@login_required
def check_answer(request):
    data = json.loads(request.body)
    selected = data['selected']
    question_id = data['question_id']

    question = Question.objects.get(id=question_id)
    session = QuizSession.objects.get(id=request.session['quiz_id'])

    correct = selected == question.correct_option

    if correct:
        session.score += 1
        session.save()

    request.session['index'] += 1

    return JsonResponse({
        "result": correct
    })

@login_required
def quiz_result(request):
    session = QuizSession.objects.get(id=request.session['quiz_id'])
    percent = (session.score / session.total_questions) * 100
    return render(request, 'result.html', {"session": session, "percent": percent})