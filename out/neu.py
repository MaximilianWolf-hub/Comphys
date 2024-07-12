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
kmax = 25

# Gefilterte Fourier-Koeffizienten
filtered_fft_coefficients = np.zeros_like(fft_coefficients)
filtered_fft_coefficients[:kmax] = fft_coefficients[:kmax]
filtered_fft_coefficients[-kmax + 1:] = fft_coefficients[-kmax + 1:]

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

# Monte-Carlo-Sampling zur Bestimmung der Unsicherheit der Periodendauer
n_samples = 1000
period_samples = np.zeros(n_samples)

for i in range(n_samples):
    noise = np.random.normal(0, np.std(S), len(S))
    S_sample = S + noise

    # Fourier-Transformation des resampelten Signals
    fft_sample = np.fft.fft(S_sample)
    filtered_fft_sample = np.zeros_like(fft_sample)
    filtered_fft_sample[:kmax] = fft_sample[:kmax]
    filtered_fft_sample[-kmax + 1:] = fft_sample[-kmax + 1:]

    # Bestimmung der dominanten Frequenz und der entsprechenden Periode
    dominant_frequency_sample = frequencies[np.argmax(np.abs(filtered_fft_sample))]
    if dominant_frequency_sample == 0:
        dominant_period_sample = np.inf
    else:
        dominant_period_sample = 1 / dominant_frequency_sample

    period_samples[i] = dominant_period_sample

# Berechnung des Mittelwerts und der Unsicherheit der Periodendauer
period_mean = np.mean(period_samples)
period_std = np.std(period_samples)
period_sem = period_std / np.sqrt(n_samples)  # Standard Error of the Mean (SEM)

# Plotten der Histogramm der Periodensamples
plt.figure(figsize=(10, 6))
plt.hist(period_samples, bins=30, edgecolor='black', alpha=0.7)
plt.axvline(period_mean, color='r', linestyle='--', linewidth=2, label='Mittelwert')
plt.xlabel('Periode')
plt.ylabel('Häufigkeit')
plt.legend()
plt.title('Histogramm der Periodensamples')
plt.grid(True)
plt.show()

# Ausgabe der Ergebnisse
print("\nAusgabe der Ergebnisse:")
print("Mittelwert der dominanten Perioden:")
print(period_mean)
print("Standardabweichung der dominanten Perioden:")
print(period_std)
print("Unsicherheit des Mittelwerts der dominanten Perioden:")
print(period_sem)

