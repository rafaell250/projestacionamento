from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, Movmensalista
from .form import PessoaForm, VeiculoForm, Mov_rot_form, MensalistaForm, MovmensalistaForm



def home(request):
    context = {'menssagem' : 'ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas' : pessoas, 'form' : form}
    return render(request, 'core/lista_pessoas.html', data)


def nova_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id): #recebe a request e o id da pessoa
    data = {}  #dicionario
    pessoa = Pessoa.objects.get(id=id)  #pega a pessoa pelo id
    form = PessoaForm(request.POST or None, instance=pessoa) # a diferença para das outras vezes é que o form ja vai esta preenchido  com os dados da pessoa com o (instance=pessoa), essa ja foi identificada pelo id
    data['pessoa'] = pessoa #variavel colocada no dicionario
    data['form'] = form  #variavel colocada no dicionario

    if request.method == 'POST':  #pós edição dos dados da pessoa, clica-se em 'salvar' que dispara o metodo POST, se verdadeiro entra na condição e executa o if
        if form.is_valid:  #se o form é valido
            form.save()    #salve
            return redirect('core_lista_pessoas') 
    else: 
        return render(request, 'core/update_pessoa.html', data)  #se não houve alteração dos dados da pessoa então retorne a lista normalmente de pessoas

#NO UPDATE FIZEMOS TUDO SEPARADO (NO MUNDO REALCOSTUMA SER ASSIM POIS QUANTO MAIS COMPLEXO VAI FICANDO, MAIO A CHANCE DE CONFLITO)
#UPDATE = ACTION EM CADA TEMPLATE
#JÁ NO DELETE VAMOS USAR APENAS UM TEMPLATE DE DELETE PARA DELETAR QUALQUER ITEM DE QLQR ENTIDADE POIS SEM O 'ACTION' DEFINIDO, A URL POR PADRÃO SERA A ATUAL

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id) 
    if request.method == 'POST': 
        pessoa.delete()
        return redirect('core_lista_pessoas') 
    else: 
        return render(request, 'core/delete_confirm.html', {'obj' : pessoa}) 


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos' : veiculos, 'form' : form}
    return render(request, 'core/lista_veiculos.html', data)


def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {} 
    veiculo = Veiculo.objects.get(id=id)  
    form = VeiculoForm(request.POST or None, instance=veiculo) 
    data['veiculo'] = veiculo 
    data['form'] = form 

    if request.method == 'POST': 
        if form.is_valid:  
            form.save()    
            return redirect('core_lista_veiculos') 
    else: 
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id) 
    if request.method == 'POST': 
        veiculo.delete()
        return redirect('core_lista_veiculos') 
    else: 
        return render(request, 'core/delete_confirm.html', {'obj' : veiculo}) 


def lista_mov_rot(request):
    mov_rot = MovRotativo.objects.all()
    form = Mov_rot_form()
    data = {'mov_rot' : mov_rot, 'form' : form}
    return render(request, 'core/mov_rotativo.html', data)


def novo_mov_rot(request):
    form = Mov_rot_form(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rot')


def mov_rot_update(request, id):
    data = {}
    mov_rot = MovRotativo.objects.get(id=id)
    form = Mov_rot_form(request.POST or None, instance=mov_rot)
    data['mov_rot'] = mov_rot
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rot')
    else:
        return render(request, 'core/update_mov_rot.html', data)


def mov_rot_delete(request, id):
    mov_rot = MovRotativo.objects.get(id=id) 
    if request.method == 'POST': 
        mov_rot.delete()
        return redirect('core_lista_mov_rot') 
    else: 
        return render(request, 'core/delete_confirm.html', {'obj' : mov_rot}) 


def lista_mensalista(request):
    mensalista = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalista' : mensalista, 'form' : form}
    return render(request, 'core/lista_mensalista.html', data)


def novo_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id) 
    if request.method == 'POST': 
        mensalista.delete()
        return redirect('core_lista_mensalista') 
    else: 
        return render(request, 'core/delete_confirm.html', {'obj' : mensalista})


def lista_mov_mens(request):
    mov_mens = Movmensalista.objects.all()
    form = MovmensalistaForm()
    data = {'mov_mens' : mov_mens, 'form' : form}
    return render(request, 'core/mov_mensalista.html', data)


def mov_mensalista_novo(request):
    form = MovmensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_mens')


def mov_mensalista_update(request, id):
    data = {}
    mov_mens = Movmensalista.objects.get(id=id)
    form = MovmensalistaForm(request.POST or None, instance=mov_mens)
    data['mov_mens'] = mov_mens
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mens')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)


def mov_mensalista_delete(request, id):
    mov_mens = Movmensalista.objects.get(id=id) 
    if request.method == 'POST': 
        mov_mens.delete()
        return redirect('core_lista_mov_mens') 
    else: 
        return render(request, 'core/delete_confirm.html', {'obj' : mov_mens})