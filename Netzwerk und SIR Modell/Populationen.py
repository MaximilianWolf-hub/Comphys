import numpy as np
from city_data import staedte, einwohner, laender, breitengrad, laengengrad

landverkehr = np.loadtxt("landverkehr.txt", dtype=str, encoding="utf-8", skiprows=1, delimiter='\t')
flugverkehr = np.loadtxt(f"flugverkehr.txt", dtype=str, encoding="utf-8", delimiter='\t', skiprows=1)


