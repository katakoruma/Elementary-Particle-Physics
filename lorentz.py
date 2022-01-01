# -*- coding: utf-8 -*-

# Nötige from- und import-Anweisungen hier einfügen.
from sympy.physics.matrices import mgamma
from sympy import *


def Szrot(Theta):
    """
    Matrix für die Rotation eines Spinors um die z-Achse mit dem Winkel 𝜃
    """
    return simplify( exp(-Theta/2 * mgamma(1,True)*mgamma(2,True)) )

def Sxrot(Theta):
    return simplify( exp(-Theta/2 * mgamma(2,True)*mgamma(3,True)) )

def Syrot(Theta):
    return simplify( exp(-Theta/2 * mgamma(3,True)*mgamma(1,True)) )

def Szlor(omega):
    """
    Matrix, um einen Lorentz-Boosts entlang der 𝑧-Achse mit 𝜔 = artanh(𝛽) auf einen Spinor anzuwenden
    """
    return exp(omega/2 * mgamma(0,True)*mgamma(3,True))
