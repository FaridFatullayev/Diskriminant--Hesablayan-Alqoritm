import math
print("Kvadrat Tənliyin Kökünü Tapan Alqoritm ")
a=int(input("a Əmsalını Daxil Edin :"))
b=int(input("b Əmsalını Daxil Edin :"))
c=int(input("c Əmsalını Daxil Edin :"))
D=b**2-4*a*c
if D<0:
    print("Tənliyin Həqiqi Kökü Yoxdur . ")
    print("Diskriminant = ",D)
elif D == 0:
    print("Tənliyin 2 Bərabər Kökü Var . ")
    print('Diskriminant = ',D)
    x1 = x2 = -b/2*a
    print("Tənliyin Kökü : " ,x1)
elif D>0:
    print("Tənliyin 2 Həqiqi Kökü Var . ")
    print('Diskriminant = ',D)
    x1=(-b+math.sqrt(D))*2*a
    x2=(-b-math.sqrt(D))*2*a
    print("Birinci Kök : " , x1)
    print("İkinci Kök : ", x2)
