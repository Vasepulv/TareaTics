from django.shortcuts import render


# Create your views here.
def homeCliente(request):
    return render(request, 'homeCliente.html')


def inputs(request):
    return render(request, 'inputs.html')


def contacto(request):
    return render(request, 'contacto.html')


def agenda(request):
    return render(request, 'agenda.html')


def catalogo(request):
    return render(request, 'catalogo.html')


def backoffice(request):
    return render(request, 'backoffice.html')


def homeEmpresa(request):
    return render(request, 'homeEmpresa.html')


def fichaClinica(request):
    return render(request, 'fichaClinica.html')


def estadisticas(request):
    return render(request, 'estadisticas.html')


def inventario(request):
    return render(request, 'inventario.html')


def comprarObjeto(request):
    return render(request, 'comprarObjeto.html')


def agendaReg(request):
    return render(request, 'agendaReg.html')


def agregarElemento(request):
    return render(request, 'agregarElemento.html')


def envioInventario(request):
    return render(request, 'envioInventario.html')


def contacto_exitoso(request):
    return render(request, 'contacto_exitoso.html')


def recuperar(request):
    diccionario = {}

    name1 = request.POST.get("inputComida1")
    if (name1):
        diccionario["Bebestible"] = "Bebestible"

    name2 = request.POST.get("inputComida2")
    if (name2):
        diccionario["Snack"] = "Snack"

    name3 = request.POST.get("inputComida3")
    if (name3):
        diccionario["Cena"] = "Cena"

    #  nombre=request.POST["inputNombre"]
    #	edad=request.POST["inputEdad"]
    #	email=request.POST["inputEmail"]
    #	carrera=request.POST["exampleRadios"]
    #	tema=request.POST["inputTema"]
    #
    #	diccionario["Nombre"]=nombre
    #	diccionario["Edad"]=edad
    #	diccionario["Email"]=email
    #	diccionario["Departamento"]=carrera
    #	diccionario["Tematica"]=tema

    return render(request, "mostrar_resultado.html", diccionario)


def resumen(request):
    diccionario = {}

    name4 = request.POST.get("inputEstado1")
    if (name4):
        diccionario["Vacunado"] = "Posee vacunas al día"

    name5 = request.POST.get("inputEstado2")
    if (name5):
        diccionario["Desparacitado"] = "Desparacitado"

    name6 = request.POST.get("inputEstado3")
    if (name6):
        diccionario["nuevasVacunas"] = "Requiere vacunas"

    name7 = request.POST.get("inputEstado4")
    if (name7):
        diccionario["Medicamento"] = "Requiere medicamento para desparacitación"

    amo = request.POST["inputNombreAmo"]
    rut = request.POST["inputRut"]
    edadAmo = request.POST["inputEdadAmo"]
    email = request.POST["inputEmailAmo"]
    mascota = request.POST["inputNombreMascota"]
    especie = request.POST["exampleRadiosEspecie"]
    edadMascota = request.POST["inputEdadMascota"]
    genero = request.POST["inputGenero"]
    diagnostico = request.POST["textA"]
    agendarH = request.POST["exampleRadiosCita"]
    area = request.POST["input Select"]
    medico = request.POST["inputMedico"]
    fecha = request.POST["inputDate"]
    hora = request.POST["appt"]

    diccionario["Amo"] = amo
    diccionario["Rut"] = rut
    diccionario["EdadAmo"] = edadAmo
    diccionario["Email"] = email
    diccionario["Mascota"] = mascota
    diccionario["Especie"] = especie
    diccionario["EdadMascota"] = edadMascota
    diccionario["Genero"] = genero
    diccionario["Diagnostico"] = diagnostico
    diccionario["AgendarH"] = agendarH
    diccionario["Area"] = area
    diccionario["Medico"] = medico
    diccionario["Fecha"] = fecha
    diccionario["Hora"] = hora

    return render(request, "resumen_fichaClinica.html", diccionario)
