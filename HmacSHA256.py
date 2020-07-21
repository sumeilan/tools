import base64
import hmac, json
import hashlib


def sh258(co):
    secretKey = 'SwYNTwt5qPABx29Atyi0'
    Authorization = base64.b64encode(
        hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    return Authorization.decode('utf-8')

def sh258_v2(co):
    secretKey = 'SwYNun73nlo82443Twt5qPABx29Atyi0'
    AuthorizationV2 = base64.b64encode(
        hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    return AuthorizationV2.decode('utf-8')


if __name__ == '__main__':
    body = {'page': '1', 'pageSize': '20', 'app_key': 'lemondream'}
    A = sh258(json.dumps(body))
    print(A)
