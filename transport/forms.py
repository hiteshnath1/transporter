from django import forms
from .models import transport,branches
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class transportSearchForm(forms.Form):
    source = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Source'}))
    destination = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Destination'}))

class transportForm(forms.ModelForm):
    
    class Meta:
        model = transport
        fields = ('name','address','logo','mobile_no','landline_no','email','transporter_id')

class branchesForm(forms.ModelForm):
    
    class Meta:
        model = branches
        fields = ("name","address",'mobile_no','landline_no','email')

class signUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(Again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email ID'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class':'form-control'}),
                   'last_name': forms.TextInput(attrs={'class':'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }
