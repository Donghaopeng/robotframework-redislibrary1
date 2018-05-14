# -*- coding: utf-8 -*-
import redis
from robot.api import deco
from robot.api import logger

from version import VERSION

__author__ = 'donghp'
__email__ = '1173619682@qq.com'
__version__ = VERSION


class RedisLibraryKeywords(object):

    @deco.keyword('Connect To Redis')
    def connect_to_redis(self, redis_host, redis_port=6379, db=0, redis_password=None):
        # pragma: no cover
        """Connect to the Redis server.

        Arguments:
            - redis_host: hostname or IP address of the Redis server.
            - redis_port: Redis port number (default=6379)
            - db: Redis keyspace number (default=0)
            - redis_password: Redis auth.

        Return redis connection object

        Examples:
        | ${redis_conn}=   | Connect To Redis |  redis-dev.com | 6379 | 0 | 123456 |
        """
        try:
            pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=db,
                                        password=redis_password, decode_responses=True)
            redis_conn = redis.Redis(connection_pool=pool)
        except Exception as ex:
            logger.error(str(ex))
            raise Exception(str(ex))
        return redis_conn

    # @deco.keyword('Append To Redis')
    # def append_to_redis(self, redis_conn, key, value):
    #     """ Append data to Redis. If key doesn't exist, create it with value.
    #         Return the new length of the value at key.
    #
    #     Arguments:
    #         - redis_conn: Redis connection object.
    #         - key: String key.
    #         - value: String value.
    #
    #     Examples:
    #     | ${data}=   | Append To Redis |  ${redis_conn} | BARCODE|1234567890 | ${data} |
    #
    #     """
    #     return redis_conn.lpush(key, value)

    @deco.keyword('Set To Redis List')
    def set_to_redis_list(self, redis_conn, objects, data):
        """ Set data to Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: objects list to find.
            - data: data in list.

        Examples:
        | ${data}=   | Set To Redis List |  ${redis_conn} | BARCODE|1234567890 | ${data}  |
        """
        return redis_conn.lpush(objects, data)

    @deco.keyword('Get From Redis List')
    def get_from_redis_list(self, redis_conn, objects, start, end):
        """ Get cached data from Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: objects to find.
            - start: list start index.
            - end: list end index.

        Examples:
        | Set To Redis List |  ${redis_conn} | objects | one  |
        | Set To Redis List |  ${redis_conn} | objects | two  |
        | ${data}=   | Get From Redis List|  ${redis_conn} | objects | 0 | 1 |
        """
        return redis_conn.lrange(objects, start, end)

    @deco.keyword('Set To Redis String')
    def set_to_redis_string(self, redis_conn, key, data):
        """ Set data to Redis

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.
            - data: String data

        Examples:
        | ${data}=   | Set To Redis String |  ${redis_conn} | BARCODE|1234567890 | ${data}  |
        """
        return redis_conn.set(key, data)

    @deco.keyword('Get From Redis String')
    def get_from_redis_string(self, redis_conn, key):
        """ Get cached data from Redis

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.

        Examples:
        | ${data}=   | Set To Redis |  ${redis_conn} | BARCODE|1234567890 | ${data}  |
        | ${data}=   | Get From Redis String |  ${redis_conn} | BARCODE|1234567890 |
        """
        return redis_conn.get(key)

    @deco.keyword('Set To Redis Hash')
    def set_to_redis_hash(self, redis_conn, objects, key, data):
        """ Set data to Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: hash objects.
            - key: String keyword to find.
            - data: String data.

        Examples:
        | Set To Redis Hash |  ${redis_conn} | user:info | name | jack |
        | Set To Redis Hash |  ${redis_conn} | user:info | age | 10 |
        """
        return redis_conn.hset(objects, key, data)

    @deco.keyword('Get From Redis Hash')
    def get_from_redis_hash(self, redis_conn, objects):
        """ Get cached data from Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: objects class.

        Examples:
        | ${data}=   | Get From Redis Hash |  ${redis_conn} | user:info |
        """
        return redis_conn.hgetall(objects)

    @deco.keyword('Set To Redis Set')
    def set_to_redis_set(self, redis_conn, objects, data):
        """ Set data to Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: set objects.
            - data: set data.

        Examples:
        | Set To Redis Set |  ${redis_conn} | set | name |
        | Set To Redis Hash |  ${redis_conn} | set | age |
        """
        return redis_conn.sadd(objects, data)

    @deco.keyword('Get From Redis Set')
    def get_from_redis_set(self, redis_conn, objects):
        """ Get cached data from Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: objects class.

        Examples:
        | ${data}=   | Get From Redis Set |  ${redis_conn} | set |
        """
        return redis_conn.smembers(objects)

    @deco.keyword('Set To Redis Sorted Set')
    def set_to_redis_sorted_set(self, redis_conn, objects, data, index):
        """ Set data to Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: sorted set objects.
            - key: sorted set key.
            - data: sorted set data.

        Examples:
        | Set To Redis Sorted Set |  ${redis_conn} | user:info | {'name':'jack'} | 1 |
        | Set To Redis Sorted Set |  ${redis_conn} | user:info | {'age':10} | 2 |
        | Set To Redis Sorted Set |  ${redis_conn} | user:info | {'phone':123456} | 4 |
        | Set To Redis Sorted Set |  ${redis_conn} | user:info | {'email':'123456@qq.com'} | 3 |
        """
        return redis_conn.zadd(objects, data, index)

    @deco.keyword('Get From Redis Sorted Set')
    def get_from_redis_sorted_set(self, redis_conn, objects, start, end):
        """ Get cached data from Redis

        Arguments:
            - redis_conn: Redis connection object
            - objects: objects class.
            - start: Set start.
            - end: Set end.

        Examples:
        | Set To Redis Sorted Set |  ${redis_conn} | user:info:1 | {'name':'jack'} | 1 |
        | Set To Redis Sorted Set |  ${redis_conn} | user:info:1 | {'age':10} | 2 |
        | Set To Redis Sorted Set |  ${redis_conn} | user:info:1 | {'phone':123456} | 4 |
        | Set To Redis Sorted Set |  ${redis_conn} | user:info:1 | {'email':'123456@qq.com'} | 3 |
        | ${data}=   | Get From Redis Sorted Set |  ${redis_conn} | user:info:1 | 1 | 10 |
        """
        return redis_conn.zrange(objects, start, end)

    @deco.keyword('Flush All')
    def flush_all(self, redis_conn):
        """ Delete all keys from Redis

        Arguments:
            - redis_conn: Redis connection object

        Examples:
        | ${data}=   | Flush All |  ${redis_conn} |
        """
        return redis_conn.flushall()

    @deco.keyword('Expire Data From Redis')
    def expire_data_from_redis(self, redis_conn, key, expire_time=0):
        """ Expire items from Redis

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.
            - expire_time: waiting time to expire data (Default = expire now)

        Examples:
        | Expire Data From Redis |  ${redis_conn} | BARCODE|1234567890 |
        """
        redis_conn.expire(key, expire_time)

    @deco.keyword('Get Time To Live In Redis')
    def get_time_to_live_in_redis(self, redis_conn, key):
        """ Return time to live in Redis (minutes)

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.

        Examples:
        | Expire Data From Redis |  ${redis_conn} | BARCODE|1234567890 |
        """
        return redis_conn.ttl(key) / 60

    @deco.keyword('Delete From Redis')
    def delete_from_redis(self, redis_conn, key):
        """ Delete data from Redis

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.

        Examples:
        | Delete From Redis |  ${redis_conn} | BARCODE|1234567890 |
        """
        return redis_conn.delete(key)

    @deco.keyword('Redis Key Should Be Exist')
    def check_if_key_exits(self, redis_conn, key):
        """ Keyword will fail if specify key doesn't exist in Redis

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.

        Examples:
        | ${is_exist}= | Check If Key Exists | ${redis_conn} | BARCODE|1234567890 |
        """
        if redis_conn.exists(key) is False:
            logger.error("Key " + key +" doesn't exist in Redis.")
            raise AssertionError

if __name__ == '__main__':
    r = RedisLibraryKeywords()
    conn = r.connect_to_redis(redis_host='127.0.0.1', redis_port=6379, db=0)

    # r.set_to_redis_string(conn, 'SWCACHE:Banner:1', 'one')
    # print r.get_from_redis_string(conn, 'SWCACHE:Banner:1')

    # r.set_to_redis_list(conn, 'SWCACHE:Banner:3', 'one')
    # r.set_to_redis_list(conn, 'SWCACHE:Banner:3', 'two')
    # print r.get_from_redis_list(conn, 'SWCACHE:Banner:3', start=0, end=1)

    # r.set_to_redis_hash(conn, 'user:info', 'name', 'jack')
    # r.set_to_redis_hash(conn, 'user:info', 'age', '10')
    # print r.get_from_redis_hash(conn, 'user:info')

    # r.set_to_redis_set(conn, 'set:user1', 'xiaoming')
    # r.set_to_redis_set(conn, 'set:user2', 'xiaohong')
    # print r.get_from_redis_set(conn, 'set:user1')

    r.set_to_redis_sorted_set(conn, 'user:info:1', {'name': 'Jack'}, 1)
    r.set_to_redis_sorted_set(conn, 'user:info:1', {'age': 10}, 2)
    r.set_to_redis_sorted_set(conn, 'user:info:1', {'phone': 123456}, 4)
    r.set_to_redis_sorted_set(conn, 'user:info:1', {'email': '123456@qq.com'}, 3)
    print r.get_from_redis_sorted_set(conn, 'user:info:1', 0, 10)

