from math import sqrt, cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt

steps = 1e3

cosAng = np.linspace(-1,1,steps)
scalar = np.ones(steps)*0.5
vector0 = (1+cosAng**2 + cosAng)
vector = (vector0 - min(vector0))/(max(vector0)-min(vector0))
tensor0 = (1-3*cosAng**2 + 4*cosAng**4)
tensor = (tensor0 - min(tensor0))/(max(tensor0)-min(tensor0))


plt.xlabel(r'$\cos(\theta)$')
plt.ylabel(r'$d\sigma$')
plt.title(r'$q\bar{q} \rightarrow l^-l^+$')
hey1, = plt.plot(cosAng, scalar,label="Higgs")
hey2, = plt.plot(cosAng, vector,label="Electroweak")
hey3, = plt.plot(cosAng, tensor,label="Graviton")
plt.legend(handles=[hey1,hey2,hey3])
plt.savefig('angDist.pdf')
plt.show()
