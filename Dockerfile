FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Car_Shopping/ .

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=Car_shop.settings

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Car_shop.wsgi:application"]