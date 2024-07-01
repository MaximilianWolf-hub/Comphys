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
                                              #speichern können (Floats - erste Spalte, Strings - zweite Spalte)

mu = 1
beta = 1
gamma = 1


def SIR(S, I, R):   #Wir definieren das SIR-Modell, bzw. die DGL, welche es zu lösen gilt
    N = S + I + R
    dS = - beta * S * I / N + mu * (N - S)
    dI = beta * S * I / N - gamma * I - mu * I
    dR = gamma * I - mu * R
    return np.array([dS, dI, dR], dtype=float)


#Eulerverfahren
def infectEuler(x):
    h = 1
    x += h * SIR(x)
    return x


#Runge-Kutta-Verfahren vierter Ordnung
def infectRK4(x):       #Übergebe ein Array mit den S, I, R für eine Stadt
    h = 1   #Schrittweite = ein Tag

    k1 = h * SIR(x)
    k2 = h * SIR(x + 0.5 * k1)
    k3 = h * SIR(x + k2 * 0.5)
    k4 = h * SIR(x + k3)

    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x


#Nutzen der Ode-Int Methode von Scipy
def infectODEsolver(x, t):
    deltat = np.array([t, t + 1], dtype=float)
    x = odeint(SIR, x, deltat)
    return x[-1]  # Wir interessieren uns nur für den Endwert nach einem Zeitschritt

#SIR Modell mit Euler Verfahren fur alle Städte
def infectEulerAll():
    for i in range(len(cities)):
        x = [sus[i][0], inf[i][0], rec[i][0]]
        result = infectEuler(np.array(x))
        sus[i][0], inf[i][0], rec[i][0] = result


#SIR Modell mit Runge-Kutta Verfahren fur alle Städte
def infectRK4All():
    for i in range(len(cities)):
        x = [sus[i][0], inf[i][0], rec[i][0]]
        result = infectRK4(np.array(x))
        sus[i][0], inf[i][0], rec[i][0] = result


#SIR Modell mit ode/odeint fur alle Städte
def infectODEsolverAll():
    for i in range(len(cities)):
        x = [sus[i][0], inf[i][0], rec[i][0]]
        result = infectODEsolver(np.array(x), 0)
        sus[i][0], inf[i][0], rec[i][0] = result

