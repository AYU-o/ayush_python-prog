days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
total_temp=[]
for i in range (0,7):
    temp=int(input(f"Enter temp. of {days[i]}: "))
    total_temp.append(temp)
c=0
for x in total_temp:
    c=c+x
    
print("Average temprature pf the week: ",c/2)
