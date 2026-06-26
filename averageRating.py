values = input()
values = values.split(",")
values = list(map(int,values))
# first - function which needs to be applied 
# second - values / list for which the function need to be applied 
print(values)

# number = "3"
# number = int(number)

# for i in range(len(values)): # 0 to n-1 where n is the length of the list 
#     values[i] = int(values[i])
# print(values)
if len(values)>0:
    average=sum(values)/len(values)
    print("Average:", average)
else:
    print("No numbers entered.")
