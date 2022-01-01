# -*- coding: utf-8 -*-

from sympy import exp
from sympy.physics import mgamma


def Sxrot(theta):
    """
    Matrix für die Rotation eines Spinors um die x-Achse mit dem Winkel 𝜃
    """
    return exp(-theta/2 * mgamma(2) * mgamma(3))

def Sxlor(omega):
    """
    Matrix, um einen Lorentz-Boosts entlang der x-Achse mit 𝜔 = artanh(𝛽) auf einen Spinor anzuwenden
    """
    return exp(-omega/2 * mgamma(0) * mgamma(1))

def Syrot(theta):
    """
    Matrix für die Rotation eines Spinors um die y-Achse mit dem Winkel 𝜃
    """
    return exp(-theta/2 * mgamma(3) * mgamma(1))

def Sylor(omega):
    """
    Matrix, um einen Lorentz-Boosts entlang der y-Achse mit 𝜔 = artanh(𝛽) auf einen Spinor anzuwenden
    """
    return exp(-omega/2* mgamma(0) * mgamma(2))

def Szrot(theta):
    """
    Matrix für die Rotation eines Spinors um die z-Achse mit dem Winkel 𝜃
    """
    return exp(-theta/2 * mgamma(1) * mgamma(2))

def Szlor(omega):
    """
    Matrix, um einen Lorentz-Boosts entlang der z-Achse mit 𝜔 = artanh(𝛽) auf einen Spinor anzuwenden
    """
    return exp(-omega/2 * mgamma(0) * mgamma(3))
