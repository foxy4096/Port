from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required
def notification_page(request):
    return render(request, "notifications/notification.html")

@login_required
def notification_redirect(request, id):
    notification = get_object_or_404(Notification, pk=id)
    notification.is_read = True
    notification.save()
    if notification.object_type == "story":
        return redirect("story_detail", notification.object_id)
    else:
        return redirect("home")