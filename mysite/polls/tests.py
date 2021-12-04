import datetime

from django.test import TestCase
from django.utils import timezone
from django.test import Client

from .models import Question

"""
python manage.py test polls -v 2
"""


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_if_new_record_could_be_created(self):
        record = Question(question_text="sample text", pub_date=timezone.now())
        record.save()

        client = Client()
        response = client.get("/polls/question/1/")
        print(response)

        self.assertEqual(
            response.json()["status"],
            "Success"
            # Question.objects.filter(id=1).first(),
        )
