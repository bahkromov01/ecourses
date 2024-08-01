
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView

from main.forms import LoginForm, RegisterModelForm, EmailForm
from django.contrib.auth.decorators import permission_required
from confic import settings
from django.contrib.auth.models import User

from main.tokens import account_activation_token


class Info(View):
    def get(self, request):
        return render(request, 'User/info.html')


class LoginPageView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'User/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')

        return render(request, 'app/index.html', {'form': form})


class LogoutPage(View):

    def get(self, request):
        if request.method == 'GET':
            logout(request)
            return redirect('index')
        return render(request, 'User/logout.html')


class RegisterFormView(FormView):
    template_name = 'User/register.html'
    form_class = RegisterModelForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        subject = "Verify Email"
        message = render_to_string('email/verify_email_message.html', {
            'request': self.request,
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(subject, message, to=[user.email])
        email.content_subtype = 'html'

        email.send()
        # login(self.request, user)
        return redirect('verify_email_done')


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('verify_email_complete')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'email/verify_email_confirm.html')


def verify_email_done(request):
    return render(request, 'email/verify_email_done.html')


def email_send(request):
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = settings.DEFAULT_FROM_EMAIL
            recipients = form.cleaned_data['recipients']
            send_mail(subject, message, from_email, recipients, fail_silently=False)
            sent = True
    else:
        form = EmailForm()

    return render(request, 'email/email_send.html', {'form': form, 'sent': sent})


def verify_email_complete(request):
    return render(request, 'email/verify_email_complete.html')


def verify_email(request):
    return render(request, 'email/verify_email.html')
