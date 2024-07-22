import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Fourier-Reihe definieren
def fourier_series(t, P, *a):
    S0 = a[0]
    series = S0
    K = (len(a) - 1) // 2
    for k in range(1, K+1):
        Ck = a[2*k-1]
        Dk = a[2*k]
        series += Ck * np.sin(2 * np.pi * k * t / P) + Dk * np.cos(2 * np.pi * k * t / P)
    return series

# Daten laden
data = np.loadtxt('Selection6.txt', skiprows=2, dtype=float)
t = data[:, 0]
deltaM = data[:, 1]
uncertaintiesM = data[:, 2]

# Berechnung von frac_S und dessen Unsicherheiten
frac_S = np.exp(-np.log(10) * deltaM / 2.5)
uncertainties_S = 1 / 2.5 * np.log(10) * uncertaintiesM * np.exp(-np.log(10) * deltaM / 2.5)

# Erste Schätzung der Periodendauer (z.B. aus der Frequenzanalyse oder manuell geschätzt)
initial_period = 0.15  # Beispielwert, sollte basierend auf den Daten angepasst werden

# Erste Schätzungen für Fourier-Koeffizienten
Kmax = 8
initial_guess = [0.7] + [0.0] * (2 * Kmax)

# Curve-Fitting
# Curve-Fitting
params, params_covariance = curve_fit(fourier_series, t, frac_S, p0=[initial_period] + initial_guess, sigma=uncertainties_S, absolute_sigma=True)

# Parameter extrahieren
fitted_period = params[0]
S0 = params[1]
Ck = params[2:2+Kmax]
Dk = params[2+Kmax:]

# Kovarianzmatrix extrahieren
cov_diag = np.diag(params_covariance)

# Unsicherheit der Periodendauer
uncertainty_period = np.sqrt(cov_diag[0])

# Angepasste Fourier-Reihe berechnen
t_fit = np.linspace(min(t), max(t), 1000)
fitted_series = fourier_series(t_fit, fitted_period, *params[1:])

# Plot
plt.figure(figsize=(10, 6))
plt.errorbar(t, frac_S, yerr=uncertainties_S, fmt='o', label='Daten', color='black', capsize=2, markersize=2)
plt.xlabel('Julianisches Datum (JD)')
plt.plot(t_fit, fitted_series, label='Fourier-Fit')
plt.ylabel(r'$\frac{S_C}{S_V}$')
plt.legend()
plt.title('Fourier-Fit der Lichtkurve')
plt.savefig('Lichtkurve_teil.jpeg')
plt.show()

# Ausgabe der angepassten Parameter und deren Unsicherheiten
print(f"Angepasste Periodendauer: {fitted_period} ± {uncertainty_period}")
for k in range(1, Kmax+1):
    print(f"C_{k} = {Ck[k-1]}, D_{k} = {Dk[k-1]}")