from django import newforms as forms
import StringIO

class PlayersField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('Game has no players')
        players = value.split(',')
        players = ['"%s"'%player.strip() for player in players]
        players = ','.join(players)
        try:
            players =  eval(players)
        except:
            raise forms.ValidationError('Problem parsing players')
        if len(players) < 2:
            raise forms.ValidationError('Need at least 2 players')
        return players

class PayoffsField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('Game has no payoff vector')
        payoffs = '(%s)' % value
        try:
            payoffs = eval(payoffs)
        except:
            raise forms.ValidationError('Problem parsing payoffs')
        if len(payoffs) < 2:
            raise forms.ValidationError('Need at least 2 items in payoff vector')
        return payoffs

class InfoSetsField(forms.Field):
    def clean(self, value):
        if not value:
            return []
        try:
            infosets = eval('[%s]'%value)
        except:
            raise forms.ValidationError('Problem parsing information sets')
        return infosets

class TreeField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('Game needs a tree!')
        stmt = 'tree = '+' '.join(value.split('\r\n'))
        vars = {}
        try:
            exec(stmt, {}, vars)
        except:
            raise forms.ValidationError('Bad tree')
        return vars['tree']

class RunScriptForm(forms.Form):
    name = forms.CharField()
    players = PlayersField(widget=forms.TextInput(
        attrs={'size':'50'}))
    payoffs = PayoffsField(widget=forms.TextInput(
        attrs={'size':'50'}))
    initial_node = forms.CharField(widget=forms.TextInput(attrs={'size':'20'}))
    tree = TreeField(widget=forms.Textarea(
        attrs={'rows':'30','cols':'50'}))
    information_sets = InfoSetsField(widget=forms.TextInput(
        attrs={'size':'50'}), required=False)
