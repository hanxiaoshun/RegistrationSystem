id = '152224199101106515'
print(id[6:14][6:8])
import os

os.environ.update({"DJANGO_SETTINGS_MODULE": "baoming.settings"})
import django.utils.timezone as timezone
age = timezone.now().year - int("1991")

print(str(age))