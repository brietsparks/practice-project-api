from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class ProjectSchema(Schema):
    class Meta:
        type_ = 'projects'
        self_view = 'project_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'project_list'

    id = fields.Integer(dump_only=True)
    owner_id = fields.Str()
    title = fields.Str()
    subtitle = fields.Str()

    skills = Relationship(self_view='project_skills',
                          self_view_kwargs={'id': '<id>'},
                          related_view='skill_list',
                          related_view_kwargs={'id': '<id>'},
                          many=True,
                          schema='SkillSchema',
                          type_='skills')


class SkillSchema(Schema):
    class Meta:
        type_ = 'skills'
        self_view = 'skill_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'skill_list'

    id = fields.Integer()
    project_id = fields.Integer()
    creator_id = fields.Str()
    name = fields.Str()
