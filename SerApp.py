from flask import Flask, render_template, request
import platform
import os
import sys
import getpass
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    ipadd = request.remote_addr
    sistema = platform.system()
    version = sys.version
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    usuario = getpass.getuser()   
    ruta = os.getcwd()

    return render_template(
        'index2.html',
        ip=ipadd,
        sistema=sistema,
        version=version,
        fecha_hora=fecha_hora,
        usuario=usuario,
        ruta=ruta
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
