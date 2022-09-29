from cmath import sqrt

print("equations de la forme ax2 + bx + c")
kdfd_a = int(input("en la premiere valeur de a"))
kdfd_b = int(input("entrez la valeur de b"))
kdfd_c = int(input("entrez la valeur de c"))

if kdfd_a == 0 and kdfd_b == 0: 
   print("attention! variable manquante")
elif kdfd_a==0 and kdfd_b!=0:
     kdfd_x = (-kdfd_c/kdfd_b)   
     print("la solution est", kdfd_x)
elif kdfd_a!=0 or kdfd_b!=0:
     kdfd_d = kdfd_b*kdfd_b - 4*kdfd_a*kdfd_c
     if kdfd_d < 0:
          print ("pas de solutions dans R")
     elif kdfd_d == 0:
          kdfd_x= (-kdfd_b/2*kdfd_a)
          print("on obtient une solution double qui est X=", kdfd_x)
     else :
             kdfd_x1 = -kdfd_b + (sqrt(kdfd_d)/2*kdfd_a)
             kdfd_x2 = -kdfd_b - (sqrt(kdfd_d)/2*kdfd_a)
             print ("on obtient deux solutions a savoir:")
             print("X1=", kdfd_x1)
             print("X2=", kdfd_x2)
