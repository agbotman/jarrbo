from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from registration.backends.hmac.views import RegistrationView as HmacRegistrationView
from jarrbo.forms import RegistrationForm, ContactForm
from django.core.mail import send_mail

def jarrbo_home(request):
    return render(request, 'jarrbo_home.html',)
    
def ContactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['ton@jarrbo.nl'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thanks/')
    
    return render(request, 'contact.html', {
        'form': form,
    })
    
def ThanksView(request):
    return render(request, 'contact_thanks.html',)
    
def ProfileView(request):
    return render(request, 'profile.html',)
    
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


