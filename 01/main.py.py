for i in range(1,10):
    print(' '*8*i,end='')
    for j in range(i,10):
           
        formular='{0:1}*{1:1}={2:<3} '.format(i,j,i*j)
      
        print ( formular,end='')
    print()

