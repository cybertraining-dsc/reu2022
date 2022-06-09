import pickle

# Creating dictionary of data
votes = [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
print('Votes:', votes)

# Pickling the data
pickle_votes = pickle.dumps(votes)
print('Pickle:', pickle_votes)
