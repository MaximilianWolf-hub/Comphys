import numpy
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Lichtkurve.txt', skiprows=2, dtype=float)
# Daten einlesen
t = data[:, 0]
S = data[:, 1]

# Fourier-Transformation durchführen
fft_coefficients = np.fft.fft(S)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

# Anzahl der zu behaltenden Koeffizienten
kmax = 25

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
dominant_periods = 1 / dominant_frequencies[2:]  # Frequenz bei Index 0 ist der DC-Anteil
print("Dominante Perioden:")
print(dominant_periods)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(t, S, label='Daten', color='blue')
plt.plot(t, reconstructed_signal.real, label='Gefittete Fourier-Reihe', color='red')
plt.xlabel('Julian Date (JD)')
plt.ylabel('Magnitude (V-C)')
plt.legend()
plt.title('Fourier-Fit der Lichtkurve')
plt.show()

Mittelwert = numpy.mean(dominant_periods[1:])