import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Beispielhafte Lichtkurvendaten (Zeit t und Helligkeit y)
t = np.array([...])  # Zeiten der Messungen
y = np.array([...])  # Helligkeitswerte der Messungen

# Fourier-Reihe Funktion
def fourier_series(t, *params):
    S0 = params[0]
    P = params[1]
    Kmax = (len(params) - 2) // 2
    result = S0
    for k in range(1, Kmax + 1):
        Ck = params[2 * k]
        Dk = params[2 * k + 1]
        result += Ck * np.sin(2 * np.pi * k * t / P) + Dk * np.cos(2 * np.pi * k * t / P)
    return result

# Initiale Schätzungen für S0, P, Ck und Dk
S0_init = np.mean(y)
P_init = ...  # Schätzung der Periode (z.B. durch Periodensuche)
Kmax = 5  # Maximalordnung der Fourier-Reihe
initial_guess = [S0_init, P_init] + [0] * (2 * Kmax)

# Fit der Fourier-Reihe an die Daten
params, covariance = curve_fit(fourier_series, t, y, p0=initial_guess)

# Extrahieren der Fit-Parameter
S0_fit = params[0]
P_fit = params[1]
Ck_fit = params[2::2]
Dk_fit = params[3::2]

# Plotten der Ergebnisse
t_fit = np.linspace(min(t), max(t), 1000)
y_fit = fourier_series(t_fit, *params)

plt.scatter(t, y, label='Daten')
plt.plot(t_fit, y_fit, label='Fourier Fit', color='red')
plt.xlabel('Zeit')
plt.ylabel('Helligkeit')
plt.legend()
plt.show()

# Ausgabe der Ergebnisse
print("Gefittete Koeffizienten:")
print(f"S0 = {S0_fit}")
print(f"P = {P_fit}")
for k in range(Kmax):
    print(f"C{k+1} = {Ck_fit[k]}")
    print(f"D{k+1} = {Dk_fit[k]}")

