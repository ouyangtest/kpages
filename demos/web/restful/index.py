# -*- coding:utf-8 -*- 
"""
    index action
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url,ContextHandler,LogicContext,get_context,service_async

@url(r"/")
class IndexHandler(ContextHandler):
    def get(self):
        #import pdb;pdb.set_trace()

        print self.session('demokey',dict(abcdeed='deee',dd='dssd'))

        with LogicContext():
            service_async('demofun',dict(data='sasa'))
        print self.session('demokey')
        self.write('hi kpages')

@url(r'/list')
class ListHandler(ContextHandler):
    ''' demo for motor pymongo '''
    @gen.coroutine
    def get(self):
        ses = get_context().get_aync_mongo('session')['session']
        lst = yield ses.find().to_list(100)
        data = dict(data = lst)
        with LogicContext(): 
            service_async('demofun',data)

        self.write('ok')