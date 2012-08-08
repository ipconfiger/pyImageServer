import os

DEBUG=True
HOLDER="saestore"
ALLOWED_EXT=['jpg','jpeg','gif','png']
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
UPFILE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, 'upfile'))
SAEDOMAIN="img1"