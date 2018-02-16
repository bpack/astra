A Simple Task ReST API

Generate requirements.txt 
`pipenv lock -r > requirements.txt`

Recreate the database
> rm -rf migrations
> rm astra/astra.sqlite

> python manage.py db init
> python manage.py db migrate
> python manage.py db upgrade 

>>> import astra
>>> app = astra.create_app()
>>> db = astra.db
>>> app.app_context().push()
>>> db.create_all()
>>> from astra.models import User
>>> u = User('bpack', 'bpack@example.com')
>>> db.session.add(u)
>>> db.session.commit()

>>> db.session.query(User).all()