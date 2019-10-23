it's work in progress

update to use `docker` and `docker-compose`, to run use command

```
$ docker-compose up -d
```

browse in `http://localhost`

### Create Models

Yeay, we have better implementation

1. create `model` class in `app/models`, add `__tablename__` attribute to define `table name` in database
2. generate alembic migration with `$ docker-compose exec web alembic revision --autogenerate -m "migration message"`
3. run your migration with `$ docker-compose exec web alembic upgrade head`

