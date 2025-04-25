# 🌈 Pretty Admin – Tailwind-powered Django Admin Skin
[![PyPI version](https://badge.fury.io/py/pretty-admin.svg)](https://badge.fury.io/py/pretty-admin)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



**Pretty Admin** is a beautiful, customizable Django admin interface built with Tailwind CSS. It enhances the default Django admin with modern UI and responsive design.

> ⚠️ This package is under active development. Full-featured updates will be released soon. Stay tuned!

---

## 🚀 Features

- 🎨 Beautiful Tailwind-based UI
- 🌙 Light/Dark theme toggle
- 📱 Fully responsive layout
- ⚡ Minimal setup, plug & play

---

## 📦 Installation

You can install Pretty Admin directly from PyPI:

```bash
pip install pretty-admin
```

## ⚙️ Setup Instructions

Follow these steps to integrate `pretty_admin` into your Django project:

### 1. Add `pretty_admin` to `INSTALLED_APPS`

Make sure it's placed **before** `django.contrib.admin`:

```python
# settings.py

INSTALLED_APPS = [
    'pretty_admin',              # 👈 Add this at the top before `django.contrib.admin`
    'django.contrib.admin',
    'django.contrib.auth',
    ...
]
```



### 2. `Set STATIC_URL` and `STATIC_ROOT`
Add this to your settings.py if not already set:

```
# settings.py

import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### 3. Run collectstatic
To gather all static files (including Pretty Admin's Tailwind assets), run:


```
python manage.py collectstatic
```
This will generate a staticfiles/ folder containing all necessary static files.


### 4. Start your server

```
python manage.py runserver
```
## Visit your admin panel at:
```
http://127.0.0.1:8000/admin/
```
You should now see the beautiful Pretty Admin UI ✨
