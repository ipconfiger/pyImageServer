#coding=utf8
import pybcs
import logging

pybcs.init_logging(logging.INFO)

AK = ''           #请改为你的AK
SK = ''         #请改为你的SK

BUCKET='myimage1'

bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK)

def dump_file(filename,file_obj):
    o = b.object('/%s'%filename)
    o.put(file_obj)

def read_file(filename):
    o = b.object('/%s'%filename)
    return o.get()