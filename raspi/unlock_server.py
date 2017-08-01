from gevent.server import StreamServer
from mprpc import RPCServer
from servo import unlock
import time
from datetime import datetime

class SumServer(RPCServer):    
  def unlock_key(self):
    print "Unlock"
    unlock()
    print datetime.now()
    time.sleep(3)
    

server = StreamServer(('133.27.171.245', 6000), SumServer())
server.serve_forever()
