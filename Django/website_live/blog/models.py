from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
import re

def validate_pwd(password):
    if len(password) < 8:
        raise ValidationError("At least 8 characters")
    if not any(char.isupper() for char in password):
        raise ValidationError("At lest 1 uppercase")
    if not any(char.islower() for char in password):
        raise ValidationError("At lest 1 lowercase")
    if not any(char.isdigit() for char in password):
        raise ValidationError("At lest one numbeb")
    if not any(char in ["&", "@","!","#"] for char in password):
        raise ValidationError("At lest 1 special symbol: &, @,!,#")
    # if not re.findall("[&@!#]", password):

def validate_username(u):
    if not u.isalnum():
        raise ValidationError("Username should be alphanumeric only")
    if len(u) < 4:
        raise ValidationError("Did not pass the vibe check")

# TODO: User model class
class User(models.Model):
    username = models.CharField(max_length=150, unique=True, validators=[validate_username])
    password = models.CharField(max_length=128, validators=[validate_pwd])
    email = models.EmailField()


# TODO: Post model class
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    content = models.TextField()