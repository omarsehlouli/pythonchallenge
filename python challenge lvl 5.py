import pickle
pickle_off = open("level5.pickle","rb")
emp = pickle.load(pickle_off)
for line in emp:
  empr=""
  for k, v in line:
    empr+=k*v
  print(empr)