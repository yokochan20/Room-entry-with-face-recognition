from mprpc import RPCClient

def callraspi():
    client = RPCClient("133.27.171.245", 6000)
    print (client.call('unlock_key'))

