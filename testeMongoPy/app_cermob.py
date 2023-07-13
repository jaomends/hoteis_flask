from flask import Flask
from flask_restful import Api
from resource_design.design_resource import Design, Design_Diploma
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api = Api(app)
jwt = JWTManager(app)


@app.before_request
def cria_banco():
    banco.create_all()


api.add_resource(Design_Diploma, '/design')
api.add_resource(Design, '/design/<string:id_design_diploma>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
