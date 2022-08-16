def recur(n):
    if n>0:
        
        recur(n-1)
        print(n)
print(recur(4))