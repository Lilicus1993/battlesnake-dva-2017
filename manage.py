"""Django entry point"""
#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line
from django.core.management.commands.runserver import Command as runserver
import netifaces

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    if not os.environ.get('IS_PRODUCTION', False):
        ASSIGNED_IP = netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
        ASSIGNED_IP6 = netifaces.ifaddresses('en0')[netifaces.AF_INET6][0]['addr']

        runserver.default_addr = ASSIGNED_IP
        runserver.default_addr_ipv6 = ASSIGNED_IP6

    execute_from_command_line(sys.argv)
