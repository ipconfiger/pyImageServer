#coding=utf8
from google.appengine.ext import db

class ImgEntity(db.Model):
    filename = db.StringProperty(required=True)
    filedata= db.Blob()


def dump_file(filename,file_obj):
    img=ImgEntity(key_name=filename)
    img.filename=filename
    img.filedata=file_obj
    img.put()

def read_file(filename):
    img=ImgEntity.get(filename)
    return True,img.filedata