__author__ = 'fernando'
import re
from datetime import datetime
import pytz
import base64
import hashlib

class WsseError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class WsseUnsupportedError(WsseError):
    pass

class ExpiredTokenError(WsseError):
    pass

class AuthenticationFailedError(WsseError):
    pass

def validate_header(wsse_header, user, password, lifetime=3000):
    if re.match(r'^UsernameToken ', wsse_header):
        wsse_header = wsse_header.replace('UsernameToken ', '')
        wsse = dict()
        for val in wsse_header.split(','):
            key = val.split('=')[0].strip()
            wsse[key] = val.split('=', 1)[1].strip('"')
        wsse['Created'] = datetime.strptime(wsse['Created'],'%Y-%m-%dT%H:%M:%SZ')

        if (datetime.utcnow() - wsse['Created']).seconds > lifetime:
            raise ExpiredTokenError('Token has expired')

        seed = base64.decodestring(wsse['Nonce']) + wsse['Created'].isoformat()+'Z' + password
        hasher = hashlib.sha1()
        hasher.update(seed)
        expectedDigest = base64.encodestring(hasher.digest())[:-1] #al final hay que quitar el salto de linea

        if (user != wsse['Username']) or (expectedDigest != wsse['PasswordDigest']):
            raise AuthenticationFailedError('Authentication failed')

        return True
    else:
        raise WsseUnsupportedError('Unsupported Token')