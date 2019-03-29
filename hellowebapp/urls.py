from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from django.views.generic import TemplateView

from collection import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/',
        TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/',
        TemplateView.as_view(template_name='contact.html'), name='contact'),

    path('things/<slug>/', views.thing_detail, name='thing_detail'),
    path('things/<slug>/edit/', views.edit_thing, name='edit_thing'),

    path('accounts/password/reset/',
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    path('accounts/password/reset/done/',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('accounts/password/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('accounts/password/done/',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
