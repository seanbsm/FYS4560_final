
from math import sqrt, cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt

#SM free parameters
alpha 	 = 1/137.		#n.u.
mZ 	 = 91.1875		#[GeV]
WSin2Ang = 0.23126
WCos2Ang = 0.76874


#Sm dependant parameters
steps = 1e6
energies 	  = np.linspace(9148,9150,steps)		#[GeV]
#taken from p.423 Thomson
Ve = Vt   = -0.04
Ae = At   = -0.5
fullWidth = 2.4952	#[GeV] (from PDG)
gZ 		  = sqrt((4*pi*alpha)/(WSin2Ang*WCos2Ang))

for s in energies:
	chi 	= (s*(s-mZ**2)*gZ**2)/(16*pi*alpha*((s-mZ**2)**2+mZ**2*fullWidth**2))
	chi2 	= ((s*gZ**2)**2)/((16*pi*alpha)**2*((s-mZ**2)**2+mZ**2*fullWidth**2))

	A = 1 + 2*chi*Ve*Vt + chi2*(Ve**2 + Ae**2)*(Vt**2 + At**2)
	B = 4*chi*Ae*At + 8*chi2*Ve*Ae*Vt*At

	if abs(A-B) < 1e-6:
		print s

