import numpy as np
import matplotlib.pyplot as plt

# Daten einlesen
data = np.loadtxt('Lichtkurve.txt', skiprows=2, dtype=float)
t = data[:, 0]
S = data[:, 1]

# Fourier-Transformation durchführen
fft_coefficients = np.fft.fft(S)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

# Anzahl der zu behaltenden Koeffizienten
kmax = 20

# Gefilterte Fourier-Koeffizienten
filtered_fft_coefficients = np.zeros_like(fft_coefficients)
filtered_fft_coefficients[:kmax] = fft_coefficients[:kmax]
filtered_fft_coefficients[-kmax+1:] = fft_coefficients[-kmax+1:]

# Rekonstruierte Signal
reconstructed_signal = np.fft.ifft(filtered_fft_coefficients)

# Fourier-Koeffizienten anzeigen
print("Fourier-Koeffizienten:")
print(filtered_fft_coefficients[:kmax])

# Dominante Frequenzen anzeigen
dominant_frequencies = frequencies[:kmax]
print("Dominante Frequenzen:")
print(dominant_frequencies)

# Dominante Periode bestimmen (Periode = 1 / Frequenz)
# Ausschließen von Frequenzen bei 0 (DC-Anteil)
valid_indices = dominant_frequencies != 0
dominant_periods = 1 / dominant_frequencies[valid_indices]
print("Dominante Perioden:")
print(dominant_periods)

# Monte-Carlo-Sampling zur Bestimmung der Unsicherheiten
n_samples = 1000
coeff_samples = np.zeros((n_samples, len(filtered_fft_coefficients)))

for i in range(n_samples):
    noise = np.random.normal(0, np.std(S), len(S))
    S_sample = S + noise
    fft_sample = np.fft.fft(S_sample)
    filtered_fft_sample = np.zeros_like(fft_sample)
    filtered_fft_sample[:kmax] = fft_sample[:kmax]
    filtered_fft_sample[-kmax+1:] = fft_sample[-kmax+1:]
    coeff_samples[i, :] = filtered_fft_sample

# Berechnung der Mittelwerte und Standardabweichungen der Koeffizienten
coeff_means = np.mean(coeff_samples, axis=0)
coeff_stds = np.std(coeff_samples, axis=0)

# Plotten der Ergebnisse
plt.figure(figsize=(10, 6))
plt.scatter(t, S, label='Daten', color='blue')
plt.plot(t, reconstructed_signal.real, label='Gefittete Fourier-Reihe', color='red')
plt.xlabel('Julian Date (JD)')
plt.ylabel('Magnitude (V-C)')
plt.legend()
plt.title('Fourier-Fit der Lichtkurve')
plt.show()

# Ausgabe der Ergebnisse
print("Gefittete Koeffizienten mit Unsicherheiten:")
for k in range(kmax):
    print(f"Re(C{k+1}) = {coeff_means[k].real} ± {coeff_stds[k].real}")
    print(f"Im(C{k+1}) = {coeff_means[k].imag} ± {coeff_stds[k].imag}")

# Mittelwert der dominanten Perioden
mittelwert = np.mean(dominant_periods)
print("Mittelwert der dominanten Perioden:")
print(mittelwert)


