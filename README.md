# airbnb-clone-django
django restframework v5 based backend service with python v3.12


## how to run

### setup

- install python 3.10 ~ 3.12 LTS and add system path on python & pip

```sh
$ python --version
Python 3.12.7 (or 3.10.11 or 3.11.9 or 3.12.8)

$ pip --version
pip 24.2 from /usr/lib/python3/dist-packages/pip (python 3.12)

$ pip install poetry==1.8.5
$ poetry --version
Poetry (version 1.8.5)
```

### configure

- setup poetry virtual environment

```sh
$ poetry init
$ poetry shell
$ poetry install
$ poetry show
$ poetry env info
$ exit
```

- set runtime configuration

```sh
$ cat .env
SECRET_KEY="..."
```

- create superuser account

```sh
$ ./manage.py createsuperuser 
...
Superuser created successfully.
```

- apply database schema

```sh
$ ./manage.py makemigrations
No changes detected

$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, authtoken, bookings, categories, contenttypes, direct_messages, experiences, medias, reviews, rooms, sessions, users, wishlists
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
  Applying wishlists.0002_alter_wishlist_experiences_alter_wishlist_rooms_and_more... OK
```

### launch

- run django app in poertry environment

```sh
$ poetry shell
$ ./manage.py runserver_plus
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 627-132-328
```

### browse

- check django admin service in web browser

```sh
$ curl https://localhost:8000/admin
```

- login to admin service with superuser account


### query

- run orm query in django shell

```sh
$ poetry shell
$ ./manage.py shell_plus
# Shell Plus Model Imports
from bookings.models import Booking
from categories.models import Category
from direct_messages.models import ChattingRoom, Message
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from experiences.models import Experience, Perk
from medias.models import Photo, Video
from rest_framework.authtoken.models import Token, TokenProxy
from reviews.models import Review
from rooms.models import Amenity, Room
from users.models import User
from wishlists.models import Wishlist
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery
Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.31.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: User.objects.all()
Out[1]: <QuerySet []>
```
