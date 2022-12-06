import math

a = lambda x:x**2
print (f"Hasil Kuadrat x = {a(4)}")

b = lambda x,y:math.sqrt(x**2 + y**2)
print(f"hasi dari lambda = {b(2,4)}")

c = lambda *args:sum(args)/len(args)
print(c(23))

d = lambda s:"".join(set(s))
print(d('dipca'))