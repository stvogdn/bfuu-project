from import_export import resources
from django.contrib.auth.models import User
from .models import Profile

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        