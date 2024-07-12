import numpy as np

# Gefittete Werte von C und D sowie ihre Unsicherheiten
coefficients_C = np.array([148.3544439426628, 0.8364302092998285, 1.1468796423098384,
                           2.0436985101608833, 0.836362743573689, -4.027492330174196, -0.10740873167461619,
                           -0.1298747826343872, -0.3605492201411149, 1.1137123666049429, -0.3507638528367353,
                           -0.1417280428956056, -0.5272265423748487, -0.028568415980470767, 0.11313543797015604,
                           -0.07118165550140172, -0.03723818897021762, -0.12283619271543404, -0.025131187518731266])

errors_C = np.array([0.6584042598265973, 0.46218426850262656, 0.4383302432718888,
                     0.45980533763112685, 0.4654889560181339, 0.46644117890049747, 0.46093413898445795,
                     0.4546486802867936, 0.4671953830051102, 0.4539946222207847, 0.4422932435014157,
                     0.45356397130597054, 0.463807597841296, 0.46551720663099316, 0.4621966761427097,
                     0.4666724984605514, 0.47294989905737667, 0.4588974511077617, 0.4455703033284666])

coefficients_D = np.array([0.566940771873932, 0.35810474319343094, 0.7321631581345506, -0.5814854340086469,
                           1.9882055793482172, -1.5211650054306496, 0.9303634821615013, -0.1933836696328291,
                           0.21013542233636115, 0.38103212093421784, 0.5284042296557919, -0.3958312535474161,
                           0.3638324806716155, 0.22648257639744504, -0.12448025769161028, 0.490593449113487,
                           0.07486225032453828, -0.07114411995603849, 0.1842014241455037])

errors_D = np.array([0.46622344950367955, 0.46107919755197385, 0.46093453509558363, 0.44958824152211996,
                     0.4624782012028237, 0.4660644945621699, 0.4551137660223803, 0.4608624258445787,
                     0.4493068569196146, 0.4603165223333752, 0.45291404500540583, 0.44736799833733343,
                     0.4360676594637262, 0.4651612268936313, 0.44914996515949135, 0.4661874204314783,
                     0.4532527633061108, 0.44875592631660105, 0.44276876300859896])

# Berechnung der Magnituden
magnitude_C = -2.5 * np.log10(np.abs(coefficients_C))
magnitude_D = -2.5 * np.log10(np.abs(coefficients_D))

# Berechnung der Magnitudendifferenzen
delta_magnitude = magnitude_C - magnitude_D

# Berechnung der Unsicherheiten in den Magnitudendifferenzen (vereinfachte Annahme)
uncertainty_magnitude_C = 2.5 * errors_C / np.log(10) / np.abs(coefficients_C)
uncertainty_magnitude_D = 2.5 * errors_D / np.log(10) / np.abs(coefficients_D)
uncertainty_delta_magnitude = np.sqrt(uncertainty_magnitude_C**2 + uncertainty_magnitude_D**2)

# Berechnung des Mittelwerts und seiner Unsicherheit
mean_delta_magnitude = np.mean(delta_magnitude)
std_delta_magnitude = np.std(delta_magnitude, ddof=1)  # Verwendung von ddof=1 für Bessel-Korrektur

# Berechnung der Unsicherheit des Mittelwerts
sem_delta_magnitude = std_delta_magnitude / np.sqrt(len(delta_magnitude))

# Ausgabe der Ergebnisse
print(f"Mittelwert der Magnitudendifferenzen (ohne C1 und D1): {mean_delta_magnitude:.3f} ± {sem_delta_magnitude:.3f}")


