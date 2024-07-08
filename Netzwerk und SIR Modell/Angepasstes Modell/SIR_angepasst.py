import numpy as np
from city_data import cities, population
from scipy.integrate import odeint


#Wir erzeugen zweidimensionale Arrays für jede SIR-Population mit den Namen sus (S), inf (I) und rec (R)
zeros = np.zeros(len(cities))
combined = list(zip(zeros, cities))
combined_sus = list(zip(population, cities))
sus = np.array(combined_sus, dtype=object)    #sus erhält als Startwert die jeweiligen Populationen,
inf = np.array(combined, dtype=object)        #denn jeder kann anfangs infiziert werden
rec = np.array(combined, dtype=object)        #dtype Object, damit wir zwei verschiedene Datentypen im Array
vac = np.array(combined, dtype=object)        #speichern können (Floats - erste Spalte, Strings - zweite Spalte)
                                              #zudem haben wir nun eine dritte Gruppe, die Geimpften (vac für englisch vaccinated)
mu = 3e-5   #Sterberate
beta = 0.1  #Infektionsparameter
gamma = 0.07    #Erhohlungsrate
vac_rate = 0.001    #Wahrscheinlichkeit, dass sich Person impft


# SIR-Modell-Differentialgleichungen mit Impfungen
def SIR(x, t, mu, beta, gamma, vac_rate):
    S, I, R, V = x
    N = S + I + R + V
    dS = -beta * S * I / N + mu * (N - S) - vac_rate * S
    dI = beta * S * I / N - gamma * I - mu * I
    dR = gamma * I - mu * R
    dV = vac_rate * S - mu * V
    return [dS, dI, dR, dV]

# Euler-Verfahren
def infectEuler(x, mu, beta, gamma, vac_rate):
    h = 1
    x += h * np.array(SIR(x, 0, mu, beta, gamma, vac_rate))
    return x

# Runge-Kutta-Verfahren vierter Ordnung
def infectRK4(x, mu, beta, gamma, vac_rate):
    h = 1
    x = np.array(x)  # Sicherstellen, dass x ein numpy-Array ist
    k1 = h * np.array(SIR(x, 0, mu, beta, gamma, vac_rate))
    k2 = h * np.array(SIR(x + 0.5 * k1, 0, mu, beta, gamma, vac_rate))
    k3 = h * np.array(SIR(x + 0.5 * k2, 0, mu, beta, gamma, vac_rate))
    k4 = h * np.array(SIR(x + k3, 0, mu, beta, gamma, vac_rate))
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x

# Nutzen der odeint-Methode von SciPy
def infectODEsolver(x, t, mu, beta, gamma, vac_rate):
    deltat = np.array([t, t + 1], dtype=float)
    x = odeint(SIR, x, deltat, args=(mu, beta, gamma, vac_rate))
    return x[-1]  # Wir interessieren uns nur für den Endwert nach einem Zeitschritt

# SIR-Modell mit Euler-Verfahren für alle Städte
def infectEulerAll(Sus, Inf, Rec, Vac):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Vac[i]]
        if Inf[i] / Sus[i] > 0.05:
            result = infectEuler(np.array(x), 0.5 * mu, 0.5 * beta, 0.5 * gamma, vac_rate)
        else:
            result = infectEuler(np.array(x), mu, beta, gamma, vac_rate)
        Sus[i], Inf[i], Rec[i], Vac[i] = result

# SIR-Modell mit Runge-Kutta-Verfahren für alle Städte
def infectRK4All(Sus, Inf, Rec, Vac):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Vac[i]]
        if Inf[i] / Sus[i] > 0.05:
            result = infectRK4(np.array(x), 0.5 * mu, 0.5 * beta, 0.5 * gamma, vac_rate)
        else:
            result = infectRK4(np.array(x), mu, beta, gamma, vac_rate)
        Sus[i], Inf[i], Rec[i], Vac[i] = result

# SIR-Modell mit odeint für alle Städte
def infectODEsolverAll(Sus, Inf, Rec, Vac):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Vac[i]]
        if Inf[i] / Sus[i] > 0.05:
            result = infectODEsolver(np.array(x), 0, 0.5 * mu, 0.5 * beta, 0.5 * gamma, vac_rate)
        else:
            result = infectODEsolver(np.array(x), 0, mu, beta, gamma, vac_rate)
        Sus[i], Inf[i], Rec[i], Vac[i] = result

