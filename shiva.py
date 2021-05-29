from sympy import *
a=Rational(3,5)
print(a)
b=Integer(3.567)
print(b)
c=pi
print(c)
c=(pi+2).evalf()
print(c)
r=(exp(2)+pi).evalf()
print(r)
t=oo+100
print(t)

x=Symbol('x')
y=Symbol('y')
z=x+y+x
print(z)

d=expand((x+y)**3)
print(d)
e=expand((x+y)**2)
print(e)

f=expand(cos(x+y),trig=True)
print(f)

k=simplify((x+x*y)/x)
print(k)

x=Symbol('x')
ans1=diff(sin(x)*exp(x),x)
print(ans1)

ans2=diff(tan(x),x)
print(ans2)

ans3=integrate(cos(x),(x,-1,+1))
print(ans3)

ans4=limit(sin(x)/x,x,0)
print(ans4)

ans5=solve(x**2-5*x+6,x)
print(ans5)

k=lambda x,y:x+y
print(k(2,4))