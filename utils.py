#coding=utf8
import time
import json
import settings
try:
    import Image
except:
    from PIL import Image

def create_filename():
    seed=list("1234567890qwertyuiopasdfghjklzxcvbnm~-*")
    cpt = code = int(time.time()*1000)
    selected=[]
    cl=len(seed)
    while True:
        rest = cpt / cl
        mod = cpt % cl
        if rest <= cl:
            selected.append(rest)
            break
        else:
            selected.append(mod)
            cpt = rest
    return "".join([seed[n] for n in selected])

def load_data_access(holder_name):
    if holder_name:
        holder=__import__(holder_name.lower())
        return holder.read_file,holder.dump_file
    return read_file,dump_file

def success_rep(form,filename):
    success=form.get("on_success","")
    if success:
        success=success.replace("$status","true")
        success=success.replace("$filename",filename)
        return success
    return json.dumps(dict(status=True,filename=filename))

def error_rep(form,info):
    error=form.get("on_error","")
    if error:
        error=error.replace("$status","false")
        error=error.replace("$info",info)
        return error
    return json.dumps(dict(status=False,info=info))

def dump_file(filename,file_obj):
    file_path="%s/%s"%(settings.UPFILE_ROOT,filename)
    with open(file_path,'wb') as f:
        f.write(file_obj)

def read_file(filename):
    file_path="%s/%s"%(settings.UPFILE_ROOT,filename)
    return False,file_path

def get_ext_name(filename):
    return filename.split(".")[-1]

def change_size(ext,img_data,tar_w,tar_h):
    from StringIO import StringIO
    img=Image.open(StringIO(img_data))
    w,h=img.size
    resize=True
    if not tar_h and w<=tar_w:
        resize=False
    if not tar_w and h<=tar_w:
        resize=False
    if w<=tar_w and h<=tar_h:
        resize=False
    if not resize:
        return img_data
    if tar_w<w and tar_h==0:
        tar_h=int(w*1.0/tar_w*h)
    if tar_h<h and tar_w==0:
        tar_w=int(h*1.0/tar_h*w)
    img.thumbnail((tar_w,tar_w),Image.ANTIALIAS)
    tmpf=StringIO()
    img.save(tmpf,format=img.format)
    tmpf.seek(0)
    return tmpf.read()

