from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe

class JarrboForm():
    def as_jarrbo(self):
        from django.forms.widgets import Textarea
        textarea = Textarea()
        output = []
        html_input_attrs = ['value', 'readonly', 'disabled', 'size', 'maxlength',
                            'max_length', 'min_length',
                            'autocomplete', 'autofocus', 'form', 'formaction', 'formenctype',
                            'formmethod', 'formnovalidate', 'formtarget', 'height', 'width',
                            'list', 'min', 'max', 'multiple', 'pattern', 'placeholder', 
                            'required', 'step']
        label_row = '<label for="id_%s" class="col-sm-3 control-label">%s%s</label>'
        input_textarea = '<div class="col-sm-9"><textarea class="form-control" id="id_%s" name="%s"></textarea></div>'
        input_start = '<div class="col-sm-9"><input class="form-control" type="%s" name=%s'
        input_end = '></div>'
        error_row = '<div class="col-sm-9 col-sm-offset-3 help-block">%s</div>'
        for field in self:
            if field.errors:
                output.append('<div class="form-group has-error">')
            else:
                output.append('<div class="form-group">')
            if field.field.required:
                required = ' *'
            else:
                required = ''
            output.append(label_row % (field.name, field.label, required))
            if type(field.field.widget) == type(textarea):
                input_str = [input_textarea % (field.name, field.name)]
            else:
                input_str = [input_start % (field.field.widget.input_type, field.name)]
                for attr in html_input_attrs:
                    value = getattr(field.field,attr,None)
                    if value:
                        if attr == 'max_length':
                            input_str.append('maxlength=%s' % value)
                        elif attr == 'min_length':
                            input_str.append('minlength=%s' % value)
                        else:
                            input_str.append('%s=%s' % (attr, value))
                input_str.append(input_end)
            output.append(' '.join(input_str))
            if field.errors:
                output.append(error_row % field.errors.as_text())
            output.append('</div>')
        return mark_safe('\n'.join(output))

class ContactForm(forms.Form, JarrboForm):
    email = forms.EmailField(label=_("Your email address"), required=True)
    subject = forms.CharField(label=_("Subject"), required=True)
    message = forms.CharField(
        label=_("Message"),
        required=True,
        widget=forms.Textarea
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


        
class RegistrationForm(UserCreationForm, JarrboForm):
    """
    Form for registering a new user account.

    Ignores the username field and checks wether the email address is unique
    """
    class Meta(UserCreationForm.Meta):
        fields = [
            'email',
            'password1',
            'password2'
        ]
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def clean_email(self):
        email = self.cleaned_data["email"]
        err_email_already_exists = _("This email address is already registered. Did you forget your password?")
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError(err_email_already_exists)
        except User.DoesNotExist:
            return email
            
class PasswordResetFormJarrbo(PasswordResetForm, JarrboForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetFormJarrbo, self).__init__(*args, **kwargs)
        
class SetPasswordFormJarrbo(SetPasswordForm, JarrboForm):

    def __init__(self, user, *args, **kwargs):
        super(SetPasswordFormJarrbo, self).__init__(user, *args, **kwargs)

class PasswordChangeFormJarrbo(PasswordChangeForm, JarrboForm):

    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeFormJarrbo, self).__init__(user, *args, **kwargs)
        self.fields.keyOrder = ['old_password', 'new_password1', 'new_password2']



