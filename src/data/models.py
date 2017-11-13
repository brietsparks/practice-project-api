from app import db


project_skills = db.Table(
    'project_skill',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    skills = db.relationship('Skill', secondary=project_skills, backref='projects')


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.String())
    name = db.Column(db.String())
    # projects = db.relationship('Project', secondary=project_skills, backref='skills')
