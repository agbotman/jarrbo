"""
URLconf for registration and activation, using django-registration's
HMAC activation workflow.
Amended views for using email as the unique identifier and ignore the username field

"""

from django.conf.urls import url

from jarrbo.views import RegistrationView, ContactView, ThanksView, ProfileView
from django.contrib.auth import views as auth_views
from jarrbo.forms import PasswordResetFormJarrbo, SetPasswordFormJarrbo, PasswordChangeFormJarrbo


urlpatterns = [
    url(r'^contact/$', ContactView, name='contact'),
    url(r'^contact/thanks', ThanksView, name='thanks'),
    url(r'^profile/$', ProfileView, name='profile'),
    url(r'^register/$',
        RegistrationView.as_view(),
        name='registration_register'),
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect': 'auth_password_reset_done',
         'email_template_name': 'registration/password_reset_email.txt',
         'password_reset_form': PasswordResetFormJarrbo},
        name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect': 'auth_password_reset_complete',
         'set_password_form': SetPasswordFormJarrbo},
        name='auth_password_reset_confirm'),
    url(r'^password/change/$',
        auth_views.password_change,
        {'post_change_redirect': 'auth_password_change_done',
         'password_change_form': PasswordChangeFormJarrbo},
        name='auth_password_change'),

]
