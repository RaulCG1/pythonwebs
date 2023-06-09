"""
import requests
url="https://api.catboys.com/baka"
from io import BytesIO
from PIL import Image
respuesta = requests.get(url=url)


resultado = respuesta.json()
url_img = str(resultado["url"])
url_img = "https://cdn.catboys.com/baka/baka_5.gif"
response = requests.get(url_img)
imagen = Image.open(BytesIO(response.content))
imagen.show()
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/inicio")
def inicio():
    return render_template('inicio.html',variable= {"key":10})


if __name__ == "__main__":
    app.run(debug=True)