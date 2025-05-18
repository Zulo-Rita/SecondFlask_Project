import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance/darbuotojai.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


