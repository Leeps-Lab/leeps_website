from django import newforms as forms
import sys

class CodeField(forms.CharField):
    def clean(self, value):
        if not value:
            if not self.required:
                value = '""'
            else:
                raise forms.ValidationError('This field is required')
        try:
            glob = {}; loc = {}
            code = compile(value.replace('\r\n', '\n'), '<string>', 'exec')
        except:
            raise forms.ValidationError('Problem parsing field')
        return value

class RunScriptForm(forms.Form):
    input = CodeField(required=True, widget=forms.Textarea(attrs={'rows':'30','cols':'50'}))
    output_type = forms.ChoiceField(choices=(
        ('png','png'),('svg','svg'),('jpg','jpg')))
