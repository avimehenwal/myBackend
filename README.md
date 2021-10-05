# myBackend

![Django architecture](../myBackend/docs/django-mysql-crud-rest-framework-archirecture.png)

```
python -m django --version

```

## Django

```
django-admin startproject mysite
python manage.py migrate && python manage.py runserver
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

### questions

- [Push messages in Django](https://stackoverflow.com/questions/10927505/how-to-build-a-push-system-in-django)
- [django vs django-rest-framework](https://stackoverflow.com/questions/49109791/django-or-django-rest-framework)
  - Internationalization as a core feature and not a optional feature
- Create and restore django backups
  - python manage.py dbrestore.

## projects

- [API with authorization](https://github.com/juanbenitezdev/django-rest-framework-crud)
- [graphQL backend](https://graphene-python.org/)
