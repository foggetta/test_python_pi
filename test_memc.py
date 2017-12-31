import pylibmc
import time
mc = pylibmc.Client(['127.0.0.1:11211'])
mc["some_key"] = "Some value"
mc["some_key"]

mc["another_key"]=3
mc["another_key"]

del mc["another_key"]
"some_key" in mc

mc["another_key"]=9

mc.set("key", 1)   # note that the key used for incr/decr must be a string.
value = mc.get("key")
print(value)
mc.incr("key")
value = mc.get("key")
print(value)
mc.decr("key")
value = mc.get("key")
print(value)

mc.get_multi(["key", "another_key"])
mc.set_multi({"cats": ["on acid", "furry"], "dogs": True})
mc.get_multi(["cats", "dogs"])
mc.delete_multi(["cats", "dogs", "nonextant"])
 



sample_obj = {"name": "Soliman",
"lang": "Python"}
mc.set("sample_user", sample_obj, time=15)
print ("Stored to memcached, will auto-expire after 15 seconds")
while mc.get("sample_user"):
    print (mc.get("sample_user"))
    time.sleep(1)