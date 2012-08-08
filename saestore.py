import sae.storage
import settings

def dump_file(filename,file_obj):
    s = sae.storage.Client()
    ob = sae.storage.Object(file_obj)
    s.put(settings.SAEDOMAIN, filename, ob)


def read_file(filename):
    s = sae.storage.Client()
    ob = s.get(settings.SAEDOMAIN, filename)
    return True,ob.data
