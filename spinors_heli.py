# -*- coding: utf-8 -*-

from lorentz import*
from sympy import *

# Nötige from- und import-Anweisungen hier einfügen.

def uH(E,m,Theta,Phi,hel): # Argumente für Energie, Masse, zwei Richtungswinkel und Helizität ergänzen
    """
    Spinor eines Teilchens im Helizitätseigenzustand (+ oder -)
    """
    if hel == "+":
    
        u = sqrt(E + m) * Matrix(4,1,[1,0,sqrt(E**2-m**2)/(E+m),0])
        #u =  Matrix(4,1,[1,0,sqrt(E**2-m**2)/(E+m),0])
        
    elif hel == "-":
        
        u = sqrt(E + m) * Matrix(4,1,[0,1,0,-sqrt(E**2-m**2)/(E+m)])
        #u =  Matrix(4,1,[0,1,0,-sqrt(E**2-m**2)/(E+m)])
        
    else:
        
        raise ValueError("Invalid Value for helicity. Use '+' or '-' ")
        
    u = simplify( simplify( Szrot(-Phi) * Syrot( -Theta ) * Szrot(Phi) * u ))
    
    return u # Rückgabewert ergänzen


def uHbar(E,m,Theta,Phi,hel): # Argumente für Energie, Masse, zwei Richtungswinkel und Helizität ergänzen
    """
    Adjungierter Spinor eines Teilchens im Helizitätseigenzustand (+ oder -)
    """
    if hel == "+":
    
        u = sqrt(E + m) * Matrix(4,1,[1,0,sqrt(E**2-m**2)/(E+m),0])
        #u =  Matrix(4,1,[1,0,sqrt(E**2-m**2)/(E+m),0])
        
    elif hel == "-":
        
        u = sqrt(E + m) * Matrix(4,1,[0,1,0,-sqrt(E**2-m**2)/(E+m)])
        #u =  Matrix(4,1,[0,1,0,-sqrt(E**2-m**2)/(E+m)])
        
    else:
        
        raise ValueError("Invalid Value for helicity. Use '+' or '-' ")
        
    u = simplify( simplify( Szrot(-Phi) * Syrot( -Theta ) * Szrot(Phi) * u ))
    
    u = u.H * diag(1,1,-1,-1)
    
    return u # Rückgabewert ergänzen


def vH(E,m,Theta,Phi,hel): # Argumente für Energie, Masse, zwei Richtungswinkel und Helizität ergänzen
    """
    Spinor eines Antiteilchens im Helizitätseigenzustand (+ oder -)
    """
    if hel == "+":
    
        u = sqrt(E + m) * Matrix(4,1,[0,-sqrt(E**2-m**2)/(E+m),0,1])
        #u =  Matrix(4,1,[0,-sqrt(E**2-m**2)/(E+m),0,1])
        
    elif hel == "-":
        
        u = sqrt(E + m) * Matrix(4,1,[sqrt(E**2-m**2)/(E+m),0,1,0])
        #u =  Matrix(4,1,[sqrt(E**2-m**2)/(E+m),0,1,0])
        
    else:
        
        raise ValueError("Invalid Value for helicity. Use '+' or '-' ")
        
    u = simplify( simplify( Szrot(-Phi) * Syrot( -Theta ) * Szrot(Phi) * u ))
    
    return u # Rückgabewert ergänzen


def vHbar(E,m,Theta,Phi,hel): # Argumente für Energie, Masse, zwei Richtungswinkel und Helizität ergänzen
    """
    Adjungierter Spinor eines Antiteilchens im Helizitätseigenzustand (+ oder -)
    """
    if hel == "+":
    
        u = sqrt(E + m) * Matrix(4,1,[0,-sqrt(E**2-m**2)/(E+m),0,1])
        #u =  Matrix(4,1,[0,-sqrt(E**2-m**2)/(E+m),0,1])
        
    elif hel == "-":
        
        u = sqrt(E + m) * Matrix(4,1,[sqrt(E**2-m**2)/(E+m),0,1,0])
        #u =  Matrix(4,1,[sqrt(E**2-m**2)/(E+m),0,1,0])
        
    else:
        
        raise ValueError("Invalid Value for helicity. Use '+' or '-' ")
        
    u = simplify( simplify( Szrot(-Phi) * Syrot( -Theta ) * Szrot(Phi) * u ))
    
    u = u.H * diag(1,1,-1,-1)
    
    return u # Rückgabewert ergänzen
