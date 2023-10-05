import random
import numpy as np

f = open('./db.smiles','r')
f = f.readlines()
f = np.array(f)

random.seed(0)
in_sample = random.sample(population=list(range(len(f))), k=int(len(f)/2))
out_of_sample = list(set(range(len(f))) - set(in_sample))

in_sample = f[in_sample]
out_of_sample = f[out_of_sample]

f = open('./compounds.smiles', 'w')
for line in in_sample:
    f.write(line)
