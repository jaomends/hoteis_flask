from flask_restful import Resource, reqparse
from models.design import DesignModel
from models.mongo_import import db


class Design_get(Resource):
    def get(self):
        return {'design_diploma': [design.json() for design in DesignModel.query.all()]}

class Design(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name_design')
    argumentos.add_argument('cnpj_design')
    argumentos.add_argument('hash_design')
    argumentos.add_argument('files_design')

    def get(self, id_design_diploma):
        try:
            design = DesignModel.find_design(id_design_diploma)
            if design:
                return design.json()
            return {'message': 'Design not found.'}, 404 # not found
        except:
            return {'message': 'Erro no sistema, contate o operador'}, 500 # Internal error.
    

    def post(self, id_design_diploma):

        if DesignModel.find_design(id_design_diploma):
            return {"message": "Design id '{}' already exists.".format(id_design_diploma)}, 400 # bad request

        dados = Design.argumentos.parse_args()

        design = DesignModel(id_design_diploma, **dados)
        try:
            design.save_design()
        except:
            return{'message': 'An internal error ocurred trying to save design.'}, 500 # internal Server Error
        return design.json()

    def put(self, id_design_diploma):

        dados = Design.argumentos.parse_args()
        design_encontrado = DesignModel.find_design(id_design_diploma)

        if design_encontrado:
            design_encontrado.update_design(**dados)
            design_encontrado.save_design()
            return design_encontrado.json(), 200
        
        # filtro = {'id_design_diploma': design_encontrado}
        # update = {'$set': {'id_design_diploma': self.id_design_diploma,
            # 'name_design': self.name_design,
            # 'cnpj_design': self.cnpj_design,
            # 'hash_design': self.hash_design,
            # 'files_design': self.files_design}}
        # return db.update_one(filtro, update)


        design = DesignModel(id_design_diploma, **dados)
        design.save_design()
        
        return design.json(), 201 # created
        

    def delete(self, id_design_diploma):
        design = DesignModel.find_design(id_design_diploma)
        if design:
            try:
                design.delete_design()
            except:
                return{'message': 'An internal error ocurred trying to save design.'}, 500 # internal Server Error   
            return {'message': 'Design deleted.'}
        return {'message': 'Design not found.'}, 404