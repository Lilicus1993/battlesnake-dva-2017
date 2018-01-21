#!/usr/bin/env python
import os
import sys
import netifaces

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snake.settings")

    from netifaces import AF_INET, AF_INET6
    ASSIGNED_IP = netifaces.ifaddresses('en0')[AF_INET][0]['addr']
    ASSIGNED_IP6 = netifaces.ifaddresses('en0')[AF_INET6][0]['addr']

    from django.core.management.commands.runserver import Command as runserver
    runserver.default_addr = ASSIGNED_IP
    runserver.default_addr_ipv6 = ASSIGNED_IP6

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
