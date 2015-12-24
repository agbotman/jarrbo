from django.shortcuts import render
from registration.backends.hmac.views import RegistrationView as HmacRegistrationView
from jarrbo.forms import RegistrationForm


def jarrbo_home(request):
    return render(request, 'jarrbo_home.html',)
    
class RegistrationView(HmacRegistrationView):
    """
    Register a new (inactive) user account, generate an activation key
    and email it to the user.
    
    The email field will be used as the unique identifier for the user
    The username field is ignored and a dummy unique value will be generated
    """

    form_class = RegistrationForm

    def create_inactive_user(self, form):
        """
        Create the inactive user account and send an email containing
        activation instructions.
        The current time (now()) is used to generate an unique username 
        """
        from datetime import datetime
        new_user = form.save(commit=False)
        username = 'User' + str(datetime.now())
        username = username.replace(' ','_')
        new_user.username = username
        new_user.is_active = False
        new_user.save()
        self.send_activation_email(new_user)

        return new_user

