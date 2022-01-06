import numpy as np
import matplotlib.pyplot as plt

def gradiant_descent(x,y):
    m_curr=b_curr=0
    iterations=1000
    n=len(x)
    learing_rate=0.01
    m=c=0
    ct=10000
    l=[]
    for i in range(iterations):
        y_pridicted=m_curr*x+b_curr

        cost=(1/n)*sum([val**2 for val in (y-y_pridicted)])

        md=-(2/n)*sum(x*(y-y_pridicted))
        bd=-(2/n)*sum(y-y_pridicted)
        m_curr=m_curr-learing_rate*md
        b_curr=b_curr-learing_rate*bd
        if cost<ct:
            ct=cost
            m=m_curr
            c=b_curr
        print("m {} , b {} , cost {} ".format(m_curr,b_curr,cost))
    l.append(ct)
    l.append(m)
    l.append(c)
    return l
x=np.array([0,2,3,4,5])
y=np.array([5,7,19,11,17])



#plt.show()



p=gradiant_descent(x,y)
xf=np.linspace(0,7)
yf = p[1]*xf+p[2]
plt.scatter(x,y,color="red")
plt.plot(xf,yf,color="blue")
plt.show()
