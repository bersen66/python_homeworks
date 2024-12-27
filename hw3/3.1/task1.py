from matrix import Matrix
import numpy as np

l = Matrix.from_numpy(np.random.randint(0, 10, (10, 10))) 
r = Matrix.from_numpy(np.random.randint(0, 10, (10, 10))) 

print(f"Left matrix:\n{l}\n Right matrix:\n{r}")
print("generating artifacts:")
with open("matrix+.txt", "w") as file:
    print("matrix+.txt")
    file.write(str(l + r) + "\n")
    print("done!")

with open("matrix*.txt", "w") as file:
    print("matrix*.txt")
    file.write(str(l * r) + "\n")
    print("done!")

with open("matrix@.txt", "w") as file:
    print("matrix@.txt")
    file.write(str(l @ r) + "\n")
    print("done!")

print("All artifacts generated!")
