from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")


usuario_registrado = False

@app.route('/')
def index():
    global usuario_registrado
  
    if not usuario_registrado:
        return redirect(url_for('registro'))
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    global usuario_registrado
    if request.method == 'POST':
    
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')

        if nombre and apellido and email and password:
            usuario_registrado = True  
            return redirect(url_for('index'))  
        else:
            return render_template('registro.html', error="Completa todos los campos.")

    return render_template('registro.html')


@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


if __name__ == '__main__':
    app.run(debug=True)
