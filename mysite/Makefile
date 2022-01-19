-include .env
image_name = avi/backend

# Set GCP configurations.
setup:
	@gcloud config set project ${GCP_PROJECT}
	@gcloud config set gcloudignore/enabled true
	@gcloud config set functions/region ${GCP_REGION}
	@gcloud config set run/region ${GCP_REGION}
	@gcloud config set run/platform managed

prod:
	gunicorn -w 4 mysite.wsgi

build:
	docker build --tag ${image_name} .

run: build
	docker run --rm -p 8000:8000 --env-file .env ${image_name}

deploy: setup
	gcloud run deploy mysite --allow-unauthenticated --source .

test:
	echo "secret ${GMAIL_PASS}"

# https://github.com/wptide/wptide.org/blob/ee3af4e072a08279adb01dd88396af08d7e9a82a/Makefile