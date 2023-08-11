from django import forms

class studentregis(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_name(self):
        vn = self.cleaned_data['name']
        if len(vn)<4:
            raise forms.ValidationError('enter valid name')
        return vn
