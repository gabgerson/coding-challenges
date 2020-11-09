import bisect

def activityNotifications(expenditure, d):
 
    #sort array from 0 to d -1
    days =  sorted(expenditure[0:d])
    #middle = d//2
    mid = d//2
    #save num notifications to variable
    notifications = 0

    #loop through expenditures from d to end
    for i in range(d, len(expenditure)):
        #if median is even add item at index d//2 -1 and d //2 and divide by 2
        if d % 2 == 0:
            median = (days[mid] + days[mid - 1]) / 2
        else:
            #if d is odd median is d // 2 no remainder
            median =  days[mid]
        #if item at median * 2 is greater than or equal to expenditure at i 
        if expenditure[i] >= 2 * median:
            # add to notifications
            notifications +=1
       
            
        #get index of start of trailing days and pop from days list
        days.pop(bisect.bisect_left(days, \
                 expenditure[i - d]))
       
        # add current item in expenditure to days using insort to correct place
        bisect.insort(days, expenditure[i])
 
    return notifications





