from flask import Flask
from flask_restful import Api
from resources.design import Design, Design_get
from resources.list_design import ListDesign, ListDesign_get
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000', 'http://localhost:5000'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api = Api(app)
jwt = JWTManager(app)

@app.before_request
def cria_banco():
    banco.create_all()

api.add_resource(Design_get, '/design')
api.add_resource(Design, '/design/<string:id_design_diploma>')
api.add_resource(ListDesign_get, '/design/files')
api.add_resource(ListDesign, '/design/files/<string:id_design_diploma>')
# api.add_resource(User, '/usuarios/<int:user_id>' )
# api.add_resource(UserRegister, '/cadastro')
# api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)