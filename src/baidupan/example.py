#!/usr/bin/env python
#coding=utf-8

import json
from baidupan import BaiduPan

if __name__ == '__main__':
    access_token = ''
    disk = BaiduPan(access_token)
    #quota
    print disk.quota()
    #upload
    print disk.upload('hello', path='/apps/appname/hello.txt')
    #merge
    '''
    def merge(self, path, param, **kw):
        self.urlpath = 'file'
        self.method = 'createsuperfile'
        self._method = 'POST'
        return self._request(path=path, param=param, **kw)
    '''
    param = ''
    print disk.merge('/apps/appname/hello.txt', param=param)
    #download
    print disk.download(path='/apps/appname/hello.txt')
    #mkdir
    print disk.mkdir('/apps/appname/dirname')
    #meta
    print disk.meta('/apps/appname/filename')
    #mmeta
    print disk.mmeta(json.dumps({"list": [{"path": "/apps/appname/"}]}))
    #ls
    print disk.ls("/apps/appname/")
    #mv
    print disk.mv("/apps/appname/hello.txt", "/apps/appname/hello.txt.bak")
    #mmv
    par = {"list": [{"from": "/apps/appname/hello.txt.bak",
                     "to": "/apps/appname/hello.txt.bak.bak"},
                    {"from": "/apps/appname/dirs",
                     "to": "/apps/appname/dirsbak"}]}
    print disk.mmv(json.dumps(par))
    #cp
    print disk.cp("/apps/appname/hello.txt.bak", "/apps/appname/hello.txt")
    #mcp
    par = {"list": [{"path": "/apps/appname/hello.txt1"},
                    {"path": "/apps/appname/dirs"}]}
    print disk.mcp(json.dumps(par))
    #rm
    print disk.rm('/apps/appname/hello.txt.bak')
    #mrm
    par = {"list": [{"path": "/apps/appname/hello.txt1"},
                    {"path": "/apps/appname/dirs"}]}
    print disk.mrm(json.dumps(par))
    #search
    print disk.grep('hello', '/apps/appname/')
    print disk.search('hello', '/apps/appname/')
    #thumb
    print disk.thumb('/apps/appname/1.png', 100, 100)
    #diff
    print disk.diff()
    #streaming
    print disk.streaming('/apps/appname/1.mkv')
    #stream
    print disk.stream(type='doc')
    #downstream
    print disk.downstream('/apps/appname/1.png')
    #rapidsend
    #print disk.rapidsend('/home/solos/1.png', content_length,
    #                     content_md5, slice_md5, content_crc32)
    #add_task
    print disk.add_task('http://www.baidu.com', '/apps/appname/1.html')
    #query_task
    print disk.query_task('3665778', 1)
    #list_task
    print disk.list_task()
    #cancel_task
    print disk.cancel_task('3665778')
    #listrecycle
    print disk.listrecycle()
    #restore
    print disk.restore('4045501009')
    #mrestore
    par = {"list": [{"fs_id": 2263172857}, {"fs_id": 4045501009}]}
    print disk.mrestore(json.dumps(par))
    #emptyrecycle
    print disk.emptyrecycle()
