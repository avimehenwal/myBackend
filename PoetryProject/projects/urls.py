from django.urls import path

from . import views


urlpatterns = [

    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("json/", views.project_json, name="project_json")

]
