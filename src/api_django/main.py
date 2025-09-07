#!/usr/bin/env python
"""
Django REST API for JSON parsing.

Run with: python main.py
"""

import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "json_parser.settings")
    import django

    django.setup()

    from django.core.management import execute_from_command_line

    # Run the development server
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
