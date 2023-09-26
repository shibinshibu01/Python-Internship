import numpy as np

def arr_sum(arr5d):
    pro=1
    for i in arr5d:
        for j in i:
            for k in j:
                for l in k:
                    for m in l:
                        pro*=m   
    return pro                         

arr= np.array([[1,1,1,1],[1,1,1,1]])
for i in range(0,len(arr),1):
    for j in range(0,len(arr[i]),1):
        if arr[i][j]==23:
            #print(arr[i][j])
            break
    #else:
        #print("Not Found")

#print(arr.shape)

arr3d= np.array([arr,arr])
arr4d= np.array([arr3d,arr3d])
arr5d= np.array([arr4d,arr4d])

#print(arr5d[1][1][1][1][1])


pro=arr_sum([[[[[4,5]]]]])                    
print("\n\n",pro,"\n\n")  
#print(arr5d)
#print(arr5d[1][0][0][0][1:])