from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.mixin import TitleMixin
from users.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from users.models import EmailVerification, User


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True
    redirect_url = reverse_lazy('index')
    success_message = "You logged in successfully! Welcome."


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = ("The user has been successfully created."
                       " Now you can log in.")


class UserProfileView(TitleMixin, SuccessMessageMixin, UpdateView):
    model = User
    title = 'Profile'
    template_name = 'users/profile.html'
    form_class = UserUpdateForm
    success_message = 'Your profile was successfully updated.'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Email Verification'

    def get_context_data(self, **kwargs):
        user = User.objects.get(email=kwargs['email'])
        code = kwargs.get('code')
        email_verification = EmailVerification.objects.filter(user=user, code=code)

        context = super(EmailVerificationView, self).get_context_data(**kwargs)

        if email_verification.exists() and not email_verification.last().is_expired():
            user.is_verified = True
            user.save()
            context['message_head'] = 'Congratulations'
            context['message'] = 'Your account has been successfully verified!'
            return context
        else:
            context['message_head'] = 'Oops! Something went wrong'
            context['message'] = ('We could not verify your email address.'
                                  ' Make sure the link is active (48 hours after receiving the email).')
            return context
