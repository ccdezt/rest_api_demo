import logging

from flask import request
from flask_restplus import Resource
from api.restplus import api
from api import helper

log = logging.getLogger(__name__)

ns = api.namespace('v1/suggestions', description='Operations related to making blog suggestions')


@ns.route('/')
@api.response(404, 'page ont found')
class SuggestionCollection(Resource):

    def get(self):
        """
        Just a quick suggestion

        ..and a comment
        """
        data = {
            "name": "joe sanders",
            "comment": "no pressure"
        }

        d = helper.Helper()
        return d.get()


@ns.route('/<string:name>')
class SuggestionItem(Resource):

    def get(self, name):
        """
        Just a quick yml suggestion

        ...speciy 'name'
        """

        data = {
            "name": "somefile.yml",
            "comment": "this does nothing"
        }

        d = helper.Helper()
        return d.get_yml(name)
