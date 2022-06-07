import pickle

# Creating dictionary of data
votes1 = [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
print('Before:', votes1)

# Encoding the data
pickle_votes = pickle.dumps(votes1)

# Decoding the data
votes2 = pickle.loads(pickle_votes)
print('After:', votes2)

# Checking authenticity
print('Same:', (votes1 is votes2))
print('Equal:', (votes1 == votes2))