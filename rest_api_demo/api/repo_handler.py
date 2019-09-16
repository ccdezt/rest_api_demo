import logging
import threading
import time
from api.Git import Git

log = logging.getLogger(__name__)

queue = []


class QueueOperation(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if not queue:
                time.sleep(10)
            else:
                self.handler()

    @staticmethod
    def handler():
        global queue
        log.info("Getting {} from queue...".format(queue[0].name))
        git = queue[0]
        if not isinstance(git, Git):
            log.error("A non-Git instance is in queue")
            return -1
        git.clone()
        git.switch_to_master()
        git.create_branch()
        git.create_file()
        git.add()
        git.commit()
        git.push()
        git.switch_to_master()
        queue.pop(0)


def queue_up_project(git_obj):
    global queue
    queue.append(git_obj)



'''
def git_handler(name):
    g = Git(name)
    #if not g_obj.check_file_exists(g_obj.get_repo_dir(), name):
    g.queue_up()
    while g.get_active_in_queue() != name:
        log.info("{} - waiting on {} .....".format(name, g.get_active_in_queue()))
        log.info("{} - queue list {} .....".format(name, g.get_queue()))
        time.sleep(2)
    """
    log.info("{} - sleeping for 20 .....".format(name))
    log.info("{} - queue list {} .....".format(name, g.get_active_in_queue()))
    time.sleep(20)
    log.info("{} - checking the queue......".format(name))
    log.info("{} - in queue {} .....".format(name, g.get_active_in_queue()))
    g.get_active_in_queue()
    log.info("{} - removing from queue.....".format(name))
    g.remove_from_queue()
    """

    g.switch_to_master()
    g.create_branch()
    g.create_file(name)
    g.add()
    g.commit()
    g.push()
    g.switch_to_master()
    g.remove_from_queue()'''

"""
g_obj.set_active()
g_obj.queue_up()
g_obj.switch_to_master()
g_obj.create_branch()
g_obj.create_file(name)
g_obj.add()
g_obj.commit()
g_obj.push()
g_obj.switch_to_master()
g_obj.remove_from_queue()
g_obj.set_inactive()
"""


