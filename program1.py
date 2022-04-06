def printFred(n):
    print('Fred')
    if n == 1:
       return
    else:
       printFred(n-1)

printFred(5)
