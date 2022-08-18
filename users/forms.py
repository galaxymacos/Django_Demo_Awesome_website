from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    # Create a form for entering user info, extends Django's UserCreationForm
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
