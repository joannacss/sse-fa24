from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from blog.models import User


def index(request):
    context = {'course': "CSE-60770", 'semester': 'FA24'}
    return render(request, 'blog/index.html', context)


# TODO: implement register
def register(request):
    if request.POST:
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        email = request.POST["email"]
        user = User(username=username, password=pwd, email=email)
        try:
            user.full_clean()
            # vibe has passed
            user.password = make_password(pwd)
            user.save()
            return HttpResponseRedirect(reverse("blog:login"))
        except ValidationError as e:
            return render(request, "blog/register.html", {
                "errors": e
            })

    return render(request, "blog/register.html")


# TODO: sign in feature
## This version below has SQL Injection. To exploit:
# username: ' OR 1=1; --
# password: anything
## This will bypass the authentication
def login(request):
    errors = None
    if request.POST:
        # Create a model instance and populate it with data from the request
        uname = request.POST["username"]
        pwd = request.POST["password"]
        hashed_password = make_password(pwd)
        user = User.objects.raw(f"SELECT * FROM blog_user WHERE username='{uname}' AND password='{hashed_password}'")
        if len(user) > 0:
            # create a new session
            request.session["user"] = uname
            return HttpResponseRedirect(reverse('blog:list_posts'))
        else:
            errors = [('authentication', "Login error")]

    return render(request, 'blog/login.html', {'errors': errors})



# TODO: sign out feature (delete data from request.session, redirect to login)
def logout(request):
    return HttpResponse("logout TBD")


# TODO: create post feature
def create_post(request):
    return HttpResponse("create post TBD")


# TODO: list all posts
def list_posts(request):
    return HttpResponse("list all posts TBD")


# TODO: view a specific post
def view_post(request, post_id):
    return HttpResponse("view post TBD")
