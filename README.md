# Piranhabon

convert **your** NAIST timetable into Google Calendar
## Requirement
poetry
```sh
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
$ source $HOME/.poetry/env
```
## Usage

1. Create a `.env` with `.env.sample` as a reference.
2. Run script

```sh
$ poetry install
$ poetry run python piranhabon.py
```

### or Deploying to Heroku

```sh
$ heroku create
$ git push heroku main
$ heroku open
```

or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/5ebec/piranhabon/tree/main)

## LICENSE

[MIT](./LICENSE)
