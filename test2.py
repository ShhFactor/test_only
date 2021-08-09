t1 =0
t2 =0
for i in range(len):
    if count ==1:
        t1 = lis[len-1]
        lis[len-1] = lis[len] 
    else:
        t2 = lis[len-1]
        lis[len-1] = t1
        t1 = t2
    count = count+1    
