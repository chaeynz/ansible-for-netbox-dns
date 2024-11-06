# Ansible for Netbox DNS

Based on [netbox-community/ansible_modules/0e4a6b8a8d85426092ebd65eb1d9726f9328dbfa](https://github.com/netbox-community/ansible_modules/tree/0e4a6b8a8d85426092ebd65eb1d9726f9328dbfa)

```
NETBOX_API="<url>" NETBOX_TOKEN="<token>" ansible-playbook playbooks/netbox_nb_dns_record-playbook.yml --extra-vars "name=<str> zone=<str> _state=<present/absent>"
```

Tested on: Netbox Community v4.1.4

PS: Writing test cases is a sign of weakness
