from logging import log
from flask import Flask
import usuarios as modeloUsuarios
import profesor as modeloProfesores
import asignatura as modeloAsignatura
import estudiante as modeloEstudiante
from flask_cors import CORS

from config import database

app = Flask(__name__)
CORS(app, supports_credentials=True)

#Usuarios 
@app.route('/usuarios', methods=['POST'])
def registroUsuarios():
    usuario = modeloUsuarios.CrearUsuarios()
    return usuario

@app.route('/login', methods=['POST'])
def Login():
    login = modeloUsuarios.Login();
    return login


#Profesores
@app.route('/profesores', methods=['POST'])
def registroProfesores():
    profesorRegister = modeloProfesores.CrearProfesores()
    return profesorRegister

@app.route('/profesores', methods=['GET'])
def obtenerProfesores():
    profesoresList = modeloProfesores.ObtenerProfesores()
    return profesoresList

@app.route('/profesores/<codigo>', methods=['GET'])
def obtenerProfesor(codigo):
    profesorList = modeloProfesores.ObtenerProfesorPorID(codigo)
    return profesorList

@app.route('/profesores/<codigo>', methods=['DELETE'])
def eliminarProfesores(codigo):
    profesorDelete = modeloProfesores.EliminarProfesor(codigo)
    return profesorDelete

@app.route('/profesores/<codigo>', methods=['PUT'])
def actualizarProfesores(codigo):
    profesorUpdate = modeloProfesores.ActualizarProfesor(codigo)
    return profesorUpdate


#Asignaturas
@app.route('/asignatura', methods=['POST'])
def registroAsignaturas():
    asignaturaRegister = modeloAsignatura.CrearAsignatura()
    return asignaturaRegister

@app.route('/asignatura', methods=['GET'])
def obtenerAsignaturas():
    asignaturasList = modeloAsignatura.ObtenerAsignatura()
    return asignaturasList

@app.route('/asignatura/<codigo>', methods=['GET'])
def obtenerAsignaturaPorID(codigo):
    asignaturaList = modeloAsignatura.obtenerAsignaturaPorID(codigo)
    return asignaturaList

@app.route('/relacionAsignaturas/<codigoAsignatura>', methods=['GET'])
def relacionesAsignaturas(codigoAsignatura):
    listadoRelaciones = modeloAsignatura.Relaciones(codigoAsignatura)
    return listadoRelaciones

@app.route('/asignatura/<codigo>', methods=['DELETE'])
def eliminarAsignaturas(codigo):
    asignaturaDelete =modeloAsignatura.EliminarAsignatura(codigo)
    return asignaturaDelete

@app.route('/asignatura/<codigo>', methods=['PUT'])
def actualizarAsignaturas(codigo):
    asignaturasUpdate = modeloAsignatura.ActualizarAsignatura(codigo)
    return asignaturasUpdate


#Estudiantes
@app.route('/estudiante', methods=['POST'])
def registroEstudiante():
    registroRegister = modeloEstudiante.CrearEstudiante()
    return registroRegister

@app.route('/estudiante', methods=['GET'])
def obtenerEstudiantes():
    estudiantesList = modeloEstudiante.ObtenerEstudiantes()
    return estudiantesList

@app.route('/estudiante/<codigo>', methods=['GET'])
def obtenerEstudiante(codigo):
    estudianteList = modeloEstudiante.ObtenerEstudiantePorID(codigo)
    return estudianteList

@app.route('/estudiante/<codigo>', methods=['DELETE'])
def eliminarEstudiante(codigo):
    estudianteDelete = modeloEstudiante.EliminarEstudiante(codigo)
    return estudianteDelete

@app.route('/estudiante/<codigo>', methods=['PUT'])
def actualizarEstudiante(codigo):
    estudianteUpdate = modeloEstudiante.ActualizarEstudiante(codigo)
    return estudianteUpdate

if __name__ == '__main__':
    app.run()
