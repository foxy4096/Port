from django.shortcuts import render
from story.models import Story


def frontpage(request):
    stories = Story.objects.all()
    return render(request, "core/frontpage.html", {"stories": stories})
