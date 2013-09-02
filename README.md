# baidupan

#关于

baidupan是一个百度盘(http://pan.baidu.com)API的Python SDK.

#使用方法

    from baidupan.baidupan import BaiduPan

    if __name__ == "__main__":
        access_token = ''
        disk = BaiduPan(access_token)
        print disk.quota()
        print disk.upload('hello', path='/apps/appname/hello')
