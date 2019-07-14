from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps


app = Flask(__name__)
app.config['SEC_KEY'] = 'thesecretkey'


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SEC_KEY'])
        except:
            return jsonify({'message': 'Token invalid!'}), 403
        return func(*args, **kwargs)
    return wrapper


@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Unprotected view'})


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'Protected View'})


@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'passw':
        token = jwt.encode({'user': auth.username,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15)},
                           app.config['SEC_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Couldn\'t verify', 401, {'WWW-Authenticate': 'Basic realm = "Login Required'})


if __name__ == '__main__':
    app.run(debug=True)
