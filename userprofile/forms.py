from django import forms

from .models import User, Userprofile


class UserprofileEditForm(forms.ModelForm):
    """Form definition for UserEdit."""

    class Meta:
        """Meta definition for UserEditform."""

        model = Userprofile

        fields = ("about",)


class UserEditForm(forms.ModelForm):
    """Form definition for UserEdit."""

    email = forms.EmailField(
        required=True,
        help_text="Only admins see your email below. To share publicly, add to the 'about' box.",
    )

    class Meta:
        """Meta definition for UserEditform."""

        model = User
        fields = ("email",)
