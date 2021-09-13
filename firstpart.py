import numpy as np
#Fatima Rahimova 150180905

T=1/44100  # since sampling rate = 44100 Hz, then T= 1/44100

#decleration of b_0-b_6 values as in the report
b_0=8*T**3*f_ch**3
b_1=0
b_2=-24*T**3*f_ch**3
b_3=0
b_4=24*T**3*f_ch**3
b_5=0
b_6=-8*T**3*f_ch**3

#decleration of a_0-a_6 values as in the report
a_0=T**6*f_ch**3*f_cl**3 + 6*T**5*f_ch**3*f_cl**2 + 6*T**5*f_ch**2*f_cl**3 + 12*T**4*f_ch**3*f_cl + 36*T**4*f_ch**2*f_cl**2 + 12*T**4*f_ch*f_cl**3 + 8*T**3*f_ch**3 + 72*T**3*f_ch**2*f_cl + 72*T**3*f_ch*f_cl**2 + 8*T**3*f_cl**3 + 48*T**2*f_ch**2 + 144*T**2*f_ch*f_cl + 48*T**2*f_cl**2 + 96*T*f_ch + 96*T*f_cl + 64
a_1=6*T**6*f_ch**3*f_cl**3 + 24*T**5*f_ch**3*f_cl**2 + 24*T**5*f_ch**2*f_cl**3 + 24*T**4*f_ch**3*f_cl + 72*T**4*f_ch**2*f_cl**2 + 24*T**4*f_ch*f_cl**3 - 96*T**2*f_ch**2 - 288*T**2*f_ch*f_cl - 96*T**2*f_cl**2 - 384*T*f_ch - 384*T*f_cl - 384
a_2=15*T**6*f_ch**3*f_cl**3 + 30*T**5*f_ch**3*f_cl**2 + 30*T**5*f_ch**2*f_cl**3 - 12*T**4*f_ch**3*f_cl - 36*T**4*f_ch**2*f_cl**2 - 12*T**4*f_ch*f_cl**3 - 24*T**3*f_ch**3 - 216*T**3*f_ch**2*f_cl - 216*T**3*f_ch*f_cl**2 - 24*T**3*f_cl**3 - 48*T**2*f_ch**2 - 144*T**2*f_ch*f_cl - 48*T**2*f_cl**2 + 480*T*f_ch + 480*T*f_cl + 960
a_3= 20*T**6*f_ch**3*f_cl**3 - 48*T**4*f_ch**3*f_cl - 144*T**4*f_ch**2*f_cl**2 - 48*T**4*f_ch*f_cl**3 + 192*T**2*f_ch**2 + 576*T**2*f_ch*f_cl + 192*T**2*f_cl**2 - 1280
a_4=15*T**6*f_ch**3*f_cl**3 - 30*T**5*f_ch**3*f_cl**2 - 30*T**5*f_ch**2*f_cl**3 - 12*T**4*f_ch**3*f_cl - 36*T**4*f_ch**2*f_cl**2 - 12*T**4*f_ch*f_cl**3 + 24*T**3*f_ch**3 + 216*T**3*f_ch**2*f_cl + 216*T**3*f_ch*f_cl**2 + 24*T**3*f_cl**3 - 48*T**2*f_ch**2 - 144*T**2*f_ch*f_cl - 48*T**2*f_cl**2 - 480*T*f_ch - 480*T*f_cl + 960
a_5=6*T**6*f_ch**3*f_cl**3 - 24*T**5*f_ch**3*f_cl**2 - 24*T**5*f_ch**2*f_cl**3 + 24*T**4*f_ch**3*f_cl + 72*T**4*f_ch**2*f_cl**2 + 24*T**4*f_ch*f_cl**3 - 96*T**2*f_ch**2 - 288*T**2*f_ch*f_cl - 96*T**2*f_cl**2 + 384*T*f_ch + 384*T*f_cl - 384
a_6=T**6*f_ch**3*f_cl**3 - 6*T**5*f_ch**3*f_cl**2 - 6*T**5*f_ch**2*f_cl**3 + 12*T**4*f_ch**3*f_cl + 36*T**4*f_ch**2*f_cl**2 + 12*T**4*f_ch*f_cl**3 - 8*T**3*f_ch**3 - 72*T**3*f_ch**2*f_cl - 72*T**3*f_ch*f_cl**2 - 8*T**3*f_cl**3 + 48*T**2*f_ch**2 + 144*T**2*f_ch*f_cl + 48*T**2*f_cl**2 - 96*T*f_ch - 96*T*f_cl+64
                                                                              
#decleration of X array, Y array and output arrays
Xarr= []
Yarr=[]
                                     
# pseudo code takes input as array since when we read .wav files they will become array
def pseudo(array):
    #initially B,C,D,E,F,G = 0
    B=0 
    C=0 
    D=0 
    E=0 
    F=0 
    G=0
    for X in array: #filtering every data point in array
        Xarr.append(X)
        #formulas of A(z) and Y(z)
        A=((1/a_0)*X) - ((1/a_0)*(a_1*B + a_2*C + a_3*D + a_4*E + a_5*F + a_6*G))
        Y=(1/a_0)*(b_0*A + b_1*B + b_2*C + b_3*D + b_4*E + b_5*F + b_6*G)
        Yarr.append(Y) # X is input and Y is output
          
        G=F #G=A.(z**(-6)) = F.(z**(-1))
        F=E #F=A.(z**(-5)) = E.(z**(-1))
        E=D #E=A.(z**(-4)) = D.(z**(-1))
        D=C #D=A.(z**(-3)) = C.(z**(-1))
        C=B #C=A.(z**(-2)) = B.(z**(-1))
        B=A #B=A.(z**(-1))
    return Yarr # return output array
