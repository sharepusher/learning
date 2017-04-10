# Map/Dictionary: searching for data items based on unique key values.
# A map is a container for storing a collection of data records in which each record is associated with a UNIQUE key.
# The key components must be comparable.

# Map(): Creates a new empty map.
# length(): Returns the number of key/value pairs in the map.
# contains(key): Determins if the given key is in the map and returns True if the key is found.
#     and False otherwise.
# add(key, value): Adds a new key/value pair to the map if the key is not already in the map
#     or replaces the data associated with the key if the key is in the map.
#     Returns True if this is a new key and False if the data associated with the existing key is replaced.
# remove(key): Removes the key/value pair for the given key if it is the map and raises an exception otherwise
# valueOf(key): Returns the data record associated with the given key.
#     The key must exist in the map or an exception is raised.
# iterator(): Creates and returns an iterator that can be used to iterate over the keys in the map.


