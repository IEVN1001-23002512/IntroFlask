from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp

def registrar_blueprints(app):
    app.registar_blueprints(alumnos_bp)
    app.registar_blueprints(maestros_bp)