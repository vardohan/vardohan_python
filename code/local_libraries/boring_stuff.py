import os
import sys

class boring_stuff():
    def __init__(self, source='', destination='', keyword=''):
        self.source = source
        self.destination = destination
        self.keyword = keyword

    def mycopy(self):
        try:
            pass
        except:
            print(sys.exc_info())
        
    def mymove(self):
        try:
            pass
        except:
            print(sys.exc_info())

    def __str__(self):
        return "boring_stuff"
        
class mymodule():
    def __init__(self, module=''):
        self._module = module

    @property
    def name(self):
        return self._module

    @name.setter
    def name(self, name):
        print(f"module name {name}")
        if name == '':
            raise ValueError("enter valid module name")
        self._module = name

    def details(self, mycallable=False):
        try:
            mydir               = dir(self._module)
            callable_data       = []
            non_callable_data   = []
            
            for name in mydir:
                if callable(eval(str(self._module).split()[1][1:-1] + '.' + name)):
                    callable_data.append(name)
                else:
                    non_callable_data.append(name)
            
            if mycallable:
                print(f"##### {str(self._module).split()[1][1:-1]}: Callable #####")
                count = 1
                for name in callable_data:
                    print(f"{count}.{name}", end=", ")
                    count += 1
            else:
                print(f"##### {str(self._module).split()[1][1:-1]}: Not Callable #####")
                count = 1
                for name in non_callable_data:
                    print(f"{count}.{name}", end=", ")
                    count += 1
                print(f"\n##### {str(self._module).split()[1][1:-1]}: Callable #####")
                count = 1
                for name in callable_data:
                    print(f"{count}.{name}", end=", ")
                    count += 1
                    print(str(help(eval(str(self._module).split()[1][1:-1] + '.' + name))))
        except:
            print(sys.exc_info())

    def __str__(self):
        return "mymodule"
