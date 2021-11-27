import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x*x

#Formula baseada em função
#plt.plot(x,y) # funciona somente no notebook python usando o metodo
#matplotlib inline - serve pra visualizar o grafico
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('Eixo x')
axes.set_title('Titulo')