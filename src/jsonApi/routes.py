from flask_rest_jsonapi import Api
from src.jsonApi.resources import (
    AbilityList, AbilityDetail, AbilityRelationship,
    ContributionList, ContributionDetail, ContributionRelationship, 
    SkillList, SkillDetail
)


def init_routes(app):
    api = Api(app)

    api.route(AbilityList, 'ability_list', '/abilities')
    api.route(AbilityDetail, 'ability_detail', '/abilities/<int:id>')
    api.route(AbilityRelationship, 'ability_skills', '/abilities/<int:id>/relationships/skills')
    api.route(ContributionList, 'contribution_list', '/contributions')
    api.route(ContributionDetail, 'contribution_detail', '/contributions/<int:id>')
    api.route(ContributionRelationship, 'contribution_skills', '/contributions/<int:id>/relationships/skills')
    api.route(SkillList, 'skill_list', '/skills')
    api.route(SkillDetail, 'skill_detail', '/skills/<int:id>')