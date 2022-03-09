# Deployments

## Why is it difficult

1. expose and run docker service on right port and host
2. Handle external database
3. Handle external static files repository/location
4. Handle Secrets to stateless containers
5. Allow right HOST once deployed as stateless service

Blue :large_blue_circle: /Green :green_circle: Deployment

### Static files and images

These specifics – 2.5 megabytes; /tmp; etc. – are “reasonable defaults” which can be customized as described in the next section.
https://docs.djangoproject.com/en/dev/topics/http/file-uploads/#where-uploaded-data-is-stored

- django need to be configured to store bigger image files
- How to deal with CSRFToken using RESTAPI
  - read csrf_token from cookies and attach it to requests
  - Django might NOT set the cookie for you in advance. use `@ensure_csrf_cookie` decorator on view
  - https://djangocentral.com/uploading-images-with-django/
  - https://stackoverflow.com/questions/50732815/how-to-use-csrf-token-in-django-restful-api-and-react

- [ ] HighScalability: How do I organize millions of images?
- [ ] Best Practices for Building & Maintaining an Image Database
  - Typically? As files. On a disk. Then store the paths to those files in a database for easy lookup. (Or store a key that can be used by some network service to find the file and stream it.)
  - https://stackoverflow.com/questions/17848069/where-does-facebook-store-multi-millions-of-images-and-videos-in-database-or-so