#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2022
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: custom_set_premission_profiles_access_layer
short_description: add or removes a permission profile to a existing access layer object.
description:
  - Set administrator permission profile to a existing access layer object.
  - All operations are performed over Web Services API.
author: "Jim Oqvist (@chkp-jimo)"
extends_documentation_fragment: check_point.mgmt.checkpoint_commands
"""

EXAMPLES = """
- name: Add premission profile to access layer
  custom_set_premission_profiles_access_layer:
    uid: 3cf45827-3a79-46e5-b368-1258d83ea958
    permissionsProfiles:
      add:
      - dc91382e-9f81-4c62-912b-5bd86778cdce

- name: Remove premission profile to access layer
  custom_set_premission_profiles_access_layer:
    uid: 3cf45827-3a79-46e5-b368-1258d83ea958
    permissionsProfiles:
      remove:
      - dc91382e-9f81-4c62-912b-5bd86778cdce
"""

RETURN = """
custom_add_repository_package:
  description: The checkpoint add-repository-package output.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.mgmt.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_commands, api_command


def main():
    argument_spec = dict(
        uid=dict(type='str', required=True),
        permissionsProfiles=dict(type='dict', options=dict(
            add=dict(type='list', elements='str')
            )),
            remove=dict(type='list', elements='str')
    )
    argument_spec.update(checkpoint_argument_spec_for_commands)

    module = AnsibleModule(argument_spec=argument_spec)
    command = 'set-generic-object'

    result = api_command(module, command)
    module.exit_json(**result)


if __name__ == '__main__':
    main()