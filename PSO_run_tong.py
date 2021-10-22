import matplotlib.pyplot as plt
import numpy as np
import random2 as rd

def K(x):
    S=[]
    I=[]
    R=[]
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
                


Beta=[]
Gamma=[]
BetaStart=[]
GammaStart=[]
FitP=[]
FitG=[]
BestP=[]
BestG=[]
BestInd = 0
BestFit = []
BestPI = []
for l in range(SG):
    BMN=[]
    for i in range(len(TMN)):
        BMN.append(rd.random())
    y=rd.random()*0.1+0.05
    BetaStart.append(BMN)
    GammaStart.append(y)
    gamma = y
    IN = []
    K(T+1)
    F = 0
    for j in range(len(NI_t_real)):
        F = F + (IN[j] - NI_t_real[j])**2
    Fit = F**0.5
    FitP.append(Fit)
    if l == 0:
        Fitg = Fit
        BestInd = 0
    else:
        if Fit < Fitg:
            Fitg = Fit
            BestInd = l
    BestPI.append(0)
BestFit.append(Fitg)
BestP.append(BestPI)
BestG.append([0, BestInd])
Beta.append(BetaStart)    
Gamma.append(GammaStart)


for n in range(It):
    Betan=[]
    Gamman=[]
    Fitg = BestFit[n]
    BestPI = []
    if n == It-1:
        print("0")
        print(" ")
    elif n%OI == 0:
        print(It-n, end =" ")
        if (n+1)%100 == 0:
            print(" ")
    else:
        if (n+1)%100 == 0:
            print(" ")
    for l in range(SG):
        U1 = []
        U2 = []
        for i in range(len(TMN)+1):
            U1.append(rd.random())
            U2.append(rd.random())
        BMNL = []
        BMN = []
        if n == 0:
            for i in range(len(TMN)):
                rv = rd.random()
                BMNL.append(Beta[n][l][i] + theta*rv + c1*U1[i]*(Beta[n][BestP[n][l]][i]-Beta[n][l][i]) + c2*U2[i]*(Beta[n][BestG[0][1]][i]-Beta[n][l][i]))
            rv = rd.random()
            y = Gamma[n][l] + theta*rv + c1*U1[len(TMN)]*(Gamma[n][BestP[n][l]]-Gamma[n][l]) + c2*U2[len(TMN)]*(Gamma[n][BestG[0][1]]-Gamma[n][l])
        else:
            for i in range(len(TMN)):
                BMNL.append(Beta[n][l][i] + theta*(Beta[n][l][i]-Beta[n-1][l][i]) + c1*U1[i]*(Beta[n][BestP[n][l]][i]-Beta[n][l][i]) + c2*U2[i]*(Beta[BestG[n][0]][BestG[n][1]][i]-Beta[n][l][i]))
            y = Gamma[n][l] + theta*(Gamma[n][l]-Gamma[n-1][l]) + c1*U1[len(TMN)]*(Gamma[n][BestP[n][l]]-Gamma[n][l]) + c2*U2[len(TMN)]*(Gamma[BestG[n][0]][BestG[n][1]]-Gamma[n][l])
        for i in range(len(TMN)):
            if BMNL[i] > 1:
                BMN.append(1)
            elif BMNL[i]  < 0:
                BMN.append(0)
            else:
                BMN.append(BMNL[i])
        if y > 0.15:
            y=0.15
        elif y  < 0.05:
            y=0.05
        Betan.append(BMN)
        Gamman.append(y)
        gamma = y
        IN = []
        K(T+1)
        F = 0
        for j in range(len(NI_t_real)):
            F = F + (IN[j] - NI_t_real[j])**2
        Fit = F**0.5
        if Fit < BestP[n][l]:
            BestPI.append(n+1)
        else:
            BestPI.append(BestP[n][l])
        if Fit < Fitg:
            Fitg = Fit
            BestInd = l
    Beta.append(Betan)
    Gamma.append(Gamman)
    BestP.append(BestPI)
    BestFit.append(Fitg)
    if Fitg < BestFit[n]:
        BestG.append([n+1, BestInd])
    else:
        BestG.append(BestG[n])

            
BMN = Beta[BestG[It][0]][BestG[It][1]]
gamma = Gamma[BestG[It][0]][BestG[It][1]]
IN = []

K(T+1)

NI_w_real = []
NI_w = []
Il_real = 0
Il = 0
    
for i in range(len(NI_t_real)):
    if i == 0:
        NI_w_real.append(NI_t_real[0])
        NI_w.append(IN[0])
    elif i < len(NI_t_real)-1:
        if i%7 > 0:
            Il_real = Il_real + NI_t_real[i]
            Il = Il + IN[i]
        else:
            NI_w_real.append(Il_real)
            Il_real = NI_t_real[i]
            NI_w.append(Il)
            Il = IN[i]
    else:
        NI_w_real.append(Il_real)
        NI_w.append(Il)

for j in range(len(NI_w_real)):
    F = F + (NI_w_real[j] - NI_w[j])**2
Fit_w = F**0.5

Diff = 0
IN_ges = 0
for j in range(len(NI_t_real)):
    Diff = Diff + IN[j] - NI_t_real[j]
    IN_ges = IN_ges + NI_t_real[j]
Abw = abs(Diff/IN_ges)

print(BMN, gamma, Abw)
