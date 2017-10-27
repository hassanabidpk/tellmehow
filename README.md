# Setup development version

### Prerequisites

- Install Python 3.5 [download][https://www.python.org/downloads/]
- Install git download
- Install a code editor (Sublime Text, Atom or any of your choice)

## Setup TellMeHow development environment

Clone the repository

Clone the github repository by executing following command in Command prompt on windows

`git clone https://github.com/hassanabidpk/tellmehow.git`

## Setup local server

After cloning the repository do the following steps

```
> cd tellmehow
> python -m venv hackvenv
> source hackvenv/bin/activate
(hackvenv) > pip install -r requirements.txt
```

Run following command

```
(hackvenv) > python manage.py migrate
```

Start server

```
(hackvenv) > python manage runserver
```

visit localhost:8000 or http://127.0.0.1:8000