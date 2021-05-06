from os import name
from django.shortcuts import render
from .forms import LeerForm, LoginForm, RegisterForm, RetornoForm
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

def signin(request):
    contexto ={}
    if request.method == 'GET':
        form = LoginForm(request.GET)
        print(form)
        if form.is_valid():
            user = form.cleaned_data['username']
            passw  =form.cleaned_data['password']
            r = requests.get(endpoint+'/login/'+user+'/'+passw);
            data = r.json()
            print(data['data'])
            if data['data']==True:
                response = requests.get(endpoint+'games');
                games = response.json()
                contexto = {
                'games' : games,
                'user':user
                }
    return render(request, 'store.html', contexto)

def RecibirTexto(request):
    contexto ={}
    if request.method == 'GET':
        form = RetornoForm(request.GET)
        if form.is_valid():
            response = requests.get(endpoint+'/stats');
            
            contexto= {
                'texto': response.text 
            }
        
        else:
            print('F')
    return render(request, 'signup.html', contexto)

def signup(request):
    contexto ={}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            pload = {'nombre':name}
            r = requests.post(endpoint+'/events',json=pload);
            contexto={
                'textoEntrada': name
            }
            RecibirTexto()
        else:
            print('F')
    return render(request, 'signup.html', contexto)


def abrirXML(request):
    if request.method == 'GET':
        form = LeerForm(request.GET)
       
        if form.is_valid():
            ruta = form.cleaned_data['myFile']
            sendingJson={
                'rutaArchivo':ruta
            }
            envio = requests.post(endpoint+'rutaArchivo', json=sendingJson)   
            prueba = envio.json() 
            global textoEntrada, auxiliarentrada
            if prueba['data']=='True' or name!="":
                response = requests.get(endpoint+'imprimirEntrada')
                entradaEstatica=response.json()
                auxiliarentrada=entradaEstatica['entrada']
                textoEntrada={
                    'entradaEstatica':entradaEstatica['entrada']
                }
            return render(request,'signup.html',textoEntrada)
        else:
            return render(request,'signup.html',name)


   
def upload(request):
    contexto ={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        #ds = uploaded_file
        #concatenar=""
       # with open('name.txt', 'wb+') as destination:
        #    for chunk in ds.chunks():
         #       concatenar = concatenar + str(chunk)
          #      destination.write(chunk) 
    
        data = open('C:/Users/che/Desktop/IPC2_Proyecto3_201344708/'+uploaded_file.name, 'r+', encoding='utf-8')
        hola = data.read()
        contexto= {
            'textoEntrada': hola
        }
   
    return render(request, 'signup.html', contexto)