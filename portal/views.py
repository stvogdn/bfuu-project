from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    return render(request, 'portal/home.html')


def about(request):
    return render(request, 'portal/about.html', {'title': 'About'})

