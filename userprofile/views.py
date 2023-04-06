from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, UserprofileEditForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Account created for {user.username}!", extra_tags="ok"
            )
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "userprofile/signup.html", {"form": form})


def get_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        uform = UserEditForm()
        pform = UserprofileEditForm()
        return render(
            request,
            "userprofile/user.html",
            {"pform": pform, "uform": uform, "tuser": user},
        )
    return render(request, "userprofile/user.html", {"tuser": user})


@login_required
def edit_profile(request):
    if request.method == "POST":
        uform = UserEditForm(request.POST)
        pform = UserprofileEditForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            pform.save()
            messages.success(request, f"Profile updated for {user.username}!")
        return redirect("user-profile", request.user)
    return redirect("user-profile", request.user)
