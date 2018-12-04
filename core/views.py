from django.shortcuts import render, redirect, render_to_response, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect,HttpResponseRedirect
from .models import Comunidad, TipoPersona, TipoEvento, Persona, Evento
from django.contrib import messages
from django.urls import reverse

# Create your views here.
tipos_persona = TipoPersona.objects.all()

def Home(request):
    return render(request, 'core/home.html')

def ListadoPersonas(request):
    personas = Persona.objects.all()
    return render(request, 'core/listado_personas.html', {'personas':personas})

def ListadoEventos(request):
    eventos = Evento.objects.all()
    return render(request, 'core/listado_eventos.html', {'eventos':eventos})    

def ListadoPersonasFiltroTipoPersona(request, tipo_persona):
    personas = Persona.objects.filter(tipo_persona__pk=tipo_persona)
    return render(request, 'core/listado_personas_filtro_tipo_persona.html', {'personas':personas})
    
def ListadoEventosFiltroTipoEvento(request, tipo_evento):
    eventos = Evento.objects.filter(tipo_evento__pk=tipo_evento)
    return render(request, 'core/lista_eventos_filtro_tipo.html', {'eventos':eventos})
   

def Eliminar_Personas(request, id):
    #buscar la persona
    persona = Persona.objects.get(id=id)

    try:
        persona.delete()
        mensaje = "Fiel eliminado :("
        messages.success(request, mensaje)
    except:
        mensaje = "Fiel No eliminado, suerte para la próxima Dios ;)"
        messages.error(request, mensaje)
    return redirect('listado_personas')

def IngresoPersonas(request):
    tipos_persona = TipoPersona.objects.all()
    tipos_evento = TipoEvento.objects.all()
    comunidades = Comunidad.objects.all()

    variables = {
        'tipos_persona':tipos_persona,
        'tipos_evento':tipos_evento,
        'comunidades':comunidades
    }

    if request.POST:
        persona = Persona()

        persona.apellido = request.POST.get('txtApellido')
        persona.nombre = request.POST.get('txtNombre')
        persona.edad = request.POST.get('txtEdad')
        persona.sexo = request.POST.get('rbSexo')
        persona.telefono = request.POST.get('txtTelefono')
        persona.direccion = request.POST.get('txtDireccion')
        tipo_persona = TipoPersona()
        tipo_evento = TipoEvento()
        comunidad = Comunidad()
        tipo_persona.id = request.POST.get('cboCargo')
        tipo_evento.id = request.POST.get('cboEventos')
        comunidad.id = request.POST.get('cboComunidad')

        persona.tipo_persona = tipo_persona
        persona.tipo_evento = tipo_evento
        persona.comunidad = comunidad
        
        try:
            persona.save()
            variables['mensaje'] = "Fiel Agregado"
        except:
            variables['mensaje'] = "Fiel No Agregado :(, Satán estaría orgulloso de ti"
        
        
    return render (request, 'core/ingreso_personas.html',variables)
    
def ModificacionPersonas(request, id):
    persona = Persona.objects.get(id=id)
    tipos_persona = TipoPersona.objects.all()
    tipos_evento = TipoEvento.objects.all()
    comunidades = Comunidad.objects.all()

    if request.POST:
        persona = Persona()
        persona.id = request.POST.get('txtId')
        persona.apellido = request.POST.get('txtApellido')
        persona.nombre = request.POST.get('txtNombre')
        persona.edad = request.POST.get('txtEdad')
        persona.sexo = request.POST.get('rbSexo')
        persona.telefono = request.POST.get('txtTelefono')
        persona.direccion = request.POST.get('txtDireccion')
        tipo_persona = TipoPersona()
        tipo_evento = TipoEvento()
        comunidad = Comunidad()
        tipo_persona.id = request.POST.get('cboCargo')
        tipo_evento.id = request.POST.get('cboEventos')
        comunidad.id = request.POST.get('cboComunidad')

        persona.tipo_persona = tipo_persona
        persona.tipo_evento = tipo_evento
        persona.comunidad = comunidad
        
        try:
            persona.save()
            messages.success(request, "Fiel Modificado")
        except:
            messages.error(request, "Fiel no ha podido modificarse")
        return redirect('listado_personas')
    variables = {
        'persona': persona,
        'tipos_persona':tipos_persona,
        'tipos_evento':tipos_evento,
        'comunidades':comunidades
    }

    return render(request, 'core/modificar_persona.html', variables)