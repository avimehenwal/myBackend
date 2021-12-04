from django.http import HttpResponse, JsonResponse
from polls.models import Question
from django.core import serializers


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


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
