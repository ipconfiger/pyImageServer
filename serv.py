#! /usr/bin/python
#coding=utf8
import os
import time
import settings

from StringIO import StringIO
from utils import *
from flask import Flask,request,send_file


app = Flask(__name__)
app.config.from_object(settings)

get_file,dump_file=load_data_access(settings.HOLDER)

@app.route("/ping")
def ping():
    return "it works!"

@app.route("/",methods=["POST"])
def upload_file():
    sizes=request.form.get("sizes","")
    file_object=request.files["thefile"]
    file_name=file_object.filename
    ext_name=get_ext_name(file_name)
    if ext_name.lower() not in settings.ALLOWED_EXT:
        return error_rep(request.form,"extention %s not allowed"%ext_name)
    new_filename_prefix=create_filename()
    new_filename="%s.%s"%(new_filename_prefix,ext_name)
    image_data=file_object.read()
    dump_file(new_filename,image_data)
    if not sizes:
        return success_rep(request.form,new_filename)
    for k,v in json.loads(sizes).iteritems():
        w,h=map(int,v.split("x"))
        thumb=change_size(ext_name,image_data,w,h)
        thumb_filename="%s_%s.%s"%(new_filename_prefix,k,ext_name)
        dump_file(thumb_filename,thumb)
    return success_rep(request.form,new_filename)



@app.route("/<img_name>",methods=['GET'])
def view_img(img_name):
    try:
        is_file,f=get_file(img_name)
        if is_file:
            return send_file(StringIO(f))
        else:
            return send_file(f)
    except:
        return "File not found",404

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)