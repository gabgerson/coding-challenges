def hourglassSum(arr):
    i = 0 # index of item in current array
    j = 0 # index of curent array in larger array
    
    result = list()
    while j <= len(arr):
        

        if i == len(arr[j]) or i+1 >= len(arr[j]) or i+2 >=len(arr[j]):
            i = 0
            j+=1
        if j == len(arr[j]) or j+1 >=len(arr[j]) or j+2 >=len(arr[j]):
    
            return max(result)
   
        top = arr[j][i] + arr[j][i+1] +  arr[j][i+2] 
        middle = arr[j+1][i+1]
        bottom = arr[j + 2][i] + arr[j+2][i+1] +  arr[j+2][i+2] 
        i+=1
        result.append(top+middle+bottom)

    
