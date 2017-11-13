from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    skills = db.relationship('Skill', backref='project')


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    creator_id = db.Column(db.String())
    name = db.Column(db.String())
