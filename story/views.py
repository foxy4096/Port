from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import StoryForm, StoryLinkForm, ReplyStoryForm
from .models import Story


@login_required
def submit_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()
            messages.success(request, "Story added successfully!")
            return redirect("home")
    form = StoryForm()
    return render(request, "story/submit_story.html", {"form": form})


@login_required
def submit_story_link(request):
    if request.method == "POST":
        form = StoryLinkForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()
            messages.success(request, "Story added successfully!", extra_tags="ok")
            return redirect("home")
    form = StoryLinkForm(request.GET)
    return render(request, "story/submit_story.html", {"form": form})


def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    reply_form = ReplyStoryForm()
    return render(
        request, "story/story_detail.html", {"story": story, "rform": reply_form}
    )


@login_required
def delete_story(request, pk):
    story = get_object_or_404(Story, pk=pk, created_by=request.user)
    if request.method == "POST":
        story.delete()
        messages.warning(request, "Story deleted successfully!", extra_tags="ok")
        return redirect("home")
    return render(request, "story/delete_story.html", {"story": story})


@login_required
def reply_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        form = ReplyStoryForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.reply_to = story
            reply.created_by = request.user
            reply.save()
            messages.success(request, "Reply added successfully!", extra_tags="ok")
            return redirect("story_detail", story.pk)

    return render(request, "story/reply_story_form.html", {"rform": form})


@login_required
def vote_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    story.vote(request.user)
    return render(request, "story/islands/votes.html", {"story": story})

    