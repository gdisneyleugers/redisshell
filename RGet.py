__author__ = 'gregorydisney'
from RedisController import RedisConnect
db = RedisConnect.r

class RedisGet:
        n = raw_input("Name: ")
        a = db.get(n)
        print a

if __name__ == '__main__':
    import RKeyClient