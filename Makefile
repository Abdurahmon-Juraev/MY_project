mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

lang:
	django-admin makemessages -l uz -l en -l ru

compile:
	django-admin compilemessages -i .venv