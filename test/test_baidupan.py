
# -*- coding:utf-8 -*-

import sys
sys.path.append('../src/')

from baidupan.baidupan import BaiduPan
from baidupan import baidupan
import unittest
from mock import patch, call


class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        self.baidupan = BaiduPan()
        self.request_patcher = patch("baidupan.baidupan.BaiduPan._request")
        self.mock_request = self.request_patcher.start()

    def tearDown(self):
        self.request_patcher.stop()

    def test_version(self):
        self.assertIsNotNone(baidupan.__version__, '0.0.1')

    @patch("__builtin__.open")
    def test_upload(self, mock_open):
        mock_open.return_value.read.return_value = "hulahoop"
        self.baidupan.upload({"keyword": "hulahoop"})
        self.assertEqual(self.mock_request.call_args,
                         call(file='hulahoop',
                              filename={'keyword': 'hulahoop'}))

    def test_merge(self):
        self.baidupan.merge('path', 'param', keyword="hulahoop")
        self.assertEqual(self.mock_request.call_args, call(keyword='hulahoop',
                                                           param='param',
                                                           path='path'))

    def test_similar_path_functions(self):
        for method in ('download', 'mkdir', 'meta'):
            getattr(self.baidupan, method)('path', keyword='hulahoop')
            self.assertEqual(self.mock_request.call_args,
                         call(keyword='hulahoop', path='path'))

    def test_similar_param_functions(self):
        for method in ('mmv', 'mmeta'):
            getattr(self.baidupan, method)('param', keyword='hulahoop')
            self.assertEqual(self.mock_request.call_args,
                         call(keyword='hulahoop', param='param'))

    def test_mv_cp(self):
        for method in ('mv', 'cp'):
            getattr(self.baidupan, method)('from_path',
                                           'to_path',
                                           keyword='hulahoop')
            self.assertEqual(self.mock_request.call_args,
                         call(keyword='hulahoop',
                              from_path='from_path',
                              to='to_path'))

    @patch("requests.post")
    @patch("requests.get")
    def test_private_request(self, mock_get, mock_post):
        # Disable the earlier patch on _request to properly test it.
        self.request_patcher.stop()
        baidupan = BaiduPan()
        baidupan.base_url = 'base_url'
        baidupan.urlpath = 'urlpath'
        baidupan.method = 'method'
        baidupan.access_token = 'access_token'
        baidupan._method = "GET"
        mock_get.return_value.content = 'hulahoop'
        result = baidupan._request(headers='headers',
                                   file='file1',
                                   filename='file1',
                                   from_path='from_path',
                                   content_length='content_length',
                                   content_md5='content_md5',
                                   slice_md5='slice_md5',
                                   content_crc32='content_crc32')
        self.assertTrue(mock_get.call_args, call('base_urlurlpath', headers='headers',
                                                 params={'slice-md5': 'slice_md5',
                                                         'content-length': 'content_length',
                                                         'from': 'from_path',
                                                         'access_token': 'access_token',
                                                         'filename': 'file1',
                                                         'content-crc32': 'content_crc32',
                                                         'content-md5': 'content_md5',
                                                         'method': 'method'}))
        self.assertEqual(result, 'hulahoop')
        mock_post.return_value.content = 'hulahoop'
        baidupan._method = "POST"
        result_post = baidupan._request(headers='headers',
                                        file='file1',
                                        filename='file1',
                                        from_path='from_path',
                                        content_length='content_length',
                                        content_md5='content_md5',
                                        slice_md5='slice_md5',
                                        content_crc32='content_crc32')
        self.assertEqual(mock_post.call_args, call('base_urlurlpath', files={'files': ('file1', 'file1')},
                                                   headers='headers',
                                                   params={'slice-md5': 'slice_md5',
                                                           'content-length': 'content_length',
                                                           'from': 'from_path',
                                                           'access_token': 'access_token',
                                                           'filename': 'file1',
                                                           'content-crc32': 'content_crc32',
                                                           'content-md5': 'content_md5',
                                                           'method': 'method'}))
        self.assertEqual(result_post, 'hulahoop')
        baidupan.payload = 'payload'
        baidupan.files = None
        mock_post.reset_mock()
        result_payload = baidupan._request(headers='headers')
        self.assertEqual(mock_post.call_args, call('base_urlurlpath', data='payload',
                                                   headers='headers',
                                                   params={'slice-md5': 'slice_md5',
                                                           'content-length': 'content_length',
                                                           'from': 'from_path',
                                                           'access_token': 'access_token',
                                                           'filename': 'file1',
                                                           'content-crc32': 'content_crc32',
                                                           'content-md5': 'content_md5',
                                                           'method': 'method'}))
        self.assertEqual(result_payload, 'hulahoop')
        baidupan._method = 'not allowed'
        with self.assertRaises(Exception):
            baidupan._request(headers="headers")
        self.request_patcher.start()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_version'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
