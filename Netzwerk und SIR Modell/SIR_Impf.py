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


def SIR(x, t=0):
    S, I, R ,V = x
    N = S + I + R + V
    dS = - beta * S * I / N + mu * (N - S) - vac_rate * S  # Die S-Population nimmt nun zusätzlich durch Impfungen an, die sich nicht anstecken können
    dI = beta * S * I / N - gamma * I - mu * I
    dR = gamma * I - mu * R
    dV = vac_rate * S - mu * V      # Wir nehmen an, dass sich alle aus der S Population mit Wahrscheinlichkeit "vac_rate"
                                    # impfen lassen
    return [dS, dI, dR, dV]


#Eulerverfahren
def infectEuler(x):
    h = 1
    x += h * np.array(SIR(x))
    return x


#Runge-Kutta-Verfahren vierter Ordnung
def infectRK4(x):
    h = 1
    x = np.array(x)  # Sicherstellen, dass x ein numpy-Array ist
    k1 = h * np.array(SIR(x))
    k2 = h * np.array(SIR(x + 0.5 * k1))
    k3 = h * np.array(SIR(x + 0.5 * k2))
    k4 = h * np.array(SIR(x + k3))
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x


#Nutzen der Ode-Int Methode von Scipy
def infectODEsolver(x, t):
    deltat = np.array([t, t + 1], dtype=float)
    x = odeint(SIR, x, deltat)
    return x[-1]  # Wir interessieren uns nur für den Endwert nach einem Zeitschritt

#SIR Modell mit Euler Verfahren fur alle Städte
def infectEulerAll(Sus, Inf, Rec, Vac):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Vac[i]]
        result = infectEuler(np.array(x))
        Sus[i], Inf[i], Rec[i], Vac[i] = result


#SIR Modell mit Runge-Kutta Verfahren fur alle Städte
def infectRK4All(Sus, Inf, Rec, Vac):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Vac[i]]
        result = infectRK4(np.array(x))
        Sus[i], Inf[i], Rec[i], Vac[i] = result


#SIR Modell mit ode/odeint fur alle Städte
def infectODEsolverAll(Sus, Inf, Rec, Vac):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i], Vac[i]]
        result = infectODEsolver(np.array(x), 0)
        Sus[i], Inf[i], Rec[i], Vac[i] = result

