from django.shortcuts import render


def contactenos(request):

    informacion = {
        "titulo": "Contactenos",
        "msj": "Gracias por visitarnos, aquí están nuestros datos por si quieres contactarnos.",
        "email": "admin@admin.com",
        "telefono": "12341234",
        "disponibilidad": True,
    }
    
    return render(request, "contactenos.html", informacion)
