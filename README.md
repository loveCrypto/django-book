
__Multiple Environments__

touch superlists/settings/__init__.py

__For development use, do:__
echo "from .development import *" >> superlists/settings/__init__.py

__For production use, do:__
echo "from .production import *" >> superlists/settings/__init__.py
