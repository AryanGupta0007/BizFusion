from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["Password"]
        except Exception as error:
            return HttpResponseRedirect(request, "registration/signup.html")
        else:

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("global_index"))
            else:
                return HttpResponseRedirect(reverse("login"))
    return render(request, "registration/login.html")


def user_signup(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["Password"]
            email = request.POST["email id"]
            conf_password = request.POST["Conform Password"]
            print(username, password, email, conf_password)

        except Exception:
            return HttpResponseRedirect(reverse("signup"))
        else:
            if password == conf_password:
                user_already_exists = User.objects.filter(email=email).filter(username=username)
                if user_already_exists:
                    return HttpResponseRedirect(reverse("signup"))
                else:
                    new_user = User.objects.create_user(username=username, email=email, password=password)
                    new_user.save()
                    return HttpResponseRedirect(reverse("global_index"))
            else:
                return HttpResponseRedirect(reverse("signup"))

    return render(request, "registration/signup.html")