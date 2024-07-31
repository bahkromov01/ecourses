from django.urls import path

from main.views.auth import Info, LogoutPage, LoginPageView, RegisterFormView, verify_email_done, verify_email_confirm, email_send
from main.views.views import IndexPage, about, contact

urlpatterns = [
    path('index/', IndexPage.as_view(), name='index'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),

    path('info/', Info.as_view() , name='info'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('send_email/', email_send, name='send_email'),

    # sending massage

    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify_email_confirm')
]