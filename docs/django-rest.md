# Django Rest Framework

- Framework built on top of django
- [x] web browsable API
- [x] Serialization - machine to language representations
- [ ] Internationalization
  - not content itself but error messages
- [x] schema, what resources API offers and what operations can be performed on them
- [x] GraphQL Schema Definition Language (SDL),

## How it works

- Request is captured by WSGI/ASGI implementation and then passed down to python world
- python matches the URL to a python object responsible for processing request
- View Class will have, ViewSets abstration level
  - queryset
  - serializer_class
  - permission_classes
- Authorization
  - Login and authentication
  - Object level permissions

### CMS vs django admin panel

- Focus, focus is towards published, draft and preview content
- Usability, easy drag and drop

## Questions

> Before RESTful APIs, we had RPC, SOAP, CORBA, and other less open protocols.

- Does DRF have GraphQL? it does have openAPI schema
- HOw to connect django models to graphene objects types?
- REST vs GraphQL?
  - Unlike a RESTful API, there is only a single URL from which GraphQL is accessed. Requests to this URL are handled by Graphene’s GraphQLView view.
  - A REST API is an architectural concept for network-based software. GraphQL, on the other hand, is a query language, a specification, and a set of tools that operates over a single endpoint using HTTP
  - , if you wanted to request information from two objects, you’d need to perform two REST API requests. The advantage of REST APIs is its simplicity—you have one endpoint that does one task, so it’s easy to understand and manipulate. In other words, if you have X endpoint, it provides X data.
  -

## Available Tooling

- django
- django-rest-framework
- graphene
- django-cms
- django-graphene
  - single graphQL endpoint in `urls.py`, define schema

## CMS Lingo

- pages and sub-pages, URL directory path

## GraphQL

- [Relay](https://relay.dev/docs/) is a JavaScript framework for fetching and managing GraphQL data in React applications that emphasizes maintainability, type safety and runtime performance.

```graphql
# query {
#   allIngredients {
#     id
#     name
#     notes
#     category {
#       id
#     }
#   }
# }

# query {
#   categoryByName(name: "Dairy") {
#     id
#     name
#     ingredients {
#       id
#       name
#       notes
#     }
#   }
# }

query {
  categoryByName(name: "Meat") {
    __typename
    name
    ingredients {
      __typename
      name
      notes
    }
  }
}
```

## Deployment

```
./configure --enable-optimizations --prefix=$HOME/python3.7
make
make test
sudo make install # puts the packages in PREFIX PATH
```

- https://cloud.google.com/python/django
- Multiple deployment options
  - kubernetes engine
  - cloud run, serverless
  - compute engine
  - app engine
- Which DB to use? which are officially supported, SQL
  - cloud SQL and Postgres on GCP
  - [python-spanner-django](https://github.com/googleapis/python-spanner-django/) for OLTP and horizontal scaling for RDBMS

```
The outside world <-> Nginx <-> The socket <-> Gunicorn

WEB SERVER | Nginx, reverse proxy
APP SERVER | gunicorn, uWSGI, ASGI

❯ daphne cookbook.asgi:application
```

## Django database data

### Dummy data

Fixtures: data in a format that django can understand

```
python manage.py dumpdata
python manage.py loaddata
```

### Real database data

```
pip install django-dbbackup

python manage.py listbackups

# Backup the DB
python manage.py dbbackup
python manage.py dbrestore

# Backup the app source files
python manage.py mediabackup
python manage.py mediarestore
```
