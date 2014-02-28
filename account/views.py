from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.views import logout


def index(request):
    return render_to_response('index.html',
                              RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect(reverse('index'))


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render_to_response('signup.html',
                              {'new_user_form': form},
                              RequestContext(request))

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect(reverse('index'))

    return render_to_response('login.html',
                              RequestContext(request))
