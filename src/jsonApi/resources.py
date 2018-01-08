from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from src.jsonApi.schema import AbilitySchema, ContributionSchema, SkillSchema
from src.data.models import db, Ability, Contribution, Skill
from src.jsonApi.decorators import authDecorator


class AbilityList(ResourceList):
    schema = AbilitySchema
    data_layer = {
        'session': db.session,
        'model': Ability
    }
    decorators = authDecorator


class AbilityDetail(ResourceDetail):
    schema = AbilitySchema
    data_layer = {
        'session': db.session,
        'model': Ability,
    }
    decorators = authDecorator


class AbilityRelationship(ResourceRelationship):
    schema = AbilitySchema
    data_layer = {
        'session': db.session,
        'model': Ability
    }
    decorators = authDecorator


class ContributionList(ResourceList):
    schema = ContributionSchema
    data_layer = {
        'session': db.session,
        'model': Contribution
    }
    decorators = authDecorator


class ContributionDetail(ResourceDetail):
    schema = ContributionSchema
    data_layer = {
        'session': db.session,
        'model': Contribution,
    }
    decorators = authDecorator


class ContributionRelationship(ResourceRelationship):
    schema = ContributionSchema
    data_layer = {
        'session': db.session,
        'model': Contribution
    }
    decorators = authDecorator


class SkillList(ResourceList):
    schema = SkillSchema
    data_layer = {
        'session': db.session,
        'model': Skill
    }
    decorators = authDecorator


class SkillDetail(ResourceDetail):
    schema = SkillSchema
    data_layer = {
        'session': db.session,
        'model': Skill,
    }
    decorators = authDecorator


class SkillRelationship(ResourceRelationship):
    schema = SkillSchema
    data_layer = {
        'session': db.session,
        'model': Skill,
    }
    decorators = authDecorator

