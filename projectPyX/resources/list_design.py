from flask_restful import Resource, reqparse
from models.design import DesignModel
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

class ListDesign_get(Resource):
    def get(self):
        return {'files_design': [design.json_list_design() for design in DesignModel.query.all()]}


class ListDesign(Resource):
    # /usuario/{user_id}

    atributos = reqparse.RequestParser()
    atributos.add_argument('files_design')

    def get(self, id_design_diploma):
        try:
            files_design = DesignModel.find_design(id_design_diploma)
            if files_design:
                return files_design.json_list_design()
            return {'message': 'Design not found.'}, 404 # not found
        except:
            return {'message': 'System problem.'}, 500 # internal server error
    
    def delete(self, id_design_diploma):
        files_design = DesignModel.find_design(id_design_diploma)
        if files_design:
            try:
                files_design.delete_user()
            except:
                return{'message': 'An internal error ocurred trying to save user.'}, 500 # internal Server Error   
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404
'''   
class UserRegister(Resource):
    # /cadastro
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return{"message": "The login '{}' already exists.".format(dados['login'])}
        
        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully !'}, 201 # CREATED
'''   
        
'''
class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])

        if user and check_password_hash(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return{'acess_token': token_de_acesso}, 200
        return {'message': 'The username or password is incorrect.'}, 401 # Unauthorized
'''