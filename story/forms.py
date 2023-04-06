from django import forms

from .models import Story


class StoryForm(forms.ModelForm):
    """Form definition for Story."""

    class Meta:
        """Meta definition for Storyform."""

        model = Story
        fields = (
            "title",
            "url",
            "content",
        )
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "style": """height: 120px;""",
                }
            ),
        }


class StoryLinkForm(forms.ModelForm):
    """Form definition for StoryLink."""

    class Meta:
        """Meta definition for StoryLinkform."""

        model = Story
        fields = (
            "title",
            "url",
        )


class ReplyStoryForm(forms.ModelForm):
    """Form definition for ReplyStoryForm."""

    title = forms.CharField(
        required=True,
        label="Comment",
        widget=forms.Textarea(attrs={"rows": 5, "cols": 85}),
    )

    class Meta:
        """Meta definition for ReplyStoryForm."""

        model = Story
        fields = ("title",)
