#!/usr/bin/env python
#coding=utf-8

import requests


class BaiduPan(object):
    base_url = 'https://pcs.baidu.com/rest/2.0/pcs/'
    method = ''
    params = {}
    payload = {}
    files = None

    def __init__(self, access_token=''):
        self.access_token = access_token

    def _request(self, **kw):
        if 'file' in kw:
            self.files = {'files': (kw['filename'], kw['file'])}
            del kw['file']
        if 'from_path' in kw:
            kw['from'] = kw['from_path']
            del kw['from_path']
        for keyword in ['content_length',
                        'content_md5',
                        'slice_md5',
                        'content_crc32']:
            try:
                kw[keyword.replace('_', '-')] = kw[keyword]
                del kw[keyword]
            except KeyError:
                continue

        self.params.update(method=self.method)
        self.params.update(access_token=self.access_token)
        self.params.update(kw)
        self.url = ''.join([self.base_url, self.urlpath])
        if self._method == 'GET':
            try:
                r = requests.get(self.url, params=self.params)
                return r.content
            except Exception, e:
                print e
                return None
        elif self._method == 'POST':
            if self.files:
                try:
                    r = requests.post(self.url,
                                      files=self.files,
                                      params=self.params)
                    return r.content
                except Exception, e:
                    print e
                    return None
            else:
                if self.payload:
                    try:
                        r = requests.post(self.url,
                                          data=self.payload,
                                          params=self.params)
                        return r.content
                    except Exception, e:
                        print e
                        return None
                else:
                    try:
                        r = requests.post(self.url, params=self.params)
                        return r.content
                    except Exception, e:
                        print e
                        return None
        else:
            raise Exception("Method Not Allowed: %s" % self._method)

    def quota(self, **kw):
        self.urlpath = 'quota'
        self.method = 'info'
        self._method = 'GET'
        return self._request(**kw)

    def upload(self, filename, **kw):
        self.urlpath = 'file'
        self.method = 'upload'
        self._method = 'POST'
        try:
            f = open(filename, 'rb').read()
        except Exception, e:
            print e
            raise
        return self._request(filename=filename, file=f, **kw)

    def merge(self, path, param, **kw):
        self.urlpath = 'file'
        self.method = 'createsuperfile'
        self._method = 'POST'
        return self._request(path=path, param=param, **kw)

    def download(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'download'
        self._method = 'GET'
        return self._request(path=path, **kw)

    def mkdir(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'mkdir'
        self._method = 'POST'
        return self._request(path=path, **kw)

    def meta(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'meta'
        self._method = 'POST'
        return self._request(path=path, **kw)

    def mmeta(self, param, **kw):
        self.urlpath = 'file'
        self.method = 'meta'
        self._method = 'POST'
        return self._request(param=param, **kw)

    def ls(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'list'
        self._method = 'POST'
        return self._request(path=path, **kw)

    def mv(self, from_path, to_path, **kw):
        self.urlpath = 'file'
        self.method = 'move'
        self._method = 'POST'
        return self._request(from_path=from_path, to=to_path, **kw)

    def mmv(self, param, **kw):
        self.urlpath = 'file'
        self.method = 'move'
        self._method = 'POST'
        return self._request(param=param, **kw)

    def cp(self, from_path, to_path, **kw):
        self.urlpath = 'file'
        self.method = 'copy'
        self._method = 'POST'
        return self._request(from_path=from_path, to=to_path, **kw)

    def mcp(self, param, **kw):
        self.urlpath = 'file'
        self.method = 'copy'
        self._method = 'POST'
        return self._request(param=param, **kw)

    def rm(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'delete'
        self._method = 'POST'
        return self._request(path=path, **kw)

    def mrm(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'delete'
        self._method = 'POST'
        return self._request(path=path, **kw)

    def grep(self, word, path, **kw):
        self.urlpath = 'file'
        self.method = 'search'
        self._method = 'POST'
        return self._request(wd=word, path=path, **kw)

    def search(self, word, path, **kw):
        self.urlpath = 'file'
        self.method = 'search'
        self._method = 'POST'
        return self._request(wd=word, path=path, **kw)

    def thumb(self, path, height, width, **kw):
        self.urlpath = 'thumbnail'
        self.method = 'generate'
        self._method = 'GET'
        return self._request(path=path, height=height, width=width, **kw)

    def diff(self, cursor='null', **kw):
        self.urlpath = 'file'
        self.method = 'diff'
        self._method = 'GET'
        return self._request(cursor=cursor, **kw)

    def streaming(self, path, type='M3U8_480_360', **kw):
        self.urlpath = 'file'
        self.method = 'streaming'
        self._method = 'GET'
        return self._request(path=path, type=type, **kw)

    def stream(self, type, **kw):
        self.urlpath = 'stream'
        self.method = 'list'
        self._method = 'GET'
        return self._request(type=type, **kw)

    def downstream(self, path, **kw):
        self.urlpath = 'file'
        self.method = 'download'
        self._method = 'GET'
        return self._request(path=path, **kw)

    def rapidsend(self, path, content_length,
                  content_md5, slice_md5, content_crc32, **kw):
        self.urlpath = 'file'
        self.method = 'rapidupload'
        self._method = 'POST'
        return self._request(path=path, content_length=content_length,
                             content_md5=content_md5, slice_md5=slice_md5,
                             content_crc32=content_crc32, **kw)

    def add_task(self, url, path, **kw):
        self.urlpath = 'services/cloud_dl'
        self.method = 'add_task'
        self._method = 'POST'
        return self._request(source_url=url, save_path=path, **kw)

    def query_task(self, task_ids, op_type, **kw):
        self.urlpath = 'services/cloud_dl'
        self.method = 'query_task'
        self._method = 'POST'
        return self._request(task_ids=task_ids, op_type=op_type, **kw)

    def list_task(self, **kw):
        self.urlpath = 'services/cloud_dl'
        self.method = 'list_task'
        self._method = 'POST'
        return self._request(**kw)

    def cancel_task(self, task_id, **kw):
        self.urlpath = 'services/cloud_dl'
        self.method = 'cancel_task'
        self._method = 'POST'
        return self._request(task_id=task_id, **kw)

    def listrecycle(self, **kw):
        self.urlpath = 'file'
        self.method = 'listrecycle'
        self._method = 'GET'
        return self._request(**kw)

    def restore(self, fs_id, **kw):
        self.urlpath = 'file'
        self.method = 'restore'
        self._method = 'POST'
        return self._request(fs_id=fs_id, **kw)

    def mrestore(self, param, **kw):
        self.urlpath = 'file'
        self.method = 'restore'
        self._method = 'POST'
        return self._request(param=param, **kw)

    def emptyrecycle(self, **kw):
        self.urlpath = 'file'
        self.method = 'delete'
        self._method = 'POST'
        return self._request(type='recycle', **kw)
