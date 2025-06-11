from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Seu nome')
    email = forms.EmailField(label='Seu e-mail')
    celular = forms.CharField(max_length=20, label='Celular')
    mensagem = forms.CharField(widget=forms.Textarea, label='Mensagem')

    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    celular = forms.CharField(
        label='Celular',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    
