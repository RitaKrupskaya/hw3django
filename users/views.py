import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    template_name = "users/register_form.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(13)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"https://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Добрый день, это Fitness Power. Для подтверждения почты перейдите по ссылке:{url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ResetPasswordView(PasswordResetView):
    template_name = "users/reset_password.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        if user:
            password = secrets.token_urlsafe(13)
            send_mail(
                subject="Восстановление пароля",
                message=f"Добрый день, это Fitness Power. Ваш новый пароль: {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            user.set_password(password)
            user.save()
            return redirect(reverse("users:login"))

        else:
            return redirect(reverse("users:reset_password"))


class UserProfileView(UpdateView):
    model = User
    template_name = "users/profile_form.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
