DG = 50 # Anzahl Durchläufe des ges. Skripts
SG = 200 # Schwarmgröße
It = 200 # Anzahl Iterationen
OI = 5 # Output-Intervalle für den print-Befehl

NI_t_real = [304,321,448,503,757,984,1336,2021,2573,3237,3601,4356,4433,4678,6016,5235,5288,4725,5329,4442,3818,5157,4076,4418,3998,4122,3888,3261,4394,3574,4040,3724,3730,3006,2700,3342,3054,2872,2700,2326,2016,1952,1887,1952,1940,1751,1642,1433,1310,1578,1350,1293,1268,1146,1007,904,1100,942,866,936,816,741,755,890,815,744,705,679,580,556,666,621,589,528,678,560,442,615,466,562,389,387,366,371,468,435,454,378,347,291,269,327,439,400,342,319,300,231,409,450,433]
# echte Neuinfektionen

#------------------------------------------------------------------------------------------------

N = 8 * 10**7 # Gesamtbevölkerung
I_0 = 304 # Startwert der Infektionen
T = len(NI_t_real)-1 # Anzahl Tage

TMN = [0, 10, 17, 24] # Zeitpunkte für die Einführung der Maßnahmen
MN = ['Keine Maßnahmen', 'Erste Maßnahmen', 'Zweite Maßnahmen', 'Kontaktverbot']

#------------------------------------------------------------------------------------------------

file = open("Ergebnisse_eig_real.txt","w+")

file.write("Durchgänge: %s"%DG)
file.write(" ; Schwarmgröße: %s"%SG)
file.write(" ; Iterationen: %s"%It)
file.write("\n")
file.write("Durchlauf; Beta 0; Beta 1; Beta 2; Beta 3; Gamma; Abweichung; Fit (tägl.); Fit (wöchentl.)")
file.write("\n")

secfile = open("Fit_eig_real.txt","w+")

secfile.write("Durchgänge: %s"%DG)
secfile.write(" ; Schwarmgröße: %s"%SG)
secfile.write(" ; Iterationen: %s"%It)
secfile.write("\n")

BMN0 = []
BMN1 = []
BMN2 = []
BMN3 = []
Gam = []
Out = []

NT = T 
t = T/NT

for n in range(DG):
    x = n+1
    Out_l = [] #
    print("Durchgang", x, "/ %s: \n"%DG)
    exec(open("PSO_run_eig.py").read())
    BMN0.append(BMN[0])
    BMN1.append(BMN[1])
    BMN2.append(BMN[2])
    BMN3.append(BMN[3])
    Gam.append(gamma)
    secfile.write("%s ; "%x)
    for j in range(len(BestFit)):
        secfile.write("%s ; "%BestFit[j])
        Out_l.append(BestFit[j])#
    Out.append(Out_l) #
    secfile.write("\n")
    file.write("%s"%x)
    file.write(" ; %s"%BMN[0])
    file.write(" ; %s"%BMN[1])
    file.write(" ; %s"%BMN[2])
    file.write(" ; %s"%BMN[3])
    file.write(" ; %s"%gamma)
    file.write(" ; %s"%Abw)
    file.write(" ; %s"%BestFit[It])
    file.write(" ; %s"%Fit_w)
    file.write("\n")
    print("\n ----------------------------------------------------------------------------- \n")

BMN0_D = sum(BMN0)/DG
BMN1_D = sum(BMN1)/DG
BMN2_D = sum(BMN2)/DG
BMN3_D = sum(BMN3)/DG
Gam_D = sum(Gam)/DG

BMN0_Max = max(BMN0)
BMN1_Max = max(BMN1)
BMN2_Max = max(BMN2)
BMN3_Max = max(BMN3)
Gam_Max = max(Gam)

BMN0_Min = min(BMN0)
BMN1_Min = min(BMN1)
BMN2_Min = min(BMN2)
BMN3_Min = min(BMN3)
Gam_Min = min(Gam)

file.write("\nDurchschnitt")
file.write("; %s"%BMN0_D)
file.write("; %s"%BMN1_D)
file.write("; %s"%BMN2_D)
file.write("; %s"%BMN3_D)
file.write("; %s"%Gam_D)
file.write("\n")
file.write("Maximum")
file.write("; %s"%BMN0_Max)
file.write("; %s"%BMN1_Max)
file.write("; %s"%BMN2_Max)
file.write("; %s"%BMN3_Max)
file.write("; %s"%Gam_Max)
file.write("\n")
file.write("Minimum")
file.write("; %s"%BMN0_Min)
file.write("; %s"%BMN1_Min)
file.write("; %s"%BMN2_Min)
file.write("; %s"%BMN3_Min)
file.write("; %s"%Gam_Min)
file.write("\n")

Out_D = []
Out_Max = []
Out_Min = []
for i in range(It+1):
    out_v = 0 
    for j in range(DG):
        out_v = out_v + Out[j][i]
    Out_D.append(out_v/DG)
    Out_Max.append(max(Out, key=lambda item: item[i])[i])
    Out_Min.append(min(Out, key=lambda item: item[i])[i])
  
secfile.write("\nDurchschnitt")
for i in range(It+1):
    secfile.write("; %s"%Out_D[i])
secfile.write("\n")
secfile.write("Maximum")
for i in range(It+1):
    secfile.write("; %s"%Out_Max[i])
secfile.write("\n")
secfile.write("Minimum")
for i in range(It+1):
    secfile.write("; %s"%Out_Min[i])
secfile.write("\n")

secfile.close()   
file.close()

print("Ende")