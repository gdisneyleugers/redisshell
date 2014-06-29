__author__ = 'gregorydisney'
import redis


def pattern(self):
    pass

class RedisKeys:
            r = redis.StrictRedis()
            keys = r.keys("*")
            a = ''.join(keys)
            for i,elem in enumerate(keys):
                print elem + "\n"
if __name__ == '__main__':
    import RKeyClient