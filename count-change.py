def count_change(amount, denomination): 
    m= len(denomination)

    table = [0 for k in range(amount+1)] 
  
    table[0] = 1

    for i in range(0,m): 
        for j in range(denomination[i],amount+1): 
            table[j] += table[j-denomination[i]] 
  
    return table[amount] 

print(count_change(10,[2,3,5,6]))