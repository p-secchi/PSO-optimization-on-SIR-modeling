import matplotlib.pyplot as plt
import numpy as np
import random2 as rd

#---------------------------------------------------------------------------------------------------------------------------

BMN = [0.463150569, 0.207069916, 0.105240751, 0.036859846]

gamma = 0.05
pabw = 0

NI_t_real = [304,321,448,503,757,984,1336,2021,2573,3237,3601,4356,4433,4678,6016,5235,5288,4725,5329,4442,3818,5157,4076,4418,3998,4122,3888,3261,4394,3574,4040,3724,3730,3006,2700,3342,3054,2872,2700,2326,2016,1952,1887,1952,1940,1751,1642,1433,1310,1578,1350,1293,1268,1146,1007,904,1100,942,866,936,816,741,755,890,815,744,705,679,580,556,666,621,589,528,678,560,442,615,466,562,389,387,366,371,468,435,454,378,347,291,269,327,439,400,342,319,300,231,409,450,433]
# echte Neuinfektionen

#---------------------------------------------------------------------------------------------------------------------------

N = 8 * 10**7 # Gesamtbevölkerung
I_0 = 304 # Startwert der Infektionen
T = len(NI_t_real)-1 # Anzahl Tage

TMN = [0, 10, 17, 24] # Zeitpunkte für die Einführung der Maßnahmen
MN = ['Keine Maßnahmen', 'Erste Maßnahmen', 'Zweite Maßnahmen', 'Kontaktverbot']

#---------------------------------------------------------------------------------------------------------------------------

S = []
I = []
R = []
IN = []

NT = T 
t = T/NT

def K(x):
    for i in range(x):
        if i == 0:
            S.append(N - (I_0))
            I.append(I_0)
            R.append(0)
            IN.append(I_0)
        
        else:
            for j in range(len(TMN)-1):
                if i < TMN[j+1]:
                    if i >= TMN[j]:
                        beta=BMN[j]
                        k_s1=(-beta*S[i-1]*I[i-1])/N
                        k_I1=(beta*S[i-1]*I[i-1])/N - gamma*I[i-1]
                        k_in1=(beta*S[i-1]*I[i-1])/N
                        k_r1= gamma*I[i-1]
                        k_s2=-(beta/N)*(S[i-1]+(k_s1*t)/2)*(I[i-1]+(k_I1*t)/2)
                        k_I2= (beta/N)*(S[i-1]+(k_s1*t)/2)*(I[i-1]+(k_I1*t)/2)-gamma*(I[i-1]+(k_I1*t)/2)
                        k_in2= (beta/N)*(S[i-1]+(k_s1*t)/2)*(I[i-1]+(k_I1*t)/2)
                        k_r2= gamma*(I[i-1]+(k_I1*t)/2)
                        k_s3=-(beta/N)*(S[i-1]+(k_s2*t)/2)*(I[i-1]+(k_I2*t)/2)
                        k_I3= (beta/N)*(S[i-1]+(k_s2*t)/2)*(I[i-1]+(k_I2*t)/2)-gamma*(I[i-1]+(k_I2*t)/2)
                        k_in3= (beta/N)*(S[i-1]+(k_s2*t)/2)*(I[i-1]+(k_I2*t)/2)
                        k_r3= gamma*(I[i-1]+(k_I2*t)/2)
                        k_s4=-(beta/N)*(S[i-1]+k_s3*t)*(I[i-1]+k_I3*t)
                        k_I4=(beta/N)*(S[i-1]+k_s3*t)*(I[i-1]+k_I3*t)-gamma*(I[i-1]+k_I3*t)
                        k_in4= (beta/N)*(S[i-1]+k_s3*t)*(I[i-1]+k_I3*t)
                        k_r4= gamma*(I[i-1]+k_I3*t)
                        
                        s_neu = (S[i-1]+ (t/6)*(k_s1 + 2*k_s2 + 2*k_s3 + k_s4))
                        i_neu = (I[i-1]+(t/6)*(k_I1+2*k_I2+2*k_I3+k_I4))
                        r_neu = (R[i-1]+(t/6)*(k_r1+2*k_r2+2*k_r3+k_r4))
                        in_neu = ((t/6)*(k_in1+2*k_in2+2*k_in3+k_in4))
                        if s_neu < 0:
                            S.append(0)
                        else:
                            S.append(s_neu)
                        if i_neu < 0:
                            I.append(0)
                        elif i_neu > N:
                            I.append(N)
                        else:
                            I.append(i_neu)
                        if r_neu < 0:
                            R.append(0)
                        elif r_neu > N:
                            R.append(N)
                        else:
                            R.append(r_neu)
                        if in_neu < 0:
                            IN.append(0)
                        else:
                            IN.append(in_neu)
            
            if i >= TMN[len(TMN)-1]:
                beta=BMN[len(TMN)-1]
                k_s1=(-beta*S[i-1]*I[i-1])/N
                k_I1=(beta*S[i-1]*I[i-1])/N - gamma*I[i-1]
                k_in1=(beta*S[i-1]*I[i-1])/N
                k_r1= gamma*I[i-1]
                k_s2=-(beta/N)*(S[i-1]+(k_s1*t)/2)*(I[i-1]+(k_I1*t)/2)
                k_I2= (beta/N)*(S[i-1]+(k_s1*t)/2)*(I[i-1]+(k_I1*t)/2)-gamma*(I[i-1]+(k_I1*t)/2)
                k_in2= (beta/N)*(S[i-1]+(k_s1*t)/2)*(I[i-1]+(k_I1*t)/2)
                k_r2= gamma*(I[i-1]+(k_I1*t)/2)
                k_s3=-(beta/N)*(S[i-1]+(k_s2*t)/2)*(I[i-1]+(k_I2*t)/2)
                k_I3= (beta/N)*(S[i-1]+(k_s2*t)/2)*(I[i-1]+(k_I2*t)/2)-gamma*(I[i-1]+(k_I2*t)/2)
                k_in3= (beta/N)*(S[i-1]+(k_s2*t)/2)*(I[i-1]+(k_I2*t)/2)
                k_r3= gamma*(I[i-1]+(k_I2*t)/2)
                k_s4=-(beta/N)*(S[i-1]+k_s3*t)*(I[i-1]+k_I3*t)
                k_I4=(beta/N)*(S[i-1]+k_s3*t)*(I[i-1]+k_I3*t)-gamma*(I[i-1]+k_I3*t)
                k_in4= (beta/N)*(S[i-1]+k_s3*t)*(I[i-1]+k_I3*t)
                k_r4= gamma*(I[i-1]+k_I3*t)
            
                s_neu = (S[i-1]+ (t/6)*(k_s1 + 2*k_s2 + 2*k_s3 + k_s4))
                i_neu = (I[i-1]+(t/6)*(k_I1+2*k_I2+2*k_I3+k_I4))
                r_neu = (R[i-1]+(t/6)*(k_r1+2*k_r2+2*k_r3+k_r4))
                in_neu = ((t/6)*(k_in1+2*k_in2+2*k_in3+k_in4))
                if s_neu < 0:
                    S.append(0)
                else:
                    S.append(s_neu)
                if i_neu < 0:
                    I.append(0)
                elif i_neu > N:
                    I.append(N)
                else:
                    I.append(i_neu)
                if r_neu < 0:
                    R.append(0)
                elif r_neu > N:
                    R.append(N)
                else:
                    R.append(r_neu)
                if in_neu < 0:
                    IN.append(0)
                else:
                    IN.append(in_neu)
                
K(T+1)

S_M = S
I_M = I
R_M = R
IN_M = IN
BMN_M = BMN
gamma_M = gamma

S = []
I = []
R = []
IN = []

BMN = [BMN_M[0] * (1 - pabw), BMN_M[1] * (1 - pabw), BMN_M[2] * (1 - pabw), BMN_M[3] * (1 - pabw)]
gamma = min(gamma_M * (1 + pabw), 0.15)

K(T+1)

S_U = S
I_U = I
R_U = R
IN_U = IN
BMN_U = BMN
gamma_U = gamma

S = []
I = []
R = []
IN = []

BMN = [BMN_M[0] * (1 + pabw), BMN_M[1] * (1 + pabw), BMN_M[2] * (1 + pabw), BMN_M[3] * (1 + pabw)]
gamma = max(gamma_M * (1 - pabw), 0.05)

K(T+1)

S_O = S
I_O = I
R_O = R
IN_O = IN
BMN_O = BMN
gamma_O = gamma


fig, axs = plt.subplots(2)

fig.text(.5,.05,"BMN = %s" %BMN_M,ha='center')
fig.text(.5,.03,"gamma = %s" %gamma_M,ha='center')
fig.text(.5,.01,"Fehler = %s" %(pabw),ha='center')

axs[0].plot(np.linspace(0, len(NI_t_real)-1, len(NI_t_real)), IN_M, label='Approximation')
#axs[0].fill_between(np.linspace(0, len(NI_t_real)-1, len(NI_t_real)), IN_U, IN_O, color='lavender', label='Abweichung')
axs[0].plot(np.linspace(0, len(NI_t_real)-1, len(NI_t_real)), NI_t_real, label='Realwerte')
axs[0].title.set_text('Tägliche Neuinfektionen')
axs[0].legend()

axs[1].plot(np.linspace(0, T, T+1), I_M, label='Infectious')
axs[1].plot(np.linspace(0, T, T+1), R_M, label='Removed')
#axs[1].fill_between(np.linspace(0, len(NI_t_real)-1, len(NI_t_real)), R_U, R_O, color='ivory', label='Abweichung (R)')
#axs[1].fill_between(np.linspace(0, len(NI_t_real)-1, len(NI_t_real)), I_U, I_O, color='lavender', label='Abweichung (I)')
axs[1].title.set_text('Modellverlauf')
axs[1].legend()

plt.show()