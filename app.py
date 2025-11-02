from flask import Flask, render_template

app = Flask(__name__)

# El decorador vincula esta función a la ruta URL "/" (la página principal)
@app.route('/')
def index():
   return render_template('index.html')

# Nueva ruta para la página "Sobre Mí"
@app.route('/about')
def about():
    return render_template('about.html')  


# Nueva ruta para la página "Contacto"
@app.route('/contact')
def contact():
    return render_template('contact.html') 

# Permite ejecutar el servidor directamente como un script de Python
if __name__ == '__main__':
    app.run(debug=True)

  