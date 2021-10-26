# CMS

- [x] Flexible Marketting Content
- [x] A/B Testing
- [x] Marketting Campaigns

## Features

- Asset and Image Management
- Link Content data
- support for Localization
- support content Versioning
- support DRAFT, Preperation and Publish Mode

## Dynamic Schema Generation

[for changing data-models](https://www.contentful.com/blog/2018/12/21/dynamic-schema-generation-changing-data-models/)

- shopify and gitHub switched to graphQL
  - but both have fixed schema, data structure
- SDL - Schema Definition Language

## Contentful

- Content model Type strategy based on budget, only 49 to play with
- Hierarchy of data and Logically connecting data, provides flexibility and Consistency
- Confusion with Content reusability and Flexibility, lof of content-models

## Database Schema

http://www.databaseanswers.org/data_models/

## Challenges

- How to track data changes? Who changes it? And when?
  - [RDBMS DML Event Triggers](https://www.postgresql.org/docs/current/sql-createtrigger.html)
  - https://www.cybertec-postgresql.com/en/tracking-changes-in-postgresql/

## Modelling Data

- [Many-2-many relationship](https://stackoverflow.com/questions/9789736/how-to-implement-a-many-to-many-relationship-in-postgresql)

## Questions

- What is the difference b/w homepage and landing page?
  - purpose, CTA, and Navigation
- What is the difference b/w Headline and Title?
  - Headlines describe articles inside ecosystems of something bigger — like magazines or blogs. Titles usually envelop the whole idea of your business.
  - Titles are usually — but not always — shorter than headlines.
- Various Types of WebPages?
  - get an idea from https://schema.org/WebPage

## content

> WebContent, text, multi-media, images, hyperlinks, images, audios, videos, any possible format

- Various types of content => **CONTENT_TYPE**
- Impact of content => **ENGAGEMENT**
- Marketting Campaign, Test Hypothesis, Analysise and Predict
- Depends on **WEBSITE_TYPE**, which dependes on the **DOMAIN** or Industry-TYPE
  - like E-Commerce will have specific style of data entry
    - Product Catalogue
  - Blogging Websites
  - Dashboards
  - Admin Interfaces
  - Feed Pages like
  - Discussion Forums, and Q&A Websites
  - Search Results Page

## DB Design

> A many to many relationship is typically created using a join table.

- REGISTERED_CONTENT_TYPE table with one column for each registered content-type
  - supports 0 or 1 entry, using null/valid value constraint on foreign key
  - Does not support multiple Entries?
  - One to Many Relationship?
- kNOWN_WEBSITES
- kNOWN_WEB_PAGES_TYPES
- PROJECT_WEBPAGES with CONTENT-TYPES
- Many to Many relationship on PAGE_CONTENT table from page and CONTENT-TYPES
- As you register new Content-type, remove old Content-type, update Content-type
  - run DB trigger to make new table to adjust schema
  - make migrations to adjust existing data to propogate schema adjustments
- Main domain tables are usuallt Lookup Tables with Domain Constraints
- How to add connections between database Records?
  - Many to Many relatioships in seperate tables
  - JOIN expands the Foreign keys
- Default JOIN is INNER JOIN

> In RDBMS, lists/collections are multiple entries in a mapping table which joins 2 or more lookup tables

- [Polymorphic Association](https://stackoverflow.com/questions/7000283/what-is-the-best-way-to-implement-polymorphic-association-in-sql-server)
  - Method 1 is a maintenance nightmare. Adding Object4, for example, will require full-stack changes because the Something table/classes/models/views will all have to be changed. Method 2 is better, but any referential integrity must be enforced outside the database. The last approach is the most flexible because you can (potentially) create more generic logic and UI layers on top of it, allowing for fewer changes down the road to both the schema and the things that use it.
- Composition in Database Queries and Schema definition
- Database Inheritance

> Would your SCHEMA Scale?

## Interview Questions

- https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit?usp=sharing

<iframe width="560" height="315" src="https://www.youtube.com/embed/SVvr3ZjtjI8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
