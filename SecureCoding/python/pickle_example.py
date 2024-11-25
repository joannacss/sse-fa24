import pickle

data = {'key': 'value'}
# Serialization
serialized = pickle.dumps(data)
# Deserialization
deserialized = pickle.loads(serialized)
print(serialized)
