from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from .forms import UserLoginForm

# Create your views here.

def index(request):
	return render(request,"home.html")

def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
	return render(request,"login.html", {"form":form})

def registration(request):
	return render(request,"registration.html")

def about(request):
	return render(request,"about.html")

