Deployment
==========

My workstations and servers are configured using Ansible_ using the configuration in the deployment_ repository. Machines are configured in a 1:N pattern, with each workstation having an inventory file specifying the local machine and any number of external systems (example_). This keeps secure information out of the repository, keeps information about specific machines separate from general configuration, and allows environments (e.g. home and work) to be kept separate.

Servers
-------

All servers should have a DNS entry pointing ``NAME.borntyping.co.uk`` at their IPv4 and IPv6 addresses. DNS entries for ``NAME.borntyping.io`` are also useful, but not essential. Servers and other devices are named after Nerf guns.

SSH Keys
--------

SSH keys should always be tied to a specific device - no devices should *ever* share keys, so individual devices can have their access revoked at any time. Preferably keys should also be single use (i.e. one key per service or machine), but this can be impractical.

Check ``.ssh/authorized_keys``, `GitHub SSH keys <https://github.com/settings/ssh>`_ and `Bitbucket SSH Keys <https://bitbucket.org/account/user/borntyping/ssh-keys/>`_ for keys that are out of date.

.. _Ansible: http://docs.ansible.com/
.. _deployment: https://github.com/borntyping/deployment/
.. _example: https://github.com/borntyping/deployment/blob/master/inventory.conf.example
