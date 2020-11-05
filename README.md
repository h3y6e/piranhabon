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
2. Download `credentials.json`
3. Run script

```sh
$ poetry install
$ poetry run python piranhabon.py
```

<!-- ### or Deploying to Heroku

```sh
$ heroku create
$ git push heroku main
$ heroku open
```

or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/5ebec/piranhabon/tree/main) -->

## How to Download `credentials.json`

1. Go https://developers.google.com/calendar/quickstart/python?hl=ja
1. Click "Enable the Google Calender API" button.
1. Enter new project name on the pop-up for this app (e.g. "naist-timetable")
1. Select app type (e.g. Desktop App)
1. Click "Create" button
1. Click "DOWNLOAD CLIENT CONFIGURATION" button and download `credentials.json`
1. Put `credentials.json` into root folder of this repository

## LICENSE

[MIT](./LICENSE)
