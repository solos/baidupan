
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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_version'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
