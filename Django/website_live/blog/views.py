from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from blog.models import User, Post


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
        user = User.objects.filter(username=uname)

        if len(user) > 0:
            user_obj = user[0]
            print("user obj", user_obj)
            if check_password(pwd, user_obj.password):
                # create a new session
                request.session["user"] = uname
                return HttpResponseRedirect(reverse('blog:list_posts'))
        else:
            errors = [('authentication', "Username & pwd combination doesnt match the records")]

    return render(request, 'blog/login.html', {'errors': errors})


# TODO: sign out feature (delete data from request.session, redirect to login)
def logout(request):
    del request.session["user"]
    return HttpResponseRedirect(reverse('blog:login'))


# TODO: create post feature
def create_post(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect(reverse("blog:login"))
    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        logged_user = User.objects.filter(username=request.session["user"])[0]
        post = Post(
            title=title,
            content=content,
            user=logged_user
        )
        post.save()
        return HttpResponseRedirect(reverse("blog:list_posts"))

    return render(request, "blog/create.html")


# TODO: list all posts
def list_posts(request):
    all_post = Post.objects.all()
    return render(request, "blog/list.html", {
        "posts": all_post
    })


# TODO: view a specific post
def view_post(request, post_id):
    p = Post.objects.filter(id=post_id)
    if len(p) > 0:
        post = p[0]
        return render(request, "blog/view.html", {
            "post": post
        })

    return HttpResponse("view post TBD")
