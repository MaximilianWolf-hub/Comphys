import numpy as np
import matplotlib.pyplot as plt

# Daten laden
data = np.loadtxt('Selection6_all.txt', skiprows=2, dtype=float)
t = data[:, 0]
deltaM = data[:, 1]
uncertaintiesM = data[:, 2]

# Berechnung von frac_S und dessen Unsicherheiten
frac_S = np.exp(-np.log(10) * deltaM / 2.5)
uncertainties_S = 1 / 2.5 * np.log(10) * uncertaintiesM * np.exp(-np.log(10) * deltaM / 2.5)

print(max(deltaM) - min(deltaM))

# Fourier-Transformation
fft_coefficients = np.fft.fft(frac_S)

# Abbruchordnung festlegen und ggf. erhöhen
kmax = 20  # Erhöhe kmax für mehr Frequenzkomponenten

# Filterung der Fourier-Koeffizienten
filtered_fft_coefficients = np.zeros_like(fft_coefficients)
filtered_fft_coefficients[:kmax] = fft_coefficients[:kmax]
filtered_fft_coefficients[-kmax+1:] = fft_coefficients[-kmax+1:]

# Rekonstruktion des Signals
reconstructed_signal = np.fft.ifft(filtered_fft_coefficients)

# Nur den realen Teil der rekonstruierten Signale verwenden
reconstructed_signal_real = np.real(reconstructed_signal)



# Plot
plt.figure(figsize=(10, 6))
plt.errorbar(t, frac_S, yerr=uncertainties_S, fmt='o', label='Daten', color='black', capsize=2, markersize=2)
plt.xlabel('Julianisches Datum (JD)')
plt.plot(t, reconstructed_signal_real, label='Fourier-Fit')
plt.ylabel(r'$S_C/S_V$')
plt.legend()
plt.title('Fourier-Fit der Lichtkurve')
plt.savefig('Lichtkurve_ganz.jpeg')
plt.show()

