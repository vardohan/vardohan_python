import sys

sys.path.append("/home/ramesh/Documents/github/vardohan_python/code/global_libraries")
sys.path.append("/home/ramesh/Documents/github/vardohan_python/code/local_libraries")

from boring_stuff import mymodule
from boring_stuff import common_stuff

# bs = boring_stuff()
# print(bs)
# print(bs.__dict__)

# print(sys.path)

mm = mymodule(sys)
mm.details(mycallable=False)

# import os
# mm.name = os
# mm.details()
