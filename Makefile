mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

user:
	python3 manage.py createsuperuser --username=admin --email=admin@gmail.com

sort:
	black .
	isort .

test:
	python manage.py test