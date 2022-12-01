r=(9**8)*(3**20)-(3**10)-3
count=0
while r>0:
    if r%3==2:
        count+=1
    r=r//3
print(count)