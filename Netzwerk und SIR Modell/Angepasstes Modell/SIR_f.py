import numpy as np
from city_data import cities, population
from scipy.integrate import odeint


#Wir erzeugen zweidimensionale Arrays für jede SIR-Population mit den Namen sus (S), inf (I) und rec (R)
zeros = np.zeros(len(cities))
combined = list(zip(zeros, cities))
combined_sus = list(zip(population, cities))
exp = np.array(combined, dtype=object)
sus = np.array(combined_sus, dtype=object)    #sus erhält als Startwert die jeweiligen Populationen,
inf = np.array(combined, dtype=object)        #denn jeder kann anfangs infiziert werden
rec = np.array(combined, dtype=object)        #dtype Object, damit wir zwei verschiedene Datentypen im Array
des = np.array(combined, dtype=object)        #speichern können (Floats - erste Spalte, Strings - zweite Spalte)
                                              #zudem haben wir nun eine dritte Gruppe, die Exponierten, also infizierten aber nicht ansteckenden
                                              #und eine vierte Gruppe, die an der Krankheit verstorbenen

mu = 3e-5   #allgemeine Sterberate
beta = 0.1  #Infektionsparameter
gamma = 0.07    #Erhohlungsrate
psi = 0.01   # Wahrscheinlichkeit, dass ein infizierter an der Krankheit stirbt, hier z.B. 1%
sigma = 0.2  # Rate/Geschwindigkeit, mit der exponierte Personen infektiös werden (Inkubationszeit)


# SIR-Modell-Differentialgleichungen mit Impfungen
def SIR(x, t):
    S, I, R, D, E = x
    N = S + I + R + D + E
    dS = -beta * S * I / N
    dE = beta * S * I / N - sigma * E - mu * E
    dI = sigma * E - gamma * I - psi * I - mu * I
    dR = gamma * I - mu * R
    dD = psi * I + mu * (E + I + R)
    return [dS, dI, dR, dD, dE]

# Euler-Verfahren
def infectEuler(x):
    h = 1
    x += h * np.array(SIR(x, 0))
    return x

# Runge-Kutta-Verfahren vierter Ordnung
def infectRK4(x):
    h = 1
    x = np.array(x)  # Sicherstellen, dass x ein numpy-Array ist
    k1 = h * np.array(SIR(x, 0))
    k2 = h * np.array(SIR(x + 0.5 * k1, 0))
    k3 = h * np.array(SIR(x + 0.5 * k2, 0))
    k4 = h * np.array(SIR(x + k3, 0))
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x

# Nutzen der odeint-Methode von SciPy
def infectODEsolver(x, t):
    deltat = np.array([t, t + 1], dtype=float)
    x = odeint(SIR, x, deltat)
    return x[-1]  # Wir interessieren uns nur für den Endwert nach einem Zeitschritt

# SIR-Modell mit Euler-Verfahren für alle Städte
def infectEulerAll(Sus, Inf, Rec, Des, Exp):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Des[i], Exp[i]]
        result = infectEuler(np.array(x))
        Sus[i], Inf[i], Rec[i], Des[i], Exp[i] = result

# SIR-Modell mit Runge-Kutta-Verfahren für alle Städte
def infectRK4All(Sus, Inf, Rec, Des, Exp):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Des[i], Exp[i]]
        result = infectRK4(np.array(x))
        Sus[i], Inf[i], Rec[i], Des[i] , Exp[i]= result

# SIR-Modell mit odeint für alle Städte
def infectODEsolverAll(Sus, Inf, Rec, Des, Exp):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Des[i], Exp[i]]
        result = infectODEsolver(np.array(x), 0)
        Sus[i], Inf[i], Rec[i], Des[i], Exp[i] = result

