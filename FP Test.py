import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat, umath

data = np.loadtxt('Auswahl 1.txt', skiprows=1, dtype=float)


#Daten präparieren
time = data[:, 0]
delta_mag = data[:, 1]
uncertainties = data[:, 2]

for i in range(len(delta_mag)):
        delta_mag[i] = np.exp((- 2 / 5 * delta_mag[i]) * np.log(10))


def trapezoid(x, left1, left2, right1, right2, height1, height2, height3):
        return np.piecewise(x,
                            [x < left1,
                             (x >= left1) & (x < left2),
                             (x >= left2) & (x < right1),
                             (x >= right1) & (x < right2),
                             x >= right2], [
                             height1,
                             lambda x: (height2 - height1) / (left2 - left1) * (x - left1) + height1,
                             height2,
                             lambda x: (height3 - height2) / (right2 - right1) * (x - right1) + height2,
                             height3])

k = 2.46044e6

initial_guess = [0.415 + k, 0.433 + k, 0.495 + k, 0.51 + k, 1.56, 1.52, 1.557]
popt, pcov = curve_fit(trapezoid, time, delta_mag, p0=initial_guess, sigma=uncertainties)


perr = np.sqrt(np.diag(pcov))
print("Optimierte Parameter:")
print("left1:", popt[0], "+/-", perr[0])
print("left2:", popt[1], "+/-", perr[1])
print("right1:", popt[2], "+/-", perr[2])
print("right2:", popt[3], "+/-", perr[3])
print("height1:", popt[4], "+/-", perr[4])
print("height2:", popt[5], "+/-", perr[5])
print("height3:", popt[6], "+/-", perr[6])

left1 = ufloat(popt[0], perr[0])
left2 = ufloat(popt[1], perr[1])
right1 = ufloat(popt[2], perr[2])
right2 = ufloat(popt[3], perr[3])
height1 = ufloat(popt[4], perr[4])
height2 = ufloat(popt[5], perr[5])
height3 = ufloat(popt[6], perr[6])



xvals = np.linspace(time[0], time[-1], 1000)
yvals = trapezoid(xvals, *popt)

plt.plot(xvals, yvals, label='Trapezfit')
plt.errorbar(time, delta_mag, yerr=uncertainties, fmt='o',markersize=3, color='black', label='Datenpunkte')
plt.xlabel('JD [d]')
plt.ylabel(r'$S_V / S_C$')
plt.legend()
plt.savefig('Exoplanet_Trapez_Fit.jpg')
plt.show()


#Die wichtigsten Kenngrößen aus den Daten berechnen:

transit_tiefe = 5 / 2 * (umath.log10((height1 + height3) / 2) - umath.log10(height2))
t_T = (right2 - left1) * 24 * 60 #Zeit zwischen ersten und vierten Kontakt in Minuten
t_t = (right1 - left2) * 24 * 60 #Zeit zwischen dem zweiten und dritten Kontakt
transit_mitte = (right1 - left1) * 0.5 + left1
verhältnis_radien = umath.sqrt(1 - (height2 / (height1 + height3) * 2))

print('Transittiefe:', transit_tiefe, 'in Magnituden')
print(r'$t_T$', t_T, 'min')
print(r'$t_t$', t_t, 'min')
print('Transitmitte', transit_mitte, 'JD')
print(verhältnis_radien)

print(time[0])
print(time[-1])

