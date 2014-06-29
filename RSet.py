__author__ = 'gregorydisney'
from RedisController import RedisConnect
db = RedisConnect.r
class RedisSet:
    name = raw_input("Name: ")
    value = raw_input("Value: ")
    db.set(name,value)
    import RKeyClient
    RKeyClient
if __name__ == '__main__':
    import RKeyClient
    RKeyClient