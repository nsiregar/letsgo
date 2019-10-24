it's work in progress

update to use `docker` and `docker-compose`, to run use command

```
$ docker-compose up -d
```

browse in `http://localhost`

### Create Models

Yeay, we have better implementation

1. Create `model` class in `app/models`, add `__tablename__` attribute to define `table name` in database
2. Generate database migration with  
   `$ docker-compose exec web alembic revision --autogenerate -m "migration message"` or  
   `$ docker-compose exec web bin/generate_migration "migration message"`
3. Run your migration with  
   `$ docker-compose exec web LETSGO_ENV=<dev/test/prod> alembic upgrade head` or  
   `$ docker-compose exec bin/run_migrations` - this command will run migrations only on `development` and `test` environment.

### Structures

This app have structures as follows
```
./letsgo
├── app
│   ├── endpoints
│   ├── events
│   ├── models
│   └── wsgi.py
├── config
│   ├── application.py
│   └── environment
│       ├── base.py
│       ├── development.py
│       ├── production.py
│       └── testing.py
├── migrations
│   └── versions
└── routes
    └── applications.py
```
1. `app` contains our `models`, `events`, `endpoints`
2. `config` contains app config
3. `migrations/versions` where database migrations generated
4. `routes` contains our app routes
