from flask import Flask
from flask.ext.restful import Api
from lxcapi.lxcapi.users import User, Users

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['DATABASE'] = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
}

# remote api
api = Api(app, prefix='/v1', catch_all_404s=True)
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
