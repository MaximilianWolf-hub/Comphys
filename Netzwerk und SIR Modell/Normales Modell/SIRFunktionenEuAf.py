import numpy as np
from Städte_und_Populationen import cities_combined, population_combined
from scipy.integrate import odeint

#Wir erzeugen zweidimensionale Arrays für jede SIR-Population mit den Namen sus (S), inf (I) und rec (R):
zeros = np.zeros(len(cities_combined))
combined = list(zip(zeros, cities_combined))
combined_sus = list(zip(population_combined, cities_combined))
sus = np.array(combined_sus, dtype=object)  # sus erhält als Startwert die jeweiligen Populationen,
inf = np.array(combined, dtype=object)      # denn jeder kann anfangs infiziert werden
rec = np.array(combined, dtype=object)      # dtype Object, damit wir zwei verschiedene Datentypen im Array speichern können
                                            # (Floats - erste Spalte, Strings - zweite Spalte)
mu = 3e-5
beta = 0.1
gamma = 0.07

#Das sind die Parameter unserer Epidemie, die wir hier anpassen können beta ist der Ansteckungsparameter,
#mu die Sterbe- und Reproduktionsrate und gamma die Erholungsrate

def SIREuAf(x, t=0):  # diese DGL möchten wir numerisch lösen
    S, I, R = x
    N = S + I + R
    dS = - beta * S * I / N + mu * (N - S)
    dI = beta * S * I / N - gamma * I - mu * I
    dR = gamma * I - mu * R
    return [dS, dI, dR]

# Euler-Verfahren für eine Stadt
def infectEulerEuAF(x):
    h = 1
    x += h * np.array(SIREuAf(x))
    return x

# Runge-Kutta-Verfahren vierter Ordnung für eine Stadt
def infectRK4EuAF(x):
    h = 1
    x = np.array(x)  # Sicherstellen, dass x ein numpy-Array ist
    k1 = h * np.array(SIREuAf(x))
    k2 = h * np.array(SIREuAf(x + 0.5 * k1))
    k3 = h * np.array(SIREuAf(x + 0.5 * k2))
    k4 = h * np.array(SIREuAf(x + k3))
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x

# Nutzen der Ode-Int Methode von Scipy für eine Stadt
def infectODEsolverEuAF(x, t):
    deltat = np.array([t, t + 1], dtype=float)
    x = odeint(SIREuAf, x, deltat)
    return x[-1]  # Wir interessieren uns nur für den Endwert nach einem Zeitschritt

# SIR Modell mit Euler Verfahren für alle Städte
def infectEulerAllEuAF(Sus, Inf, Rec):
    for i in range(len(cities_combined)):
        x = [Sus[i], Inf[i], Rec[i]]
        result = infectEulerEuAF(
            np.array(x))
        Sus[i], Inf[i], Rec[i] = result

# SIR Modell mit Runge-Kutta Verfahren für alle Städte
def infectRK4AllEuAF(Sus, Inf, Rec):
    for i in range(len(cities_combined)):
        x = [Sus[i], Inf[i], Rec[i]]
        result = infectRK4EuAF(np.array(x))
        Sus[i], Inf[i], Rec[i] = result

# SIR Modell mit ode/odeint für alle Städte
def infectODEsolverAllEuAf(Sus, Inf, Rec):
    for i in range(len(cities_combined)):
        x = [Sus[i], Inf[i], Rec[i]]
        result = infectODEsolverEuAF(np.array(x), 0)
        Sus[i], Inf[i], Rec[i] = result
