from flask_rest_jsonapi import Api
from src.jsonApi.resources import (
    ProjectList, ProjectDetail, ProjectRelationship, SkillList, SkillDetail
)


def init_routes(app):
    api = Api(app)

    api.route(ProjectList, 'project_list', '/projects')
    api.route(ProjectDetail, 'project_detail', '/projects/<int:id>')
    api.route(ProjectRelationship, 'project_skills', '/projects/<int:id>/relationships/skills')
    api.route(SkillList, 'skill_list', '/skills')
    api.route(SkillDetail, 'skill_detail', '/skills/<int:id>')