from django import newforms as forms
import traceback

class CodeField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('This field in required')
        try:
            code = eval(value)
        except:
            raise forms.ValidationError(
                    'Problem parsing field: %s'%traceback.exc_info()[0])
        return code

def RunScriptFormFactory(script):
    glob = {}; loc = {}
    execfile(script, glob, loc)
    print loc
    class RunScriptForm(forms.Form): pass
    return RunScriptForm()
