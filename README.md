# klingon_transcriber

# Pictures of pIqaD
[Klingon Wiki](http://klingon.wiki/En/PIqaD)

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject transcriber .  
3. Generate application : python3 manage.py startapp klingon

# To migrate after changing models
1. python manage.py makemigrations
2. python manage.py migrate

# Run server
python3 manage.py runserver  

# For sqllite db admin
- Create super user : python3 manage.py createsuperuser

# To make ready for Azure
1. Add requirements.txt
2. Add 'klingon-transcriber.azurewebsites.net' to ALLOWED_HOSTS
3. Static_root to settings.py
4. Add to u=rlsettings in url.py + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

