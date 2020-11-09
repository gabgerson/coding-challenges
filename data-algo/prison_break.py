# def prison(n, m, h, v):
#     # make a matrix with n+ 1 size list with  lists that are m + 1 long 
#     # prison_bars = [[0] * (m + 1)]* (n + 1)
#     prison_bars = [[0 for i in range(m +1)] for j in range(n + 1)]
#     # print(prison_bars)
#     # loop through horixontal bars list
#     # every index in each nested list gets +=1  at index h and 1 before

#     for bar in v:
    
    
#         for i in range(len(prison_bars)):

        
#             prison_bars[i][bar] = "v" 
               
#             prison_bars[i][bar-1] = "v"

#     for bar in h:
#         for i in range(bar - 1, bar + 1):
#             for j in range(len(prison_bars[i])):
#                 if prison_bars[i][j]  == "v":
#                     prison_bars[i][j] = prison_bars[i][j] + "h"
#                 elif prison_bars[i][j] == 0:
#                     prison_bars[i][j] = "h"
    
#     # loop through matrix and count how many vh's there are
#     area = 0
#     max_area = 0
#     for row in prison_bars:
    
#         for col in row:
     
#             if col == "vh":
#                 area += 1
        
    
#     print(prison_bars)
#     return area


def prison(n, m, h, v):
    # Write your code here
    #make list to store h_bar places 1 = bar is there same for v_bars
    h_bars = [1] * (n)
    
    v_bars = [1] * (m)

    #store max_h bar value and max_v value
    max_h_gap = 0
    max_v_gap = 0
    #store current_h_gap and current_v_gap
    current_h_gap = 0
    current_v_gap = 0

    #loop through h list
    for bar in h:
        #where an bar is taken away put a 0
        h_bars[bar-1] = 0
    
    # loop through v list
    for bar in v:
        #where an bar is taken away put a 0 in v_bars
        v_bars[bar-1] = 0

    #get max gap created by taking bars out
    #repeat for v_bars
    # loop through h_bars
    for bar in h_bars:
        # if bar == 1  reset current h_gap to 0
        if bar == 1:
            current_h_gap = 0
        #if b == 0 current_h_gap += 1 find max_h_gap
        else:
            current_h_gap += 1
            max_h_gap = max(current_h_gap, max_h_gap)
    
    for bar in v_bars:
        if bar == 1:
            current_v_gap = 0
        else:
            current_v_gap +=1
            max_v_gap = max(current_v_gap, max_v_gap)
    #multipy max v gaps + 1 and h gaps + 1 to get the max area 
    return (max_h_gap + 1) * (max_v_gap + 1)


print(prison(3,2,[1,2,3],[1,2]))
print(prison(3,3,[2],[2]))
print(prison(2,2,[1],[2]))
print(prison(6,6,[4],[2]))
print(prison(6,9,[2,5],[2,3]))
print(prison(500,200,[2,5,9,10,100],[2,3,3,6,7]))