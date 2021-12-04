image_name = avi/backend

prod:
	gunicorn -w 4 mysite.wsgi

build:
	docker build --tag ${image_name} .

run: build
	docker run --rm -p 8000:8000 ${image_name}