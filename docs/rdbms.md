# RDBMS

- DATA Capture, generation
- Data Transformation
- Data analysis, aggregations etc
- Data Tracking

## Problems

> Trying to solve database level problem at Application Level

- How can I track all changes to a model?
- How do I "soft delete" a modal?
- How can I keep a field in-sync with another?
- How can I protect a column from being updated?
  - read-only field only
- Django signals are NOT gonna fire when you do a bulk update on modal!
  - Solve Database problems in a idiomatic way

> Its easier to add field in DB than remove them. Remove them could be a breaking change

## Triggers

Solve database related problem using **database Triggers**

- run a function when something changes in one table
- users write triggers in **plpgsql**
  - https://pypi.org/project/django-pgtrigger/
  - install DB_TRIGGERS along with modals in a django like way
- Let database protect its table from deletion rather than app level logic overriding on_delete ORM
- [django pgtrigger tutorial, how to version a modal](https://wesleykendall.github.io/django-pgtrigger-tutorial/#versioning-a-model)
  - Modal Auditing

## Postgres

```
CONTAINER_NAME=postgresql-container

docker run --rm --name ${CONTAINER_NAME} -p 5432:5432 -e POSTGRES_PASSWORD=somePassword -d postgres
docker run --rm -p 5050:5050 thajeztah/pgadmin4

docker exec -it -u postgres ${CONTAINER_NAME} psql
```

https://dev.to/shree_j/how-to-install-and-run-psql-using-docker-41j2

## DB Analytics at Massive Scale

400 TB of Analytics DB for 200 TB of DATA

- Mobile Advertisement Attribution
  - REFREE, which **ADVERTISEMENT ACTIVITY** gets accredited with which **REVENUE ACTIVITY**
- User postgres like SPRk
- High velocity, High Volume data
- Map-Reduce from backend DB Servers to Analytics Charts
- 16 Shards, Horizontal scaling
- deeply grounded both in theory and practise
- Small gains add up in big ways, Same for small errors also

## Real time Monitoring

## Advanced Database Concepts

- Store references as Array?
- Polymorphic Association
- Foreign key could be null or a value
- Foreign key as a Reference vs only as a Constraint?
- use SERIAL to generate Primary key IDs
