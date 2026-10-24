from flask import Flask, jsonify, request, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config

maestros_bp=Blueprint('maestros',__name__,url_prefix='/api/maestros')

def fila_a_diccionario(cursor,fila):
    columnas=(columna[0] for columna in cursor.descrip)
    return dict(zip(columnas,fila))

@maestros_bp_route("/maestros",methods=['GET'])
def listar_maestros():
    cursor=None
