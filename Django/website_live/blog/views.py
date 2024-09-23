from django.shortcuts import render


def index(request):
    context = {'course': "CSE-60770", 'semester': 'FA24'}
    return render(request, 'blog/index.html', context)


# TODO: implement register
def register(request):
    pass


# TODO: sign in feature
def login(request):
    pass


# TODO: sign out feature (delete data from request.session, redirect to login)
def logout(request):
    pass


# TODO: create post feature
def create_post(request):
    pass


# TODO: list all posts
def list_posts(request):
    pass


# TODO: view a specific poster
def view_post(request, post_id):
    pass
