from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from charityproject.charity.models import charityInfo
from django import forms

class RegistrationForm(forms.Form):
    addr1=forms.CharField(
        max_length=40,
        required=True,
    )
	
    addr2=forms.CharField(
        max_length=40,
        required=True,
    )
	
    addr3=forms.CharField(
        max_length=40,
        required=False,
    )
	
    addr4=forms.CharField(
        max_length=40,
        required=False,
    )
	
    pri_phone_number=forms.IntegerField(
        max_length=40,
        required=False,
    )
	
    sec_phone_numer=forms.IntegerField(
        max_length=40,
        required=False,
    )
	
    email=forms.Emailfield(
        max_length=40,
        required=True,
    )
	
    charity_description=forms.Charfield(
        max_length=1000,
        required=False,
    )
	
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))