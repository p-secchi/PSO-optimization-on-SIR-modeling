import matplotlib.pyplot as plt
import numpy as np
import random2 as rd

DG = 50 # Anzahl Durchläufe des ges. Skripts
DIt = 5 # Anzahl Iterationen mit jedem Datensatz
SG = 200 # Schwarmgröße
It = 200 # Anzahl Iterationen
OI = 5 # Output-Intervalle für den print-Befehl

theta = 0.72984 # Faktor für vorherige Bewegung
c1 = 1.496172 # Faktor für Bewegung zum persönlichen Bestwert
c2 = 1.496172 # Faktor für Bewegung zum globalen Bestwert

#------------------------------------------------------------------------------------------------

N = 8 * 10**7 # Gesamtbevölkerung
I_0 = 304 # Startwert der Infektionen
T = 100 # Anzahl Tage

TMN = [0, 12, 19, 26] # Zeitpunkte für die Einführung der Maßnahmen
MN = ['Keine Maßnahmen', 'Erste Maßnahmen', 'Zweite Maßnahmen', 'Kontaktverbot']

#------------------------------------------------------------------------------------------------

file = open("Ergebnisse_tong.txt","w+")

file.write("Durchgänge: %s"%DG)
file.write(" ; Schwarmgröße: %s"%SG)
file.write(" ; Iterationen: %s"%It)
file.write(" ; theta: %s"%theta)
file.write(" ; c1: %s"%c1)
file.write(" ; c2: %s"%c2)
file.write("\n")


secfile = open("Fit_tong.txt","w+")

secfile.write("Durchgänge: %s"%DG)
secfile.write(" ; Schwarmgröße: %s"%SG)
secfile.write(" ; Iterationen: %s"%It)
secfile.write(" ; theta: %s"%theta)
secfile.write(" ; c1: %s"%c1)
secfile.write(" ; c2: %s"%c2)
secfile.write("\n")
secfile.write("\n")

tripfile = open("ParFit_tong.txt","w+")

tripfile.write("Durchgänge: %s"%DG)
tripfile.write(" ; Schwarmgröße: %s"%SG)
tripfile.write(" ; Iterationen: %s"%It)
tripfile.write(" ; theta: %s"%theta)
tripfile.write(" ; c1: %s"%c1)
tripfile.write(" ; c2: %s"%c2)
tripfile.write("\n")
tripfile.write("\n")

Out_D = []  #
Out_Max = []#
Out_Min = []#

Out2_D = []  #
Out2_Max = []#
Out2_Min = []#

NT = T 
t = T/NT

for n in range(DG):
    BMN = []
    gamma = rd.random()*0.1+0.05
    for j in range(4):
        BMN.append(rd.random())
    SetBMN = BMN
    Setgamma = gamma
    exec(open("SIR Validierungswerte.py").read())
    y = n+1
    x_neu = n+1
    secfile.write("\n Durchgang %s"%y)
    secfile.write(" ; BMN = %s"%BMN)
    secfile.write(" ; gamma = %s \n"%gamma)
    tripfile.write("\n Durchgang %s"%y)
    tripfile.write(" ; BMN = %s"%BMN)
    tripfile.write(" ; gamma = %s \n"%gamma)
    file.write("\n Durchgang %s"%y)
    file.write(" ; BMN = %s"%BMN)
    file.write(" ; gamma = %s \n"%gamma)
    print("Durchgang", y, "/ %s: \n"%DG)
    Out = [] #
    Out2 = []#
    for i in range(DIt):
        x = i+1
        Out_l = [] #
        Out2_l = []#
        print("Durchlauf", x, "/ %s"%DIt, "(%s): \n"%x_neu) 
        exec(open("PSO_run_tong.py").read())
        tripfile.write("%s ; "%x)
        secfile.write("%s ; "%x)
        for j in range(len(BestFit)):
            secfile.write("%s ; "%BestFit[j])
            Out_l.append(BestFit[j])#
            FitPar = 0
            for m in range(len(SetBMN)):
                FitPar = FitPar + abs((SetBMN[m] - Beta[BestG[j][0]][BestG[j][1]][m])/SetBMN[m])
            FitPar = FitPar + abs((Setgamma - Gamma[BestG[j][0]][BestG[j][1]])/Setgamma)
            FitPar = abs(FitPar/(len(SetBMN)+1))
            tripfile.write("%s ; "%FitPar)
            Out2_l.append(FitPar) #
        Out.append(Out_l) #
        Out2.append(Out2_l) #
        tripfile.write("\n")
        secfile.write("\n")
        file.write("%s"%x)
        file.write(" ; %s"%BMN)
        file.write(" ; %s"%gamma)
        file.write(" ; %s"%Abw)
        file.write(" ; %s"%BestFit[It])
        file.write(" ; %s"%Fit_w)
        file.write("\n")
        print("\n ----------------------------------------------------------------------------- \n")
    Out_D_l = []
    Out2_D_l = []
    Out_Max_l = []
    Out2_Max_l = []
    Out_Min_l = []
    Out2_Min_l = []
    for i in range(It+1):
        out_v = 0 #
        out2_v = 0#
        for j in range(DIt):
            out_v = out_v + Out[j][i]
            out2_v = out2_v + Out2[j][i]
        Out_D_l.append(out_v/DIt)
        Out2_D_l.append(out2_v/DIt)
        Out_Max_l.append(max(Out, key=lambda item: item[i])[i])
        Out2_Max_l.append(max(Out2, key=lambda item: item[i])[i])
        Out_Min_l.append(min(Out, key=lambda item: item[i])[i])
        Out2_Min_l.append(min(Out2, key=lambda item: item[i])[i])
    Out_D.append(Out_D_l)
    Out2_D.append(Out2_D_l)
    Out_Max.append(Out_Max_l)
    Out2_Max.append(Out2_Max_l)
    Out_Min.append(Out_Min_l)
    Out2_Min.append(Out2_Min_l)
    
    tripfile.write("Durchschnitt")
    for i in range(It+1):
        tripfile.write("; %s"%Out2_D_l[i])
    tripfile.write("\n")
    tripfile.write("Maximum")
    for i in range(It+1):
        tripfile.write("; %s"%Out2_Max_l[i])
    tripfile.write("\n")
    tripfile.write("Minimum")
    for i in range(It+1):
        tripfile.write("; %s"%Out2_Min_l[i])
    tripfile.write("\n")
    
    secfile.write("Durchschnitt")
    for i in range(It+1):
        secfile.write("; %s"%Out_D_l[i])
    secfile.write("\n")
    secfile.write("Maximum")
    for i in range(It+1):
        secfile.write("; %s"%Out_Max_l[i])
    secfile.write("\n")
    secfile.write("Minimum")
    for i in range(It+1):
        secfile.write("; %s"%Out_Min_l[i])
    secfile.write("\n")

Out_D_g = []
Out_Max_g = []
Out_Min_g = []

Out2_D_g = []
Out2_Max_g = []
Out2_Min_g = []

for i in range(It+1):
    out_D_v = 0
    out_Max_v = 0
    out_Min_v = 0

    out2_D_v = 0
    out2_Max_v = 0
    out2_Min_v = 0
    
    for j in range(DG):
        out_D_v = out_D_v + Out_D[j][i]
        out_Max_v = out_Max_v + Out_Max[j][i]
        out_Min_v = out_Min_v + Out_Min[j][i]
        out2_D_v = out2_D_v + Out2_D[j][i]
        out2_Max_v = out2_Max_v + Out2_Max[j][i]
        out2_Min_v = out2_Min_v + Out2_Min[j][i]
    
    Out_D_g.append(out_D_v/DG)
    Out_Max_g.append(out_Max_v/DG)
    Out_Min_g.append(out_Min_v/DG)
    Out2_D_g.append(out2_D_v/DG)
    Out2_Max_g.append(out2_Max_v/DG)
    Out2_Min_g.append(out2_Min_v/DG)
    
tripfile.write("\n")
secfile.write("\n")    
    
tripfile.write("Gesamtdurchschnitt")
for i in range(It+1):
    tripfile.write("; %s"%Out2_D_g[i])
tripfile.write("\n")
tripfile.write("Durchschnittliches Maximum")
for i in range(It+1):
    tripfile.write("; %s"%Out2_Max_g[i])
tripfile.write("\n")
tripfile.write("Durchschnittliches Minimum")
for i in range(It+1):
    tripfile.write("; %s"%Out2_Min_g[i])
tripfile.write("\n")
 
secfile.write("Gesamtdurchschnitt")
for i in range(It+1):
    secfile.write("; %s"%Out_D_g[i])
secfile.write("\n")
secfile.write("Durchschnittliches Maximum")
for i in range(It+1):
    secfile.write("; %s"%Out_Max_g[i])
secfile.write("\n")
secfile.write("Durchschnittliches Minimum")
for i in range(It+1):
    secfile.write("; %s"%Out_Min_g[i])
secfile.write("\n")

tripfile.close()
secfile.close()   
file.close()

print("Ende")
