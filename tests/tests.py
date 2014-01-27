from nose.tools import assert_raises

from redisq import RedisqClient, Task


def test():
    #test correct composition of task JSON
    data = '{"datetime": "2014-01-25T16:00:51.735405"}'
    t = Task(data, task_time=1390663231)
    assert t.get_json() == '[0, 1390663231, {"datetime": "2014-01-25T16:00:51.735405"}, 0]'

    #test RedisClient needs queuname
    assert_raises(TypeError, RedisqClient)

    #test initializaing Task with dictionary instead of JSON string raises error
    assert_raises(TypeError, Task, {})
