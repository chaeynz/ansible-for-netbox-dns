#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, chaeynz <chaeynz4msg@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_nb_dns_record
short_description: Create, update or delete DNS record within NetBox DNS
description:
  - Creates, updates or removes DNS records from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - chaeynz (@chaeynz)
requirements:
  - pynetbox
version_added: '0.1.0'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    description:
      - Defines the DNS record configuration.
    suboptions:
      name:
        description:
          - The name of the DNS record.
        required: true
        type: str
      zone:
        description:
          - The DNS zone where this record is going to be created.
        required: true
        type: raw
      type:
        description:
          - Specifies the type of the DNS record.
        required: true
        type: str
      value:
        description:
          - Sets the value of the record.
        required: true
        type: str
      status:
        description:
          - Defines the operational status of the resource. Accepts the values active/inactive.
        required: false
        type: raw
      ttl:
        description: 
          - Time-to-live (TTL) value for the DNS record, in seconds.
        required: false
        type: int
      description:
        description:
          - A brief text field for additional information about the resource.
        required: false
        type: str
      tags:
        description:
          - List of any tags that the DNS record may be associated with.
        required: false
        type: list
        elements: raw
      disable_ptr:
        description:
          - If set to C(true), disables automatic creation of a PTR (reverse DNS) record for this resource.
        required: false
        type: bool
      custom_fields:
        description:
          - Dictionary of custom fields associated with the resource.
        required: false
        type: dict
      tenant:
        description:
          - Tenant responsible for this resource.
        required: false
        type: raw
    required: true
"""

EXAMPLES = r"""
- name: "Test NetBox Modules
  connection: local
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Create DNS record
      chaeynz.netbox_dns.netbox_nb_dns_record:
        netbox_url: "{{ lookup('ansible.builtin.env', 'NETBOX_API') }}"
        netbox_token: "{{ lookup('ansible.builtin.env', 'NETBOX_TOKEN') }}"
        data:
          name: "one"
          zone: "one.one.one"
          type: "A"
          value: "1.1.1.1"
        state: present
"""

RETURN = r"""
record:
  description: Serialized object as created or already existent within NetBox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.chaeynz.netbox_dns.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.chaeynz.netbox_dns.plugins.module_utils.netbox_nb_dns import (
    NetboxDnsModule,
    NB_RECORDS
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    name=dict(required=True, type="str"),
                    zone=dict(required=True, type="raw"),
                    type=dict(required=True, type="str"),
                    value=dict(required=True, type="str"),
                    status=dict(required=False, type="raw"),
                    ttl=dict(required=False, type="int"),
                    description=dict(required=False, type="str"),
                    tags=dict(required=False, type="list", elements="raw"),
                    disable_ptr=dict(required=False, type="bool"),
                    custom_fields=dict(required=False, type="dict"),
                    tenant=dict(required=False, type="raw"),
                ),
            ),
        )
    )


    module = NetboxAnsibleModule (
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    netbox_dns_record = NetboxDnsModule(
        module=module,
        endpoint=NB_RECORDS
    )
    netbox_dns_record.run()


if __name__ == '__main__':
    main()
