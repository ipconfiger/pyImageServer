import os

DEBUG=True
AUTH_KEY="alexander is a good guy"
HOST="127.0.0.1"
USERNAME="su"
PASSWORD="123456"
DATABASE="img"
HOLDER="saestore"
ALLOWED_EXT=['jpg','jpeg','gif','png']
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
UPFILE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, 'upfile'))
SAEDOMAIN="img1"