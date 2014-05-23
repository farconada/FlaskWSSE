__author__ = 'fernando'
from application import app, API_PREFIX
from application import controllers

app.add_url_rule('/', 'index', view_func=controllers.main)
app.add_url_rule(API_PREFIX + '/coto/<int:coto_id>/ultimaactividad', 'ultimaactividad', view_func=controllers.ultima_actividad)
