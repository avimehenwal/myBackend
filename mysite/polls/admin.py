from django.contrib import admin
from django.db.models.enums import Choices

from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)
