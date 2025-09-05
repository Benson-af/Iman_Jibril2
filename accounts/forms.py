from django import forms
from .models import OtherDonation



class OtherDonationForm(forms.ModelForm):
    class Meta:
        model = OtherDonation
        fields = [ 'name', 'email', 'number', 'category', 'comment']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'styled-select',
                'style': 'width:100%;padding:10px;border-radius:8px;border:1px solid #d0dd94;font-size:1rem;margin-bottom:16px;'
            }),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Specify your message...'}),
        }