import pickle

tuple = (1,1)

serial = pickle.dumps(tuple)
print('pickle: ', serial)
deserial = pickle.loads(serial)
print(deserial)
