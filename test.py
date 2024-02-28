
for i in range(1345):
    print(i)
    
variable = "variable"
print(variable[2])

guess = "a"

unders = ['_'] * len(variable)
print(unders)

for i in range(len(variable)):
    if variable[i] == guess:
        print(i)
        unders[i] = guess
    
print(unders)
