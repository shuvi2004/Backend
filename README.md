# Django Backend
# Notification Service

## Setup
1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create project Setup: `django-admin startproject notification_service`
4. Create a app:`python manage.py createapp notifications`
5. Run migrations: `python manage.py migrate`
6. Create admin user: `python manage.py createsuperuser`

## Running
1. Start RabbitMQ: `docker run -d -p 5672:5672 rabbitmq`
2. Start Django: `python manage.py runserver`
3. Start Celery: `celery -A notification_service worker --loglevel=info`

## API Endpoints
- POST `/notifications/` - Send notification
- GET `/users/{id}/notifications/` - Get user notifications

## Assumptions
- Uses Django's default SQLite database
- Email uses console backend
- SMS implementation is mocked
- Retries configured with exponential backoff
