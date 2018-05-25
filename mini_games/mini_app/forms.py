from django import forms
from mini_app.models import feedback_model

# class archery_board_form(forms.ModelForm):
#     score = forms.CharField(widget =forms.HiddenInput(),required =False)
#     class Meta():
#         model = archery_board
#         fields = '__all__'



class feedback_form(forms.ModelForm):
    feedback = forms.CharField( widget=forms.Textarea)
    class Meta():
        model = feedback_model
        fields = '__all__'
