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

mu = 3e-5           #das sind die Parameter unserer Epedemie, die wir hier anpassen können
beta = 0.1            # beta ist der Ansteckungsparameter, mu die Sterbe- und Reproduktionsrate und gamma die Erhohlungsrate
gamma = 0.07


def SIR(x, t=0):        # diese DGL möchten wir numerisch lösen
    S, I, R = x
    N = S + I + R
    dS = - beta * S * I / N + mu * (N - S)
    dI = beta * S * I / N - gamma * I - mu * I
    dR = gamma * I - mu * R
    return [dS, dI, dR]


#Eulerverfahren für eine Stadt
def infectEuler(x):
    h = 1
    x += h * np.array(SIR(x))
    return x


#Runge-Kutta-Verfahren vierter Ordnung für eine Stadt
def infectRK4(x):
    h = 1
    x = np.array(x)  # Sicherstellen, dass x ein numpy-Array ist
    k1 = h * np.array(SIR(x))
    k2 = h * np.array(SIR(x + 0.5 * k1))
    k3 = h * np.array(SIR(x + 0.5 * k2))
    k4 = h * np.array(SIR(x + k3))
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x


#Nutzen der Ode-Int Methode von Scipy für eine Stadt
def infectODEsolver(x, t):
    deltat = np.array([t, t + 1], dtype=float)
    x = odeint(SIR, x, deltat)
    return x[-1]  # Wir interessieren uns nur für den Endwert nach einem Zeitschritt

#SIR Modell mit Euler Verfahren fur alle Städte
def infectEulerAll(Sus, Inf, Rec):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i]]
        result = infectEuler(np.array(x))
        Sus[i], Inf[i], Rec[i] = result


#SIR Modell mit Runge-Kutta Verfahren fur alle Städte
def infectRK4All(Sus, Inf, Rec):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i]]
        result = infectRK4(np.array(x))
        Sus[i], Inf[i], Rec[i] = result


#SIR Modell mit ode/odeint fur alle Städte
def infectODEsolverAll(Sus, Inf, Rec):
    for i in range(len(cities)):
        x = [Sus[i], Inf[i], Rec[i]]
        result = infectODEsolver(np.array(x), 0)
        Sus[i], Inf[i], Rec[i] = result

