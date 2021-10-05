from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Reporter
from .models import Article
from .models import Publication


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
