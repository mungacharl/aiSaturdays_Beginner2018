import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
for belowFive in ourList:
	if belowFive < 5:
		print(belowFive)
