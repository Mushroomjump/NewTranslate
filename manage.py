#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Translate.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'fintech',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://sbp1784:OBbxnqbZowezp2qX@iwazolab.sksu1fm.mongodb.net/?retryWrites=true&w=majority',
        }
    }
}


if __name__ == '__main__':
    main()
