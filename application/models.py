__author__ = 'fernando'
import flask.ext.sqlalchemy
from marshmallow import Serializer, fields


db = flask.ext.sqlalchemy.SQLAlchemy()

"""
    Listado de provincias
"""
class Provincia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)


"""
    Cotos de las provincias
"""
class Coto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincia.id'))
    provincia = db.relationship('Provincia', backref=db.backref('cotos', lazy='dynamic'))

"""
    Calibres y elementos para caza, por ejempl 22mm o arco
"""
class Calibre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)


"""
    Actividad en el coto
"""
class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    foto = db.Column(db.LargeBinary)
    comentario = db.Column(db.Text)
    coto_id = db.Column(db.Integer, db.ForeignKey('coto.id'), nullable=False)
    coto = db.relationship('Coto', backref=db.backref('actividad', lazy='dynamic'))
    calibre_id = db.Column(db.Integer, db.ForeignKey('calibre.id'), nullable=False)
    calibre = db.relationship('Calibre')

class ActividadSerializer(Serializer):
    id = fields.Integer()
    fecha = fields.DateTime()
    foto = fields.String()
    comentario = fields.String()
    coto_id = fields.Integer()
    calibre_id = fields.Integer()