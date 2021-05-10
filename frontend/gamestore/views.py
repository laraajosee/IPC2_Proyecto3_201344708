from os import name
from django.shortcuts import render
from .forms import GraficarForm, GraficarForm2, LeerForm, LoginForm, RegisterForm, RetornoForm
import requests
import json
from django.core.files.storage import FileSystemStorage
# Create your views here.

endpoint = 'http://127.0.0.1:5000/'
def home(request):
    response = requests.get(endpoint+'games');
    games = response.json()
    contexto = {
        'games' : games
    }
    return render(request, 'store.html', contexto)



def about(request):
    context = {
        'title':'about'
    }
    return render(request, 'about.html', context)

def login(request):
    context = {
        'title':'Login'
    }
    return render(request, 'signup.html', context)

def registro(request):
    context = {
        'title':'Registro'
    }
    return render(request, 'signup.html', context)

def ayuda(request):
    context = {
        'datos':'Jose Manuel Lara Elias - 201344708'
    }
    return render(request, 'ayuda.html', context)

def ayuda1(request):
    context = {
        'title':'hola'
    }
    return render(request, 'ayuda.html', context)


def RecibirTexto(request):
    contexto ={}
    if request.method == 'GET':
        form = RetornoForm(request.GET)
        if form.is_valid():
            response = requests.get(endpoint+'/stats');
         
            contexto= {
                'texto': response.text,     
            }
        else:
            print('F')
    return render(request, 'signup.html', contexto)

def signup(request):
    contexto ={}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form2 = RetornoForm(request.GET)
            response = requests.get(endpoint+'/stats');
            name = form.data['name']
            pload = {'nombre':name}

            r = requests.post(endpoint+'/events',json=pload);
            contexto={
                'textoEntrada': name,
                'texto': response.text
            }
        else:
            print('F')
            
    return render(request, 'signup.html', contexto)


def graficar(request):
    contexto ={}
  
    if request.method == 'GET':
        form = GraficarForm(request.GET)
        if form.is_valid():
            result = request.GET['comboBox']
            pload = {'data':result}
            r = requests.post(endpoint+'/fecha',json=pload);
            k = r.json()
            response = requests.get(endpoint+'comboBox')
            data = response.json()
            h = requests.post(endpoint+'/cantidad',json=pload);
            p = h.json()
            contexto={
                'pastel': p['data'],
                'grafica': k['data'],
                'games' : data['hola'],
                'listaErrores': data['adios']
            }
 
    return render(request, 'upload.html', contexto)

def graficar2(request):
    contexto={

    }
    if request.method == 'GET':
        form = GraficarForm2(request.GET)
        print("entrando a graficar2")
        if form.is_valid():
            print("el form es valido")
            result = request.GET['comboBox2']
            response = requests.get(endpoint+'comboBox')
            data = response.json()
            pload = {'data':result}
            r = requests.post(endpoint+'/error',json=pload);
            k = r.json()
            print(k['data'])
            print(k['data2'])
            contexto={
                'pastel2': k['data2'],
                'grafica2': k['data'],
                'games' : data['hola'],
                'listaErrores': data['adios']
            }
    return render(request, 'upload.html', contexto)        

def cargarGrafica(request):
    response = requests.get(endpoint+'comboBox')
    data = response.json()
    contexto = {
        'games' : data['hola'],
        'listaErrores': data['adios']
    }
    print("cargar grafica")
    return render(request, 'upload.html', contexto)



def upload(request):
    contexto ={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
     
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    
        data = open('C:/Users/che/Desktop/IPC2_Proyecto3_201344708/'+uploaded_file.name, 'r+', encoding='utf-8')
        hola = data.read()
        contexto= {
            'textoEntrada': hola
        }
   
    return render(request, 'signup.html', contexto)

