from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer
from .tasks import send_notification_task

@api_view(['POST'])
def send_notification(request):
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        notification = serializer.save()
        send_notification_task.delay(notification.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_notifications(request, id):
    notifications = Notification.objects.filter(user__id=id)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)