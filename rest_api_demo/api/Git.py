import logging
import os
import os.path
import sys
import subprocess

log = logging.getLogger(__name__)

git = "git"
repo_base_dir = r'C:\Temp'

curr_dir = os.getcwd()
repo_dir = os.path.join(repo_base_dir, "scratch_test")

repo_store = "https://github.com/ccdezt/scratch_test.git"

class Git(object):


    def __init__(self, file_name):
        self._repo_url = repo_store
        self._repo_dir = repo_dir
        self.name = file_name
        self.is_branch = False
        self.branch = "feature/{}".format(file_name)

    def clone(self):
        if not os.path.exists(self._repo_dir):
            log.info('{} - Cloning Repository.....'.format(self.name))
            os.chdir(repo_base_dir)
            subprocess.call([git, 'clone', self._repo_url])
            os.chdir(curr_dir)

    def add(self, filename=None):
        if not filename:
            filename = self.name + ".yml"
        log.info('{} - Adding file: {}'.format(self.name, filename))
        self._git_run(git, 'add', os.path.join(repo_dir, filename))

    def commit(self, filename=None):
        if not filename:
            filename = self.name
        log.info('{} - Commiting file: {}'.format(self.name, filename))
        self._git_run(git, 'commit', '-m', "{} - Adding file {}".format(self.name, filename))

    def push(self):
        log.info('{} - Rebase and push new file into repo'.format(self.name))
        if self.is_branch:
            self._git_run(git, 'push', '--set-upstream', 'origin', self.branch)
        else:
            self._git_run(git, 'rebase')
            self._git_run(git, 'push')

    def create_branch(self, branch=None):
        if not branch:
            branch = self.branch

        import re
        try:
            re.match('^feature/', branch)[0]
        except TypeError:
            branch = "feature/{}".format(branch)

        log.info('{} - Creating branch: {}'.format(self.name, branch))
        self._git_run(git, 'checkout', '-b', branch)
        self.is_branch = True

    def switch_to_master(self):
        log.info('{} - Switching to master branch'.format(self.name))
        self._git_run(git, 'checkout', 'master')
        self.is_branch = False

    def _git_run(self, *args):
        no_dir_change = ['config']
        if args[0].__contains__('git'):
            if args[1] in no_dir_change:
                code = subprocess.call([*args])
            else:
                os.chdir(repo_dir)
                code = subprocess.call([*args])
                os.chdir(curr_dir)
            if code > 1:
                log.warning("{} - Command failed: {}".format(self.name, *args))
                return code
        else:
            return log.warning("{} - Not running a GIT command".format(self.name))
        return 1

    def create_file(self, filename=None):
        if not filename:
            filename = self.name
        filename = filename + ".yml"
        file_path = os.path.join(repo_dir, filename)
        try:
            with open(file_path, 'w') as f:
                f.write("this is just a test {}".format(filename))
            log.info('{} - Wrote file: {}'.format(self.name, file_path))
        except Exception as e:
            log.error("{} - Unable to write to {}".format(self.name, file_path))
            log.error("{} - General catch error: {e}".format(self.name, e=e))

    def check_file_exists(self, dir, filename):
        file_path = os.path.join(dir, filename)
        if os.path.exists(file_path):
            log.info('{} - File {} exists!'.format(self.name, file_path))
            return True

        log.info('{} - File {} does NOT exist!'.format(self.name, file_path))
        return False

    def get_repo_dir(self):
        return self._repo_dir


if __name__ == "__main__":
    g = Git("name")
    print(type(g))
    if not isinstance(g, Git):
        print("not Git")
    else:
        print("is Git!")