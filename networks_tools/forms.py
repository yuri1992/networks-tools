from django import forms


class FormWithRequest(forms.Form):
    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
        self.request = kwargs.pop('request')
        super(FormWithRequest, self).__init__(*args, **kwargs)