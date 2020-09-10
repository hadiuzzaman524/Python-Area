#Two dice are rolled. What is the probability that at least one is a six?
#solutions
import itertools as it

space=set(it.product({1,2,3,4,5,6},{1,2,3,4,5,6}))

total_sample_space=len(space)
print(f"Total sample space: {total_sample_space}")

atlast_one_six=0
for i in space:
    if i.count(6)>=1:
        atlast_one_six+=1
print("Total event of atlast one six: atlast_one_six))

print(f"Probability of at last one six is: {atlast_one_six/total_sample_space}")

