from app import db

ability_contributions = db.Table(
    'ability_contribution',
    db.Column('ability_id', db.Integer, db.ForeignKey('ability.id')),
    db.Column('contribution_id', db.Integer, db.ForeignKey('contribution.id'))
)

contribution_skills = db.Table(
    'contribution_skill',
    db.Column('contribution_id', db.Integer, db.ForeignKey('contribution.id')),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
)


class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String())
    short_summary = db.Column(db.String())


class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    skills = db.relationship('Skill', secondary=contribution_skills, backref='contributions')


# class Employer(db.Model):
#     id =

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.String())
    name = db.Column(db.String())
    # contributions = db.relationship('Contribution', secondary=contribution_skills, backref='skills')
