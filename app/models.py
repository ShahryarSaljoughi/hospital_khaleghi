from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from pytz import timezone

from app import db

Tehran = timezone('Asia/Tehran')


doctor_specialty_table = db.Table('doctor_specialty',
                db.Column('doctor_id', db.Integer, db.ForeignKey('doctors.id')),
                db.Column('specialty_id', db.Integer, db.ForeignKey('specialties.id'))
        )


class Drug(db.Model):
    __tablename__ = 'drugs'

    drug_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.TEXT, nullable=False)


class PaDoDr(db.Model):  # patient-doctor-drug

    __tablename__ = 'patient-doctor-drug'
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.drug_id'))
    drug = db.relationship('Drug', uselist=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    patient = db.relationship('Patient', back_populates='prescriptions', uselist=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor = db.relationship('Doctor', uselist=False)
    dosage = db.Column(db.Integer)
    description = db.Column(db.TEXT)


class Gender(db.Model):
    __tablename__ = 'genders'
    gender_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)

class HospitalSections(db.Model):
    __tablename__ = 'hospital_sectins'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))


class User(db.Model):
    __tablename__ = 'users'
    id =  db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    birthday = db.Column(db.DateTime)
    gender_id = db.Column(db.Integer, db.ForeignKey(
        'genders.gender_id',
        )
    )
    posts = db.relationship('Post', back_populates='author')
    gender = db.relationship('Gender')
    password_hash = db.Column(db.TEXT, nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        pass # I do not know what this is!!!

    def is_anonymous(self):
        return False


class Patient(User):
    __tablename__ = 'patients'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, db.ForeignKey(
        'users.id',
        ondelete="CASCADE",
        onupdate="CASCADE"),
        primary_key=True
    ) 
    admission_date = db.Column(db.DateTime)
    discharge_date = db.Column(db.DateTime)
    prescriptions = db.relationship(
        'PaDoDr',
        back_populates='patient'
    )



class Doctor(User):
    __tablename__ = 'doctors'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    specialty = db.relationship(
        'Specialty', secondary=doctor_specialty_table,
        backref=db.backref('doctors', lazy='dynamic')
    )
    prescriptions = db.relationship('PaDoDr', back_populates='doctor')


class Specialty(db.Model):
    __tablename__ = 'specialties'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False, unique=True)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', back_populates='posts')
    content = db.Column(db.TEXT)
    publish_date = db.Column(db.DateTime)
