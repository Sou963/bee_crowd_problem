while True:
    x=float(input())
    y=float(input())
    if 0<=x<=10:
        if 0<=y<=10:
                result=(x+y)/2
                print('media = %.2f'%result)
                break
        else:
                 print('nota invalida')        
    else:
        print('nota invalida')




