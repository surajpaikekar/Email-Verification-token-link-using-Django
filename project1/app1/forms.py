from django import forms

class EmailVerificationForm(forms.Form):
    email = forms.EmailField()









# from django import forms
# from .models import Profile
#
# class ProfileForms(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = "__all__"