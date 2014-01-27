redisq-py
=========

.. image:: https://secure.travis-ci.org/joshuakarjala/redisq-py.png?branch=master
   :target: http://travis-ci.org/joshuakarjala/redisq-py

Python client for https://github.com/runk/redisq (Fast message processing queue backed up by redis and nodejs)

Example
-------

.. code-block:: py

    from redisq import RedisqClient, Task

    task_dict = {"foo": "bar"}

    queue = RedisqClient("foo:bar")
    task = Task(json.dumps(task_dict))

    queue.pushTask(task)


    #Connecting to non-default Redis Server
    queue = RedisqClient("foo:bar", host="foo", port=6389, password="bar", db=1)
