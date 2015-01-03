Deployment
==========

Workstations and servers are configure using Ansible_ using the configuration in the deployment_ repository. Machines are configured in a 1:N pattern, with each workstation having an inventory file specifying the local machine and any number of external systems (example_). This is useful for two reasons:

- Information about specific machines is not kept in the repository
- Machines in different environments (e.g. home and work) are kept completely separate but can still use the same configuration

.. _Ansible: http://docs.ansible.com/
.. _deployment: https://github.com/borntyping/deployment/
.. _example: https://github.com/borntyping/deployment/blob/master/inventory.conf.example
