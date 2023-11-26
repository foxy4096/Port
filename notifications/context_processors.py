from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        return {
            "unread_notifications": Notification.objects.filter(
                recipient=request.user, is_read=False
            ),
            "notifications": Notification.objects.filter(recipient=request.user),
        }
    else:
        return {"notifications": None}
