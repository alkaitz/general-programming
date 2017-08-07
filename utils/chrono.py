'''
Created on Aug 2, 2017

@author: alkaitz
'''                                               

import time

def chrono(f):

    def _f(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print 'Called:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts)
        return result

    return _f