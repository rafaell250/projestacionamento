from django.forms import ModelForm
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, Movmensalista

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__' #fields que se quer apresentar


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__' 


class Mov_rot_form(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__' 


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__' 


class MovmensalistaForm(ModelForm):
    class Meta:
        model = Movmensalista
        fields = '__all__' 