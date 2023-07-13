from flask_restful import Resource, reqparse # noqa
from models.design import DesignModel
from flask_jwt_extended import create_access_token # noqa
from werkzeug.security import check_password_hash # noqa


class Design_Diploma(Resource):
    def get(self):
        return {'design_diplomas': [design.json() for design in DesignModel.query.all()]}  # noqa [design.json() for design in DesignModel.query.all()]


class Design(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name_design')  # noqa
    argumentos.add_argument('cnpj')
    argumentos.add_argument('hash')
    argumentos.add_argument('files')

    def get(self, id_design_diploma):
        design = DesignModel.find_design(id_design_diploma)
        if design:
            return design.json()
        return {'message': 'Design not found.'}, 404  # not found

    def post(self, id_design_diploma):

        if DesignModel.find_design(id_design_diploma):
            return {"message": "Design id '{}' already exists.".format(id_design_diploma)}, 400  # noqa bad request

        dados = Design.argumentos.parse_args()

        design = DesignModel(id_design_diploma, **dados)
        try:
            design.save_design()
        except:
            return {'message': 'An internal error ocurred trying to save design.'}, 500  # noqa internal Server Error
        return design.json()

    def put(self, id_design_diploma):

        dados = Design.argumentos.parse_args()
        design_find = DesignModel.find_design(id_design_diploma)

        if design_find:
            design_find.update_design(**dados)
            design_find.save_design()
            return design_find.json(), 200
        design = DesignModel(id_design_diploma, **dados)
        try:
            design.save_design()
        except:
            return {'message': 'An internal error ocurred trying to save design.'}, 500  # noqa internal Server Error        
        # return db.update_one(filtro, update)
        # design = DesignModel(id_design_diploma, **dados)
        # design.save_design()
        return design.json(), 201  # created

    def delete(self, id_design_diploma):
        design = DesignModel.find_design(id_design_diploma)
        if design:
            try:
                design.delete_design()
            except:
                return {'message': 'An internal error ocurred trying to save design.'}, 500  # noqa internal Server Error
            return {'message': 'Design deleted.'}
        return {'message': 'Design not found.'}, 404
