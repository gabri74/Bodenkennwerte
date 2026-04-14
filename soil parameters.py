#!/usr/bin/env python
# coding: utf-8

# ### Soil Parameters /  Bodenkennwerte

# In[10]:


def soil_parameters(md, mw, rho_s, rho_w, Vv, Vw, g=10):

    mt = md + mw
    Vs = md / rho_s
    Vt = Vs + Vv
    e = Vv / Vs
    n = Vv / Vt
    w = mw / md
    Sr = Vw / Vv
    rho = mt / Vt
    rho_d = md / Vt
    gamma = rho * g
    gamma_d = rho_d * g
    gamma_s = rho_s * g
    gamma_w = rho_w * g
    gamma_r = (1 - n) * gamma_s + n * gamma_w
    gamma_a = (1 - n) * (gamma_s - gamma_w)


    
    from colorama import Fore, Style

    print("Soil Parameters" )

    print()
    print(f"Vs   = {Vs:.3f} cm³")
    print(f"Vt   = {Vt:.3f} cm³")
    print(f"e    = {e:.3f}")
    print(f"n    = {n:.3f}")
    print(f"w    = {w:.3f}")
    print(f"Sr   = {Sr:.3f}")
    print(f"rho  = {rho:.3f} g/cm³")
    print(f"rho_d= {rho_d:.3f} g/cm³")
    print(f"γ    = {gamma:.3f}")
    print(f"γ_d  = {gamma_d:.3f}")
    print(f"γ_r  = {gamma_r:.3f}")
    print(f"γ_a  = {gamma_a:.3f}")

m = 75.35
md = 59.20
mw = m - md
rho_s = 2.70
rho_w = 1.0
Vt = 39


Vs = md / rho_s
Vv = Vt - Vs


w = mw / md
Vw = w * Vs  

soil_parameters(md, mw, rho_s, rho_w, Vv, Vw)


# In[ ]:




