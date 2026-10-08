# OlympusMC Web

Sitio web del servidor de Minecraft OlympusMC, desarrollado con Flask. El contenido de las páginas de anuncios e IP se escribe en archivos Markdown, por lo que se puede actualizar sin tocar el código.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
git clone https://github.com/OlympusMCPlay/www.git
cd <carpeta-del-repositorio>
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

La aplicación se inicia en el puerto `5000`.

### GitHub Codespaces

Al ejecutar la aplicación, Codespaces detecta el puerto 5000 y muestra un aviso para abrirlo en el navegador. También se puede acceder desde la pestaña **Puertos**.

## Estructura del proyecto

```
.
├── app.py                 # Aplicación Flask y rutas
├── requirements.txt       # Dependencias
├── templates/
│   ├── base.html          # Plantilla base (cabecera, navegación y pie)
│   ├── inicio.html        # Página de inicio
│   ├── anuncios.html      # Página de anuncios
│   └── ip.html            # Página de conexión
└── static/
    ├── style.css          # Estilos
    ├── anuncios.md        # Contenido de la página de anuncios
    └── ip.md              # Contenido de la página de IP
```

## Edición de contenido

Los textos de las páginas de anuncios e IP se editan directamente en Markdown:

| Página | Archivo |
|---|---|
| Anuncios | `static/anuncios.md` |
| IP | `static/ip.md` |

Los cambios se reflejan al recargar la página. No es necesario reiniciar el servidor.

## Añadir una página nueva

1. Crear la plantilla en `templates/`, por ejemplo `normas.html`:

```html
   {% extends "base.html" %}
   {% block titulo %}Normas{% endblock %}

   {% block contenido %}
   <h1>Normas</h1>
   <div class="markdown">
       {{ contenido | safe }}
   </div>
   {% endblock %}
```

2. Crear el contenido en `static/normas.md`.

3. Añadir la ruta en `app.py`:

```python
   @app.route("/normas")
   def normas():
       return render_template("normas.html", pagina="normas", contenido=leer_md("normas.md"))
```

4. Añadir el enlace en la navegación de `templates/base.html`:

```html
   <a href="{{ url_for('normas') }}" class="{{ 'activo' if pagina == 'normas' }}">Normas</a>
```

## Dependencias

- [Flask](https://flask.palletsprojects.com/)
- [Markdown](https://python-markdown.github.io/)

## Aviso legal

Proyecto de comunidad independiente. No está afiliado, asociado ni respaldado por Mojang Studios ni Microsoft. Minecraft es una marca registrada de Mojang Studios.

Hecho por Mel Roses (LDev y Co-Owner de OlympusMC, [GitHub](https://github.com/Mel-Roses)