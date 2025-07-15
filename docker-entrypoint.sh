#!/usr/bin/env bash

echo "RUNNING Question App Backend..."

echo "Waiting for Question App Backend POSTGRESQL Database..."
while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do sleep 2; done
echo "Connected to Question App Backend POSTGRESQL Database"


if [[ $# -gt 0  ]]; then
	echo "Execute Command..."
	INPUT=$@
	sh -c "$INPUT"
else
	mkdir -p /var/logs/application_logs

	if [[ "$DEBUG" = "True" ]]; then
		python /home/question_app/manage.py migrate --noinput
		if [ $? -ne 0 ]; then
			echo "Migration Question App Backend POSTGRESQL DB failed." >&2
			exit 1
		fi
	fi

	echo "Creating superuser if not exists..."
	python /home/question_app/manage.py shell < /home/question_app/scripts/create_superuser.py

	echo "Starting Gunicorn for wrench ..."

	exec gunicorn config.wsgi:application \
	   --name question_app-gunicorn \
	   --bind 0.0.0.0:8080 \
	   --workers $GUNICORN_WORKER_NUMBER \
	   --pythonpath "/home/question_app/" \
	   --log-level=info \
	   --log-file=- \
	   --timeout $GUNICORN_TIMEOUT \
	   --reload
fi

