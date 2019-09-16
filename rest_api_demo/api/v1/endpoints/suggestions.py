import logging

from flask import request
from flask_restplus import Resource
from api.restplus import api
from api import helper
from api.Git import Git
from api.repo_handler import queue_up_project
from api import repo_handler

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

@ns.route('/git/<string:name>')
class GitTest(Resource):

    def get(self, name):
        """
        Runs through the process of adding, committing and pushing into a git repo

        """

        new_git = Git(name)
        queue_up_project(new_git)
        #repo_handler.git_handler(name)



