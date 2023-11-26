from django.urls import path

from . import views

urlpatterns = [
    path("submit/", views.submit_story, name="submit"),
    path("submit/link/", views.submit_story_link, name="submit_link"),
    path("story/<int:pk>/", views.story_detail, name="story_detail"),
    path("story/<int:pk>/delete/", views.delete_story, name="story_delete"),
    path("story/<int:pk>/reply/", views.reply_story, name="reply_story"),
    path("story/<int:pk>/vote/", views.vote_story, name="vote_story"),

    # Search
    path("search/", views.search_story, name="search_story"),

]
