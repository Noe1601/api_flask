from flask import Flask,jsonify, request, make_response
from flask_mysqldb import MySQL
# from config import config
import usuarios as modelo
from config import database

app = Flask(__name__)

conexion = database

#REGISTRO DE PROFESORES
def CrearProfesores():
        try:
            req = request.get_json()

            cursor = conexion.cursor()
            sql = """INSERT INTO PROFESOR(NOMBRE,EDAD) 
                VALUES('{0}','{1}')""".format(
                request.json['nombre'],
                request.json['edad'])

            cursor.execute(sql)
            conexion.commit()

            response_body = {
            "ok": "true",
            "message": "Profesor registrado exitosamente!",
            "Profesor": req.get("nombre")
             }
             
            res = make_response(jsonify(response_body), 200)
            return res
        except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#Obtener profesores
def ObtenerProfesores():
    try:
        global counter
        cursor = conexion.cursor()
        sql = "SELECT * FROM PROFESOR"
        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryProfesores = {}
        _dictionary = {}
        counter = 0
        for i in datos:
            _dictionary = dict(ID=i[0], NOMBRE=i[1], EDAD=i[2])
            dictionaryProfesores.update({f"Profesores{counter}": _dictionary})
            counter += 1

        return dict(Profesores = dictionaryProfesores)
        
    except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#ELIMINAR PROFESOR
def EliminarProfesor(codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM PROFESOR WHERE ID = '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.commit()

        return jsonify({"ok": "true", "mensaje": "Profesor eliminado exitosamente!"})
    except:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR PROFESOR
def ActualizarProfesor(codigo):
    try:
        cursor = conexion.cursor()
        sql = """UPDATE PROFESOR SET NOMBRE = '{0}', EDAD = '{1}' 
                WHERE ID = '{2}'""".format(request.json['nombre'],
                request.json['edad'],codigo)
        cursor.execute(sql)
        conexion.commit()

        return jsonify({"ok": "true", "mensaje": "Profesor actualizado exitosamente!"})
    except:
        return jsonify({'mensaje': 'Error'})


#OBTENER PROFESOR POR ID
def ObtenerProfesorPorID(codigo):
    try:
        cursor = conexion.cursor()
        sql = """SELECT * FROM PROFESOR WHERE ID = '{0}'""".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryProfesor = {}
        _dictionary = {}
        for i in datos:
            _dictionary = dict(ID=i[0], NOMBRE=i[1], EDAD=i[2])
            dictionaryProfesor.update({f"Profesor": _dictionary})

        return dict(Profesor = _dictionary)
    except:
        return jsonify({"mensaje": "Error"})



if __name__ == '__main__':
    app.run()

# cursor = database.cursor()
