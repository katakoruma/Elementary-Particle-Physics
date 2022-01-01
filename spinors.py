# -*- coding: utf-8 -*-

# Nötige from- und import-Anweisungen hier einfügen.

from sympy import Matrix, pprint, I, ones, eye, expand, simplify, diag, sqrt

def u(E,px,py,pz,m,spin): # Argumente in der Klammer ergänzen
    """
    Spinor u
    """
    if spin == "u":
    
        u = sqrt(E + m) * Matrix(4,1,[1,0,pz/(E+m),(px+I*py)/(E+m)])
        
    elif spin == "d":
        
        u = sqrt(E + m) * Matrix(4,1,[0,1,(px-I*py)/(E+m),-pz/(E+m)])
        
    else:
        
        raise ValueError("Invalid Value for spin: Use 'u' for Spin up and 'd' for Spin down")
    
    return u # Rückgabewert ergänzen


def ubar(E,px,py,pz,m,spin): # Argumente in der Klammer ergänzen
    """
    Adjungierter Spinor u-quer
    """
    if spin == "u":
    
        u = sqrt(E + m) * Matrix(4,1,[1,0,pz/(E+m),(px+I*py)/(E+m)])
        
    elif spin == "d":
        
        u = sqrt(E + m) * Matrix(4,1,[0,1,(px-I*py)/(E+m),-pz/(E+m)])
       
    else:
        
        raise ValueError("Invalid Value for spin: Use 'u' for Spin up and 'd' for Spin down")
        
    u = u.H * diag(1,1,-1,-1)
    
    return u # Rückgabewert ergänzen


def v(E,px,py,pz,m,spin): # Argumente in der Klammer ergänzen
    """
    Spinor v
    """
    if spin == "u":
    
        v = sqrt(E + m) * Matrix(4,1,[(px-I*py)/(E+m),-pz/(E+m),0,1])
        
    elif spin == "d":
        
        v = sqrt(E + m) * Matrix(4,1,[pz/(E+m),(px+I*py)/(E+m),1,0])
    
    else:
        
        raise ValueError("Invalid Value for spin: Use 'u' for Spin up and 'd' for Spin down")
        
    return v # Rückgabewert ergänzen


def vbar(E,px,py,pz,m,spin): # Argumente in der Klammer ergänzen
    """
    Adjungierter Spinor v-quer
    """
    if spin == "u":
    
        v = sqrt(E + m) * Matrix(4,1,[(px-I*py)/(E+m),-pz/(E+m),0,1])
        
    elif spin == "d":
        
        v = sqrt(E + m) * Matrix(4,1,[pz/(E+m),(px+I*py)/(E+m),1,0])
    
    else:
        
        raise ValueError("Invalid Value for spin: Use 'u' for Spin up and 'd' for Spin down")  
        
    v = v.H * diag(1,1,-1,-1)
    
    return v # Rückgabewert ergänzen
