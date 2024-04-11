# leaflet-map-marker-geodjango
Interactive map to add markers with title, description and a href for a website you want.
Simple WebGIS using the Leaflet map library and GeoDjango.

The database used in the project is PostgreSQL with the PostGIS extension.

## It's part of the WebGIS work I do. Still in development.

### Installation 
Clone the repository, and don't forget to start your virtualenv.
```
    python3 -m venv venv
```

### To run virtualenv:
```
    source /venv/bin/activate
```
### Install dependencies.
```
    pip install -r requirements.txt
```

### Running the project. Change directory to ./geodjango
```
    python ./manage.py runserver
```
### Remeber to change in the settings.py of the project the database connection fields to suit your use.

In the localhost, goes to /markers/map and see your map.

In the terminal, create a superuser to log into the Django admin site and add, edit, and delete markers.
```
  python ./manage.py createsuperuser
```

