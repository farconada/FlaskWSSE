__author__ = 'fernando'
from functools import wraps
from flask import request, abort
from lib.wsse.util import validate_header, WsseError

def wsse_required(user, password, lifetime=300):
    def wrapper(func):
        """Requires standard X-WSSE credentials"""
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not request.headers.get('X-WSSE'):
                abort(403)
            else:
                wsse_header = request.headers.get('X-WSSE')
                try:
                    validate_header(wsse_header, user, password, lifetime)
                except WsseError as err:
                    print err
                    abort(403)

            return func(*args, **kwargs)
        return decorated_view
    return wrapper