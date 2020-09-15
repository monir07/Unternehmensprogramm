from django import forms
from .models import new_iden, Iden_preview


class New_iden_form(forms.ModelForm):
    class Meta:
        model = new_iden
        fields = ['ref', 'iden_date', 'sender_shop', 'receiver_shop', 'subject', 'job_no', 'iden_body', 'attention',
                  'sender_name', 'sender_designation', 'sign','attachment']

class Preview_iden_form(forms.ModelForm):
    class Meta:
        model = Iden_preview
        fields = ['ref', 'iden_date', 'sender_shop', 'receiver_shop', 'subject', 'job_no', 'iden_body', 'attention',
                  'sender_name', 'sender_designation', 'sign','attachment']

