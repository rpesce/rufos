from django import forms


class BuscarCliente(forms.Form):
    q = forms.EmailField(max_length=254,
                         widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                         'placeholder': 'Entre seu email para buscar seus pedidos',
                                                         'name': 'search_cliente',
                                                         'id': 'search_cliente'}),
                         label='')

