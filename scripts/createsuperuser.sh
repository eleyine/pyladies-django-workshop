#!/bin/bash

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@keep.com', 'pass')" | python manage.py shell
