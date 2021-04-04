from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    attach = forms.Field(widget = forms.FileInput)

    def __str__(self):
        return self.Email