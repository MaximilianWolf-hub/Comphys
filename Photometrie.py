import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt('Lichtkurve.txt', skiprows=2, dtype=float)
t = data[:, 0]
S = data[:, 1]

#Funktion zur Berechnung der Fourier-Reihe:

fft_coefficients = np.fft.fft(S)

kmax = 10

filtered_fft_coefficients = np.zeros_like(fft_coefficients)
filtered_fft_coefficients[:kmax] = fft_coefficients[:kmax]
filtered_fft_coefficients[-kmax+1:] = fft_coefficients[-kmax+1:]

reconstructed_signal = np.fft.ifft(filtered_fft_coefficients)


#Plot
plt.figure(figsize=(10, 6))
plt.scatter(t, S, label='Daten', color='blue')
plt.plot(t, reconstructed_signal, label='Gefittete Fourier-Reihe', color='red')
plt.xlabel('Julian Date (JD)')
plt.ylabel('Magnitude (V-C)')
plt.legend()
plt.title('Fourier-Fit der Lichtkurve')
plt.show()

