from django import forms


class BuscarCliente(forms.Form):
    q = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                         'placeholder': 'Seu email',
                                                         'name': 'search_cliente',
                                                         'id': 'search_cliente'}),
                           label='')