# myBackend

![Django architecture](../myBackend/docs/django-mysql-crud-rest-framework-archirecture.png)

```
python -m django --version

```

## Django

```
django-admin startproject mysite
python manage.py migrate && python manage.py runserver
python manage.py runserver --settings=settings.local
```

1. Requests and response
2. Models and admin panel
3. Views and Templates
4. Form Handling
5. Testing
6. Static files
7. Customizations

## How it works?

1. Modal/Data Layer
   1. [Django supported backends](https://github.com/django/django/tree/main/django/db/backends)
   2. [can use multiple DB simuntaneously](https://docs.djangoproject.com/en/3.2/topics/db/multi-db/#defining-your-databases)
   3. DB Relationships
2. Request/Response
   1. [JSON Response Objects](https://docs.djangoproject.com/en/3.2/ref/request-response/#jsonresponse-objects)
3. View/Template Layer
4. Admin/Security Layer, registering models to admin panel

### django-admin command

- dbshell
- makemigration
- sendtestemail
- runserver
- test

#### What’s the difference between a project and an app in Django world?

project - entire software
app - a part, module, functionality of s/w

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

### GCP Hosting

App Engine vs Cloud Run, pricing model is different. pay-as-you-go

[Ongoing costs — Cloud Run wins](https://dev.to/pcraig3/cloud-run-vs-app-engine-a-head-to-head-comparison-using-facts-and-science-1225) ✅

| -            | Cloud Run | App Engine | Heroku Hobby Plan |
| ------------ | --------- | ---------- | ----------------- |
| Monthly cost | $0.09     | $11.29     | $7.00             |

The big difference between the two services is that Cloud Run doesn’t run your container unless it’s getting requests. When a request comes in, it does 3 things:

    boots up the container
    serves the request
    shuts down the container

[Options to deploy Django?](https://cloud.google.com/python/django)

### questions

- [Push messages in Django](https://stackoverflow.com/questions/10927505/how-to-build-a-push-system-in-django)
- [django vs django-rest-framework](https://stackoverflow.com/questions/49109791/django-or-django-rest-framework)
  - Internationalization as a core feature and not a optional feature
- Create and restore django backups
  - python manage.py dbrestore.
- [Google CLoud Run](https://cloud.google.com/run) VS Google App Engine

## projects

- [API with authorization](https://github.com/juanbenitezdev/django-rest-framework-crud)
- [graphQL backend](https://graphene-python.org/)
