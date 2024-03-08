set -o errexit
pip install -r requirements.py
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py tailwind build