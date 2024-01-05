import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    is_verified = models.BooleanField(default=False)


class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f'Email verification for user {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verify_url = f'{settings.DOMAIN_NAME}{link}'

        html_content = render_to_string('users/email_verification_mail.html',
                                        {'link': verify_url})
        text_content = strip_tags(html_content)
        subject = f'Verification for user {self.user.get_full_name()}'
        from_email = settings.EMAIL_HOST
        to = [self.user.email]
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def is_expired(self):
        return True if timezone.now() >= self.expires_at else False
