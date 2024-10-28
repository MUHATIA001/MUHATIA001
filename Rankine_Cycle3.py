#A program to evaluate the steam turbine performane
#It determines the expansion line end points ELEP
#It assumes 10% pressure drop at theintercept valve
#It assumes 0.0508 bar exhaust pressure
#It assumes there is no pressure and temperature drop in the governor valve
import pyromat as pm
import numpy as np
steam=pm.get('mp.H2O')

#Create a function to solve HP ELEP and LP ELEP
def turbine_Performance():
    #State 1
    T_1=float(input("Enter the superheated steam temperature (K): \n"))
    p_1=float(input("Enter the boiler pressure (bar): \n"))
    h_1=steam.h(T=T_1, p=p_1)[0]
    s_1=steam.s(T=T_1, p=p_1)[0]

    #Sate 2
    
    p_drop=float(input("Enter the preeusre drop in throttle valves (%):\n"))
    p2=p_1-p_1*(p_drop/100)
    h_2=h_1 #Assuming constant pressure drop after throttling
    s_2=steam.s(h=h_2, p=p2)[0]
    print(f"State 2: p2 = {p2:.2f} bar, h2 = {h_2:.2f} kJ/kg, s2 = {s_2:.4f} kJ/kg-K")

    #Sate 3
    s_3=s_2
    p_3=float(input("Enter the HP turbine exit pressure (bar): \n"))
    h3_s=steam.h(p=p_3, s=s_3)[0]
    eff_hp=float(input("Enter the efficiency of the HP turbine (%): \n"))
    h_3=h_2-(eff_hp/100)*(h_2-h3_s)# hp turbine ELEP

    #State 4
    #The staem pressure drops by 10% in the intercept valves
    p2_drop=float(input("Enter the pressure drop in the intercept valves (bar): \n"))
    p_4=p_3-(p2_drop/100)*p_3
    T_4=float(input("Enter the temperature at the exit of the reheat (K):\n"))
    h_4=steam.h(T=T_4, p=p_4)[0]
    s_4=steam.s(T=T_4, p=p_4)[0]

    #State 5:
    p_5=float(input("Enter the condenser pressure (bar): \n"))
    s_5=s_4
    h_5=steam.h(p=p_5, s=s_5)[0]

    #Exhaust loss
    exhaust_loss=float(input("Enter the exhaust loss (kJ/kg):\n"))
    tep=h_5+exhaust_loss

    #Output variables
    print(f"Steam enthalpy at generator exit={h_1:.3f} kJ/kg.")
    print(f"The entropy at the exit of the generator={s_1:.3f} kJ/kg-K.")
    print(f"The enthalpy at turbine entry={h_2:.3f}kJ/kg.")
    print(f"The entropy at the turbine entry={s_2:.3f}kJ/kg-K.")
    print(f"The HP ELEP={h_3:.3f}kJ/kg.")
    print(f"The entropy at turbine exit={s_3:.3f}kJ/kg")
    print(f"The enthalpy of the steam entring the LP turbine={h_4:.3f}kJ/kg.")
    print(f"The entropy of the steam entering the LP turbine={s_4:.3f}kJ/kg-K.")
    print(f"The LP ELEP={h_5:.3f}kJ/kg.")
    print(f"TEP={tep:.3f}kJ/kg.")
turbine_Performance()

    