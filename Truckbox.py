'''
req:
truck size = 4
BT: [[1,3], [2,2],[3,1]]
o/p: 8

1. sort list into units in ascending order.
2. do value - ts each time till the ts = 0
3. remove elements based on truck size

'''

def maximumUnits(li, m):
    li = sorted(li, key=lambda i:i[1], reverse=True)
    
    w = 0

    for a in range(len(li)):
       b = li[a]
       

       #check till trucksize>0, delete from first index of b
       while(m>0):
        if b[0]!= 0:
            b[0] = b[0] - 1
            
            m= m - 1
            w = w + b[1]
        else:
            break
    return w
            

        

        
        
        

    

    


li = [[5,10],[2,5],[4,7],[3,9]]
print(maximumUnits(li, 10))