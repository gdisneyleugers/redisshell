__author__ = 'gregorydisney'

while True:
    rediscmd = ['get', 'set', 'keys', 'connect', 'help', 'flush', 'reload', 'exit']
    cmd = raw_input("Redis-Shell=> ")

    def Reload(self):
        self = RKeyClient
        import Reloader
        Reloader

    if cmd == 'get':
        import RGet
        RGet.RedisGet()
        import Reloader
        Reloader


    if cmd == 'keys':
        import  RKeys
        RKeys.RedisKeys()
        import Reloader
        Reloader

    if cmd == 'connect':
        import RedisController
        RedisController.RedisConnect()
        print RedisController.RedisConnect.r
        import Reloader
        Reloader

    if cmd == 'set':
        import RSet
        RSet.RedisSet()
        import Reloader
        Reloader

    if cmd == 'exit':
        print "Exiting"
        quit()

    if cmd == 'help':
        print "Options: \n"
        print "get: Query key in DB\n"
        print "set: Set key in DB\n"
        print "keys: Show all keys in DB\n"
        print "connect: Connect to Redis DB\n"
        print "flush: Flush Redis DB"
        import Reloader
        Reloader

    if cmd == 'reload':
        print "Reloading Shell"
        import Reloader
        Reloader

    if cmd == 'flush':
        import RedisController
        db = RedisController.RedisConnect.r
        db.flushall()
        print "DB flushed"
        import Reloader
        Reloader

    if cmd not in rediscmd:
        for a in enumerate(rediscmd):
            print "Command is: " + cmd + "\n"
            print "Allowed comand: " + ''.join(str(a)) + "\n"
            import Reloader

if __name__ == '__main__':
    import RKeyClient