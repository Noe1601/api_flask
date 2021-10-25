from flask import Flask,jsonify, request, make_response
from flask_mysqldb import MySQL
# from config import config
import usuarios as modelo
from config import database

app = Flask(__name__)

conexion = database

#REGISTRO DE ASIGNATURAS
def CrearAsignatura():
        try:
            req = request.get_json()

            cursor = conexion.cursor()
            sql = """INSERT INTO ASIGNATURA(NOMBRE,ID_PROFESOR) 
                VALUES('{0}','{1}')""".format(
                request.json['nombre'],
                request.json['profesor'])

            cursor.execute(sql)
            conexion.commit()

            response_body = {
            "ok": "true",
            "message": "Asignatura registrada exitosamente!",
            "Asignatura": req.get("nombre")
             }
             
            res = make_response(jsonify(response_body), 200)
            return res
        except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#Obtener ASIGNATURAS
def ObtenerAsignatura():
    try:
        global counter
        cursor = conexion.cursor()
        sql = """SELECT A.ID AS '# ASIGNATURA', A.NOMBRE AS 'NOMBRE ASIGNATURA', P.NOMBRE 'NOMBRE PROFESOR'
                 FROM ASIGNATURA A 
                 JOIN PROFESOR P ON (A.ID_PROFESOR = P.ID)"""
        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryAsignatura = {}
        _dictionary = {}
        counter = 0
        for i in datos:
            _dictionary = dict(ID=i[0], NOMBRE=i[1], PROFESOR=i[2])
            dictionaryAsignatura.update({f"Asignatura{counter}": _dictionary})
            counter += 1

        return dict(Asignatura = dictionaryAsignatura)

    except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#ELIMINAR ASIGNATURA
def EliminarAsignatura(codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM ASIGNATURA WHERE ID = '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.commit()

        return jsonify({"ok": "true", "mensaje": "Asignatura eliminada exitosamente!"})
    except:
        return jsonify({'mensaje': 'Error'})


#ACTUALIZAR ASIGNATURA
def ActualizarAsignatura(codigo):
    try:
        cursor = conexion.cursor()
        sql = """UPDATE ASIGNATURA SET NOMBRE = '{0}', ID_PROFESOR = '{1}' 
                WHERE ID = '{2}'""".format(request.json['nombre'],
                request.json['profesor'],codigo)
        cursor.execute(sql)
        conexion.commit()

        return jsonify({"ok": "true", "mensaje": "Asignatura actualizada exitosamente!"})
    except:
        return jsonify({'mensaje': 'Error'})


#OBTENER ASIGNATURA, ESTUDIANTE Y PROFESOR
def Relaciones(codigoAsignatura):
    global counter
    cursor = conexion.cursor()
    sql = """SELECT e.ID AS 'Estudiante ID',e.NOMBRE AS 'Estudiante', a.NOMBRE AS 'Nombre ASIGNATURA'
             FROM ESTUDIANTE e
             JOIN ASIGNATURA a ON (E.ID_ASIGNATURA = '{0}')
             WHERE a.ID = e.ID_ASIGNATURA""".format(codigoAsignatura)
    cursor.execute(sql)
    datos = cursor.fetchall()
    dictionaryRelacion = {}
    _dictionary = {}
    counter = 0
    for i in datos:
        _dictionary = dict(ID_ESTUDIANTE=i[0], NOMBRE_ESTUDIANTE=i[1], ASIGNATURA=i[2])
        dictionaryRelacion.update({f"Relacion{counter}": _dictionary})
        counter += 1

    return dict(Asignatura = dictionaryRelacion)
    

#OBTENER PROFESOR POR ID
def obtenerAsignaturaPorID(codigo):
    try:
        cursor = conexion.cursor()
        sql = """SELECT * FROM ASIGNATURA WHERE ID = '{0}'""".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchall()
        dictionaryAsignatura = {}
        _dictionary = {}
        for i in datos:
            _dictionary = dict(ID=i[0], NOMBRE=i[1], PROFESOR=i[2])
            dictionaryAsignatura.update({f"Asignatura": _dictionary})

        return dict(Asignatura = _dictionary)
    except:
        return jsonify({"mensaje": "Error"})


if __name__ == '__main__':
    app.run()

# cursor = database.cursor()
