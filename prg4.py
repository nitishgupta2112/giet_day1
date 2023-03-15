def change(ones,fives,t_amt):
    n_fives = t_amt//5
    t_n_fives = n_fives*5
    n_ones = t_amt - t_n_fives
    if(ones>=n_ones and n_fives>=fives):
        return n_ones,n_fives
    else:
        return "insufficient"
ones = int(input())
fives= int(input())
t_amt = int(input())
print(change(ones,fives,t_amt))


