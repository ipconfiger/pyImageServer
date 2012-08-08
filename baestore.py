#coding=utf8
import pybcs
import logging
from tempfile import NamedTemporaryFile

#pybcs.init_logging(logging.INFO)

AK = ''           #请改为你的AK
SK = ''         #请改为你的SK

BUCKET='myimage1'

bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK)

def dump_file(filename,file_obj):
    b = bcs.bucket(BUCKET)
    with NamedTemporaryFile() as f:
        o = b.object('/%s'%filename)
        o.put_file(f.name)

def read_file(filename):
    b = bcs.bucket(BUCKET)
    with NamedTemporaryFile() as f:
        o = b.object('/%s'%filename)
        o.get_to_file(f.name)
        return True,f.read()
