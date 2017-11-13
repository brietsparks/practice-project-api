from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from src.jsonApi.schema import ProjectSchema, SkillSchema
from src.data.models import db, Project, Skill
from src.jsonApi.decorators import authDecorator


class ProjectList(ResourceList):
    schema = ProjectSchema
    data_layer = {
        'session': db.session,
        'model': Project
    }
    decorators = authDecorator


class ProjectDetail(ResourceDetail):
    schema = ProjectSchema
    data_layer = {
        'session': db.session,
        'model': Project,
    }
    decorators = authDecorator


class ProjectRelationship(ResourceRelationship):
    schema = ProjectSchema
    data_layer = {
        'session': db.session,
        'model': Project
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

