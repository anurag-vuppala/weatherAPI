a = [1,2,3,4,3,2,1,5,6,7,5,8,9,8]
count = 0
t = []
for i in range(len(a)):
    if i not in t:
        for k in range(len(a)):
            if i == k:
                count= count + 1
        print(i,count)
        
    
        
    