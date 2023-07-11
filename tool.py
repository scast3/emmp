#All in metric units
from math import log10

def power(q,h,rho,g):
    w = q*rho*g*h
    return w

def pump_head(P1,V1,z1,P2,V2,z2,hl,rho,g):
    hp = (P2-P1)/(rho*g)+(V2^2-V1^2)/(2*g)+(z2-z1)+hl
    return hp

#Haaland sucks, not very accurate
def haaland(Re,e,D):
    e_D = e / D
    A = (e_D**1.11)/3.7
    B = -1.8*log10(A+6.9/Re)
    f = (1/B)**2
    
    return f

#Iterative derivation for friction factor
def colebrooks(Re,e,D, f):
    e_D = e/D
    while True:
        f_prev = f
        f = (-2 * log10(e_D / 3.7 + 2.51 / (Re * f_prev**0.5)))**-2
        
        # Check for convergence
        if abs(f - f_prev) < 1e-6:
            break
    return f

def h_loss(v,L,g,sum_k,e,D,Re):
    f = colebrooks(Re,e,D,.02)
    hl = (v**2)/(2*g)*(f*L/D+sum_k)
    return hl

def reynolds(rho,v,d,mu):
    Re = rho*v*d/mu
    return Re

def main():

    Re = reynolds(1000,3.3,0.09,9.9e-4)
    hl = h_loss(3.3,17,9.80,4*0.3+1,1.8e-4,0.09,Re)
    print(f'Loss: {hl:.2f} meters')
    hp = hl+11.55
    print(f'Power: {power(.021,1000,9.81,15.293):.2f} Watts')
main()