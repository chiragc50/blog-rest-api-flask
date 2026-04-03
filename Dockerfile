FROM python:3.13.0-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP="api:create_app"
ENV ENVIRONMENT="production"

EXPOSE 80

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "api:create_app()"]
