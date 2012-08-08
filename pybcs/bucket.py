#!/usr/bin/env python
#coding:utf8

import time
import urllib

import common 
from httpc import *
from object import Object, Superfile

try:
    import json
except:
    import simplejson as json

class Bucket:
    ''' 
     bucket.create/ bucket.delete / bucket.setacl 
     建议到yun.baidu.com 操作，create 后还需要设置quota等才能使用.
    '''
    def __init__(self, bcs, bucket_name):
        self.bcs = bcs
        self.host = bcs.host
        self.ak = bcs.ak 
        self.sk = bcs.sk 
        self.bucket_name = bucket_name
        self.sleep = 1 # sleep 1 second after upload

        self.put_url=bcs.sign('PUT', bucket_name, '/')
        self.get_url=bcs.sign('GET', bucket_name, '/')
        self.head_url=bcs.sign('HEAD', bucket_name, '/')
        self.del_url=bcs.sign('DELETE', bucket_name, '/')
        self.c = self.bcs.c

    def __str__(self):
        return '%s/%s' % (self.host, self.bucket_name)

    def object(self, object_name):
        return Object(self, object_name)

    def superfile(self, object_name, sub_object_list):
        return Superfile(self, object_name, sub_object_list)

    @network
    def create(self):
        return self.c.put(self.put_url, '')

    @network
    def delete(self):
        return self.c.delete(self.del_url)

    @network
    def list_objects_raw(self, prefix='', start=0, limit=100):
        ''' return raw json '''
        params = { 'start': start,
                  'limit': limit,
                 }
        if prefix:
            params.update ({'prefix': prefix})

        url = self.get_url + '&' + urllib.urlencode(params)

        rst = self.c.get(url)
        j = json.loads( rst['body'] )
        return j['object_list']

    @network
    def list_objects(self, prefix='', start=0, limit=100):
        '''return parsed object list'''
        lst = self.list_objects_raw(prefix, start, limit)
        return [self.object(o['object'].encode('utf-8')) 
                for o in lst] 
        
    #acl : string like: {statements':[{'user':['joe'],'resource':['bucket/object'],'action':['*'],'effect':'allow'}]}
    @network
    def set_acl(self, acl):
        return self.c.put(self.put_url+'&acl=1', acl)

    @network
    def get_acl(self):
        return self.c.get(self.get_url+'&acl=1')

    @network
    def make_public(self):
        acl = '{"statements":[{"action":["*"],"effect":"allow","resource":["%s\\/"],"user":["*"]}]}' % (self.bucket_name)
        self.set_acl(acl)

    @network
    def make_private_to_user(self, user):
        acl = '{"statements":[{"action":["*"],"effect":"allow","resource":["%s\\/"],"user":["%s"]}]}' % (self.bucket_name, user)
        self.set_acl(acl)

    @network
    def enable_logging(self, target_bucket, target_prefix='', headers=None): 
        pass

    def disable_logging(self, target_bucket, target_prefix='', headers=None): 
        pass



