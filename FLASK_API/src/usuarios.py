from flask import Flask,jsonify, request, make_response
from flask_mysqldb import MySQL
from config import database
import hashlib

app = Flask(__name__)

conexion = database

#REGISTRO DE USUARIOS
def CrearUsuarios():
        try:
            req = request.get_json()

            cursor = conexion.cursor()
            sql = """INSERT INTO USUARIOS(CORREO,PWD,NOMBRE,ROL) 
                VALUES('{0}','{1}','{2}','{3}')""".format(request.json['correo'],
                request.json['password'],
                request.json['nombre'],
                request.json['rol'])

            cursor.execute(sql)
            conexion.commit()

            response_body = {
            "ok": "true",
            "message": "Usuario registrado exitosamente!",
            "Usuario": req.get("nombre")
             }
             
            res = make_response(jsonify(response_body), 200)
            return res
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': 'Error'})


#LOGIN
def Login():

    try:
        req = request.get_json()

        cursor = conexion.cursor()
        sql = """SELECT * FROM USUARIOS WHERE CORREO = '{0}' AND PWD = '{1}' """.format(request.json['correo'],
            request.json['password'])

        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryUsuario = {}
        _dictionary = {}
        for i in datos:
            _dictionary = dict(ID=i[0], CORREO=i[1], PASSWORD=i[2], NOMBRE=i[3], ROL=i[4])
            dictionaryUsuario.update({f"Usuario": _dictionary})

        if _dictionary:          
            return dict(Usuario = _dictionary)
        else:
            _errorDictionary = dict(ERROR='Fallo')
            return dict(ERROR = _errorDictionary)
        
    except Exception as ex:
            print(ex)
            return jsonify({'mensaje': 'Error'})




if __name__ == '__main__':
    app.run()

# cursor = database.cursor()
