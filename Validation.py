while True:
  while True:
     a=float(input())
     if 0<=a<=10:
         break
     else:
         print('nota invalida')
  while True:    
     b=float(input())
     if 0<=b<=10:
         break
     else:
         print('nota invalida')
  result=(a+b)/2
  print('media = %.2f'%result)

  while True:
     print('novo calculo (1-sim 2-nao)')
     X=int(input())

     if X==1:
         break
     elif X==2:
         exit()
     else:
         continue