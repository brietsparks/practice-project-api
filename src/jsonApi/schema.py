from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class AbilitySchema(Schema):
    class Meta:
        type_ = 'abilities'
        self_view = 'ability_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'ability_list'

    id = fields.Integer(dump_only=True)
    owner_id = fields.Str()
    short_summary = fields.Str()

    contributions = Relationship(self_view='ability_contribution',
                                 self_view_kwargs={'id': '<id>'},
                                 related_view='contribution_list',
                                 related_view_kwargs={'id': '<id>'},
                                 many=True,
                                 schema='ContributionSchema',
                                 type_='contributions')


class ContributionSchema(Schema):
    class Meta:
        type_ = 'contributions'
        self_view = 'contribution_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'contribution_list'

    id = fields.Integer(dump_only=True)
    owner_id = fields.Str()
    title = fields.Str()
    subtitle = fields.Str()

    skills = Relationship(self_view='contribution_skill',
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
    contribution_id = fields.Integer()
    creator_id = fields.Str()
    name = fields.Str()
