from pathlib import Path
from flask import Flask, render_template
import markdown

app = Flask(__name__)
STATIC = Path(app.static_folder)


def leer_md(nombre):
    ruta = STATIC / nombre
    if not ruta.exists():
        return "<p>Contenido no disponible.</p>"
    return markdown.markdown(
        ruta.read_text(encoding="utf-8"),
        extensions=["extra", "nl2br"],
    )


@app.route("/")
def inicio():
    return render_template("inicio.html", pagina="inicio")


@app.route("/anuncios/")
def anuncios():
    return render_template("anuncios.html", pagina="anuncios", contenido=leer_md("anuncios.md"))


@app.route("/ip/")
def ip():
    return render_template("ip.html", pagina="ip", contenido=leer_md("ip.md"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)