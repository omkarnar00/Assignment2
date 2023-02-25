def Sort_Tuple_in_list(list): 
    list.sort(key = lambda x: x[-1]) 
    return list
   

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
   
print(Sort_Tuple_in_list(list)) 

## output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]