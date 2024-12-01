from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpResponse
from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/signup.html', {'form': form})

    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Check if the email exists in the database
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(user.pk.encode('utf-8'))

            # Generate the reset URL
            reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )

            # Send the password reset email
            send_mail(
                'Password Reset Request',
                f'Click the following link to reset your password: {reset_url}',
                'your-email@example.com',  # Replace with your actual email
                [email],
                fail_silently=False,
            )

            # Add a success message to be shown in the template
            return render(request, "users/password_reset.html", {
                'message': 'Password reset link has been sent to your email.'
            })

        else:
            # Add an error message to be shown in the template if email is not registered
            return render(request, "users/password_reset.html", {
                'message': 'Email not registered. Please check the email address and try again.'
            })

    return render(request, "users/password_reset.html")


def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        # Check if the token is valid
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = SetPasswordForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('password_reset_complete')
            else:
                form = SetPasswordForm(user)
            return render(request, 'password_reset_confirm.html', {'form': form})

        else:
            return HttpResponse("Invalid token.", status=400)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
