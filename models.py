from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()



class Darbuotojas(db.Model):
    __tablename__ = 'darbuotojai'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String)
    pavarde = db.Column(db.String)
    gimimo_data = db.Column(db.String)
    pareigos = db.Column(db.String)
    skyrius_pavadinimas = db.Column(db.String)
    uzduotys = db.relationship('Uzduotis', backref='darbuotojas', cascade='all, delete-orphan')

    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    def __repr__(self):
        return f'{self.vardas} {self.pavarde} {self.gimimo_data} {self.pareigos} {self.skyrius_pavadinimas}'


class Uzduotis(db.Model):
    __tablename__ = 'uzduotys'
    id = db.Column(db.Integer, primary_key=True)
    uzduotis = db.Column(db.String)
    aprasymas = db.Column(db.String)
    skirtas_laikas = db.Column(db.String)
    statusas = db.Column(db.String)
    darbuotojas_id = db.Column(db.Integer, db.ForeignKey('darbuotojai.id'), nullable=False)

    def __init__(self, uzduotis, aprasymas, skirtas_laikas, statusas, darbuotojas_id=None):
        self.uzduotis = uzduotis
        self.aprasymas = aprasymas
        self.skirtas_laikas = skirtas_laikas
        self.statusas = statusas
        self.darbuotojas_id = darbuotojas_id

    def __repr__(self):
        return f'{self.uzduotis} {self.uzduotis} {self.skirtas_laikas} {self.statusas}'
