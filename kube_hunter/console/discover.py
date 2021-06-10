import cmd
import logging

from kube_hunter.console.env import environment
from kube_hunter.modules.discovery.hosts import RunningAsPodEvent

class DiscoverSubConsole(cmd.Cmd):
    prompt = environment.get_prompt(sub_console="discover")

    def do_local(self, arg):
        # pod discovery
        pass    
            

    def do_exit(self, arg):
        return True

    def postcmd(self, stop, line):
        if stop:
            return True
        self.prompt = environment.get_prompt(sub_console="discover")

    # binds EOF to exit the shell as well
    do_EOF = do_exit