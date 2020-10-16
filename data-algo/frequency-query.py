def freqQuery(queries):

    #create dict to store values and occurances
    val = dict()
    #store outcome of 3 queries
    
    arr3_queries = []
    # loop through queries
    
    #2 delete
    
    for query in queries:
        #1 insert
        if query[0] == 1:
            if query[1] not in val:
                val[query[1]] = 1
            else:
                val[query[1]] += 1
        #2 delete
        elif query[0] == 2:
            if query[1] in val:
                val[query[1]] -= 1
                #delete value if it == 0
                if val[query[1]] == 0:
                    del val[query[1]] 
            
        #3 check if there is a value that occurs a certain num of times
        elif query[0] == 3:
            if query[1] in set(val.values()):
                arr3_queries.append(1)
            else:
                arr3_queries.append(0)

    return arr3_queries