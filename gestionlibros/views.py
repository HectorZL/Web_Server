from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.
def saludo(request): # primera vista
    documento="""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Página en Construcción</title>
<style>
/* Estilos CSS en línea */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

.container {
    text-align: center;
    margin-top: 100px;
}

.heading {
    font-size: 36px;
    color: #333;
}

.subheading {
    font-size: 24px;
    color: #666;
}
</style>
</head>
<body>

<div class="container">
    <h1 class="heading">Página en Construcción</h1>
    <p class="subheading">Estamos trabajando en ello. ¡Vuelve pronto!</p>
</div>

</body>
</html>"""

    return HttpResponse(documento)