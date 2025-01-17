# airbnb-clone-django
django restframework v5 based backend service with python v3.12


## how to run

### setup

-   install python 3.10 ~ 3.12 LTS and add system path on python & pip

```sh
$ python --version
Python 3.12.7 (or 3.10.11 or 3.11.9 or 3.12.8)

$ pip --version
pip 24.2 from /usr/lib/python3/dist-packages/pip (python 3.12)

$ pip install poetry==1.8.5
$ poetry --version
Poetry (version 1.8.5)
```

### config

-   set runtime environment

```sh
$ cat .env
SECRET_KEY="..."
```

### launch

-   run jupyter app in poertry environment

```sh
$ poetry init
$ poetry shell
$ poetry install
$ poetry show
$ touch main.ipynb && code .
$ exit
```
