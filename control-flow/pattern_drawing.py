num_of_rows = int(input("Enter the size of the pattern:"))
i = 1 
while i <= num_of_rows:
    for j in range(0, num_of_rows):
        print("*", end="")
    print()
    i +=1
    