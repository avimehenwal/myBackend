from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from polls.models import Question


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
    question = Question.objects.get(question_id)
    return HttpResponse("You're looking at question %s. %s" % (question_id, question))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
