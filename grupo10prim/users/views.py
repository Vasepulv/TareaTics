from django.shortcuts import render


# Create your views here.
def registrar_usuario(request):
    return render(request, 'registrar_usuario.html')


def client_profile(request):
    return render(request, 'client_profile.html')


def login(request):
    return render(request, 'login.html')




def recuperar_registro(request):
    name = request.POST["input_name"]
    last_name = request.POST["input_last_name"]
    rut = request.POST["input_rut"]
    email = request.POST["input_mail"]
    diccionario = {"nombre": name, "apellido": last_name, "rut": rut, "email": email}
    return render(request, 'mostrar_resultado.html', diccionario)


def add_pet(request):
    return render(request, 'add_pet.html')
