from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random,string
from django.contrib import messages

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()
        return user
    # def create_id(self,id):
    #     if not id:
    #         raise ValueError("id required")
    #     user=get_id(id)
    #     if user:
    #         return ValueError('id already exists')
    #     else:
    #         self.model

        
        

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    def generate_unique_code():
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if not User.objects.filter(id=code).exists():
                return code
    
    email = models.EmailField(unique=True, primary_key=True)
    id=models.CharField(
        max_length=20,
        unique=True,
        default=generate_unique_code
    )
    following_artists = models.ManyToManyField(
    "artist.Artist",
    through="interactions.Follows",
    symmetrical=False,
    related_name="followed_by_user"
    )
    saved_playlist=models.ManyToManyField(
        'playlists.Playlists',
        through='playlists.SavedPlaylists',
        symmetrical=False,
        related_name='saved_playlists'
    )
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=254, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_artist=models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email