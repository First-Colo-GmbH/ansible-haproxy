
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import errors
from ansible.module_utils import basic

import re
import os.path
import sys

def haproxy_verify_binds_ssl(searchstring):
    ''' Verifys the input string to have all ssl pem files existing, otherwise HAproxy won't start '''
    filesnotfound = 0
    entrys = re.findall("crt (\/[^\s]+)", searchstring[0])
    for entry in entrys:
        if not os.path.exists(entry):
            raise errors.AnsibleFilterError("|path not found %s" % entry)
            filesnotfound += 1
    if filesnotfound == 0:
        return True
    else:
        return False;

class FilterModule(object):
    ''' Ansible haproxy jinja2 filters '''
    def filters(self):
        return {
            'haproxy_verify_binds_ssl' : haproxy_verify_binds_ssl
        }




