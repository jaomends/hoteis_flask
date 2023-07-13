from sql_alchemy import banco


class DesignModel(banco.Model):

    __tablename__ = 'design_diplomas'

    id_design_diploma = banco.Column(banco.String, primary_key=True)
    name_design = banco.Column(banco.String(80))
    cnpj_design = banco.Column(banco.String)
    hash_design = banco.Column(banco.Float)
    files_design = banco.Column(banco.String(40))

    def __init__(self, id_design_diploma, name_design, cnpj_design, hash_design, files_design): # noqa
        self.id_design_diploma = id_design_diploma
        self.name_design = name_design
        self.cnpj_design = cnpj_design
        self.hash_design = hash_design
        self.files_design = files_design

    def json(self):
        return {
            'id_design_diploma': self.id_design_diploma,
            'name_design': self.name_design,
            'cnpj': self.cnpj_design,
            'hash': self.hash_design,
            'files': self.files_design
        }

    @classmethod
    def find_design(cls, id_design_diploma):
        design = cls.query.filter_by(id_design_diploma=id_design_diploma).first()  # noqa SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if design:
            return design
        return None

    def save_design(self):
        banco.session.add(self)
        banco.session.commit()

    def update_design(self, name_design, cnpj_design, hash_design, files_design): # noqa
        self.name_design = name_design
        self.cnpj_design = cnpj_design
        self.hash_design = hash_design
        self.files_design = files_design

    def delete_design(self):
        banco.session.delete(self)
        banco.session.commit()
