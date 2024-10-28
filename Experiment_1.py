#Evaluate the parameters for the steam turbine 
import pyromat as pm
import numpy as np
import math
steam=pm.get('mp.H2O')
def steam_turbine():
    n=int(input("Enter the number of runs: \n"))
    #pressure in bar and K
    for i in range(n):
        #State 3:
        print(f"\nInput set {i+1}: \n")
        p_3=float(input("Enter the pressure at turbine entry (bar): \n"))
        T_3=float(input("Enter the temperature at turbine entry (K): \n"))
        h3=steam.h(T=T_3, p=p_3)[0]
        T7=float(input("Enter T7 (K): \n"))
        T8=float(input("Enter T8: \n"))
        T9=float(input("Enter T9 : \n"))
        Qw=float(input("Enter Qw (m3/h): \n"))
        Qc=float(input("Enter Qc (m3/h): \n"))
        

        #Sate 4:
        
        p_4=float(input("Enter the pressure at turbine exit (bar): \n"))
        h_4s1=steam.h(p=p_4, x=0)[0]
        h_4s2=steam.h(p=p_4, x=1)[0]
        h_4s=0.9*(h_4s2-h_4s1)
        h4=4.186*((T9-T8)*Qw +(T7*Qc))/Qc
        ise_eff=(h3-h4)/(h3-h_4s) *100
        V=float(input("Enter V n\n"))
        I=float(input("Enter I: \n"))
        P=V*I * pow(10, -3)
        change_H=float(input("Enter H :\n"))
        W1=1.05*1*pow(0.018,2)*0.7938*math.sqrt((1000*9.81*change_H)/0.7938)
        H_T=(h3-h4)*W1
        eff_eff=P/H_T*100
        steam_consumption=W1/P
        Mq=3600*P
        m1=float(input("Enter m1: \n"))
        m2=float(input("Enter m2: \n"))
        H_fb=43950*6*m1*780
        H_sb=43950*6*m2*780
        over_eff=(Mq)/(H_fb+H_sb) *100


        
        print(f"H3={h3:.3f}bar")
        
      
        print(f"h4={h4:.3f}")
        print(f"Shaft output={P:.3f}kW")
        print(f"Isentropic efficiency={ise_eff}%")
        print(f"Effective efficiency={eff_eff:.3f}%")
        print(f"Steam consumption={steam_consumption:.3f}")
        print(f"Overall efficiency={over_eff:.8f} %")
        print(f"W1={W1:.4f}")
        print(f"H={H_T:.4f}")
steam_turbine()

        


