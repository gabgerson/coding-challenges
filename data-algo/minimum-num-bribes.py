def minimumBribes(q):

    #store num_bribes
    num_bribes = 0
        
    for i, val in enumerate(q):
        #check if val - current index + 1 is greater that 2 meaning val moved 3 or more places
        if val - (i+1) > 2:
        #print too chaotic
            print("Too chaotic")
            return
        else:
            #check how many people bribed current val by looping from 1 place in front of curr original position to 
            #one place in front of current position.
            for j in range(max(val-2,0),i):
                if q[j] > val:
                    num_bribes += 1


    print(num_bribes)
