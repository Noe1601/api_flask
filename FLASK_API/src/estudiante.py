from typing import Counter
from flask import Flask,jsonify, request, make_response
from flask_mysqldb import MySQL
from config import database

app = Flask(__name__)

conexion = database

#REGISTRO DE ESTUDIANTES
def CrearEstudiante():
        try:
            req = request.get_json()

            cursor = conexion.cursor()
            sql = """INSERT INTO ESTUDIANTE(NOMBRE,ID_ASIGNATURA) 
                VALUES('{0}','{1}')""".format(
                request.json['nombre'],
                request.json['asignatura'])

            cursor.execute(sql)
            conexion.commit()

            response_body = {
            "ok": "true",
            "message": "Estudiante registrado exitosamente!",
            "Estudiante": req.get("nombre")
             }
             
            res = make_response(jsonify(response_body), 200)
            return res
        except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#Obtener Estudiantes
def ObtenerEstudiantes():
    try:
        global counter
        cursor = conexion.cursor()
        sql = "SELECT * FROM ESTUDIANTE"
        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryEstudiantes = {}
        _dictionary = {}
        counter = 0
        for i in datos:
            _dictionary = dict(ID=i[0], NOMBRE=i[1], ASIGNATURA=i[2])
            dictionaryEstudiantes.update({f"Estudiantes{counter}": _dictionary})
            counter += 1

        return dict(Estudiantes = dictionaryEstudiantes)

    except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#         for k in result:
#             _dictionary = dict(ID=k[0],CATEGORIA=k[1],TIPO=k[2],COMPAÑIA=k[3],URL=k[4],POSICION=k[5],UBICACION=k[6],DESCRIPCION=k[7],EMAIL=k[8])
#             dictionary.update({f"Puestos{counter}": _dictionary})
#             counter+=1
#         return dict(PuestosTrabajo=dictionary)


#ELIMINAR ESTUDIANTES
def EliminarEstudiante(codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM ESTUDIANTE WHERE ID = '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.commit()

        return jsonify({"ok": "true", "mensaje": "Estudiante eliminado exitosamente!"})
    except:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR ASIGNATURA
def ActualizarEstudiante(codigo):
    try:
        cursor = conexion.cursor()
        sql = """UPDATE ESTUDIANTE SET NOMBRE = '{0}'
                WHERE ID = '{1}'""".format(request.json['nombre'],codigo)
        cursor.execute(sql)
        conexion.commit()

        return jsonify({"ok": "true", "mensaje": "Estudiante actualizado exitosamente!"})
    except:
        return jsonify({'mensaje': 'Error'})


#OBTENER ESTUDIANTE POR ID
def ObtenerEstudiantePorID(codigo):
    try:
        cursor = conexion.cursor()
        sql = """SELECT * FROM ESTUDIANTE WHERE ID = '{0}'""".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryProfesor = {}
        _dictionary = {}
        for i in datos:
            _dictionary = dict(ID=i[0], NOMBRE=i[1], ASIGNATURA=i[2])
            dictionaryProfesor.update({f"Estudiante": _dictionary})

        return dict(Estudiante = _dictionary)
    except:
        return jsonify({"mensaje": "Error"})

if __name__ == '__main__':
    app.run()

# cursor = database.cursor()
