from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Seu nome')
    mensagem = forms.CharField(widget=forms.Textarea, label='Mensagem')

    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
   
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    
