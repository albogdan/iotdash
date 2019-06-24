@ECHO OFF

@ECHO Deleting old migrations and app.db files
rm -r migrations
rm app.db

@ECHO Initializing db
flask db init

@ECHO Migrating db
flask db migrate

@ECHO Upgrading db
flask db upgrade

@ECHO Seeding customers and devices
flask seed customers
flask seed devices
