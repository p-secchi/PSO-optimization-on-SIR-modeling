import matplotlib.pyplot as plt
import numpy as np
import random2 as rd

IN = []

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
            
                        S.append(S[i-1]+ (t/6)*(k_s1 + 2*k_s2 + 2*k_s3 + k_s4))
                        I.append(I[i-1]+(t/6)*(k_I1+2*k_I2+2*k_I3+k_I4))
                        R.append(R[i-1]+(t/6)*(k_r1+2*k_r2+2*k_r3+k_r4))
                        IN.append((t/6)*(k_in1+2*k_in2+2*k_in3+k_in4))
            
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
            
                S.append(S[i-1]+ (t/6)*(k_s1 + 2*k_s2 + 2*k_s3 + k_s4))
                I.append(I[i-1]+(t/6)*(k_I1+2*k_I2+2*k_I3+k_I4))
                R.append(R[i-1]+(t/6)*(k_r1+2*k_r2+2*k_r3+k_r4))
                IN.append((t/6)*(k_in1+2*k_in2+2*k_in3+k_in4))
                
K(T+1)

NI_t_real = IN