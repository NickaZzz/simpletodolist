from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages, auth
from accounts.models import Token
import sys

def send_login_email(request):
    email = request.POST.get('email', '')
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
      'Your login link for SimpleToDoList',
      message_body,
      'noreply@superlists',
      [email], 
    )
    messages.success(
        request,
        "Check your email, we send you a link that you can use to enter the site."
    )

    return redirect('/')


def login(request):
    user = auth.authenticate(request=None, uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')
