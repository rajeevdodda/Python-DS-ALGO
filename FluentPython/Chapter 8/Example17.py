# Example 8-17. A weak reference is a callable that returns the referenced object or None
# if the referent is no more

import weakref

a_set = {1, 2}

wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {1, 2, 3}
print(wref())
