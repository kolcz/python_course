from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation #biblioteka do robienia animacji

def rhs(y0,t):
    return -y0
#wyliczanie pochodnej
t=np.linspace(0,1,100)
y=odeint(rhs,1.,t)
#rysowanie wykresu
fig=plt.figure()
plt.plot(t,y)
plt.plot(y,t)



plt.show() #pokazanie wykresu na ekranie
