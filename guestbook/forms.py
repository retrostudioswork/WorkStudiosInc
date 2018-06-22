from django import forms
#from .models import ContactForm

#class Contact_Forms(ModelForm):
 #   class Meta:
 #       model = ContactForm
#        fields = '__all__'

class ContactForm(forms.Form):
   name = forms.CharField(required=True)
   subject = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(widget = forms.Textarea)