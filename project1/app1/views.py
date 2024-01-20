from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile
from .utils import send_email_token
import uuid


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(username=email)
        except User.DoesNotExist:
            user_obj = User(username=email)
            user_obj.set_password(password)
            user_obj.save()
        try:
            profile_obj = Profile.objects.get(User=user_obj)
        except Profile.DoesNotExist:
            profile_obj = Profile.objects.create(
                User=user_obj,
                email_token=str(uuid.uuid4())
            )
        else:
            # If a profile object with the given email already exists, update the email token
            profile_obj.email_token = str(uuid.uuid4())
            profile_obj.is_verified = False
            profile_obj.save()

        verify_url = request.build_absolute_uri(
            reverse('verify_url', kwargs={'token': profile_obj.email_token})
        )
        send_email_token(email, verify_url)
        return HttpResponse("An email has been sent to your email address. Please follow the instructions in the email to verify your account.")
    return render(request, "app1/home.html")



def verify(request, token):
    try:
        profile_obj = Profile.objects.get(email_token=token)
        if not profile_obj.is_verified:
            profile_obj.is_verified = True
            profile_obj.save()
            return HttpResponse("Your account has been verified. You can now log in.")
        else:
            return HttpResponse("Your account has already been verified.")
    except Profile.DoesNotExist:
        return HttpResponse("Invalid token.")
