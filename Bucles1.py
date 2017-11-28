aNum=[]
num=0
while(num != -1):
    print("Introduce un numero:")
    num = int( input() )
    if(num != -1):
        aNum.append(num)

#RECORRO EL ARRAY Y LO VOY SUMANDO
acumulador = 0
elMayor = aNum[0]
for n in aNum:
    acumulador = acumulador + n
    if n>elMayor:
        elMayor = n

if len(aNum) != 0:
   print("SUMA:",acumulador)
   print("MEDIA:",acumulador/len(aNum))

   print("MAYOR:",elMayor)
   print("MENOR",min(aNum))