from django import newforms as forms
import sys

class CodeField(forms.CharField):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('This field in required')
        try:
            value = ' '.join(value.split('\r\n'))
            code = eval(value)
        except:
            raise forms.ValidationError(
                    'Problem parsing field: %s'%sys.exc_info()[0])
        return code

def RunScriptFormFactory(script):
    class RunScriptForm(forms.Form): pass
    glob = {}; loc = {}
    execfile(script, glob, loc)
    for var in loc['required']['short']:
        RunScriptForm.base_fields[var] = CodeField(required=True)
    for var in loc['required']['long']:
        RunScriptForm.base_fields[var] = CodeField(required=True, widget=forms.Textarea(attrs={'rows':'30','cols':'50'}))
    for var in loc['optional']['short']:
        RunScriptForm.base_fields[var] = CodeField(required=False)
    for var in loc['optional']['long']:
        RunScriptForm.base_fields[var] = CodeField(required=True, widget=forms.Textarea(attrs={'rows':'30','cols':'50'}))
    return RunScriptForm
