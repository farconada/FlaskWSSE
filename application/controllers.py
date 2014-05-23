__author__ = 'fernando'


from flask import Response, json
from models import Actividad, ActividadSerializer
from decorators import wsse_required

@wsse_required(user='admin', lifetime=3000, password='pass')
def main():
    return Response('algo')

def ultima_actividad(coto_id):
    actividad = Actividad.query.filter_by(coto_id=coto_id).all()
    serialized = ActividadSerializer(actividad, many=True).data
    return Response(json.dumps(serialized),  mimetype='application/json')
