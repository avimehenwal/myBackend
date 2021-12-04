from django.http import HttpResponse, JsonResponse
from polls.models import Choice, Question
from django.core import serializers
from django.core.mail import send_mail

from django.core.mail import EmailMessage


def SendEmail():
    status = False
    try:
        email = EmailMessage("test", "test", to=["avimehenwal@gmail.com"])
        email.send()
        status = True
    except Exception as e:
        print(e)
    return status


def index(request):
    all_questions_serialized = list(Question.objects.values())
    return JsonResponse(
        {
            "count": len(all_questions_serialized),
            "questions": all_questions_serialized,
            "status": "Success",
        }
    )


def detail(request, question_id):
    query = Question.objects.filter(id=question_id).values().first()
    if query:
        result = query
        status = "Success"
    else:
        result = "No result found with question ID = %s" % question_id
        status = "Failed"
    return JsonResponse(
        {
            "question": result,
            "status": status,
        }
    )


def choices(request, question_id):
    query = list(Choice.objects.filter(question_id=question_id).values())
    print(query)
    result = {}
    if query:
        result["status"] = "Success"
        result["choices"] = query
        return JsonResponse(result)
    else:
        result["status"] = "Failed"
        result["message"] = (
            "Sorry no choicces found for question with id %s" % question_id
        )
        return JsonResponse(result, status=204)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
