it's work in progress

update to use `docker` and `docker-compose`, to run use command

```
$ docker-compose up -d
```

browse in `http://localhost`

### Create Models

This is sucks, need to find better implementation

1. create `model` class in `app/models`
2. import `model` to `db/metadata.py`
3. generate alembic migration with `$ docker-compose exec web alembic revision --autogenerate -m "migration message"`
4. run your migration with `$ docker-compose exec web alembic upgrade head`

