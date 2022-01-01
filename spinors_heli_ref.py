# -*- coding: utf-8 -*-

from spinors_ref import u, v
from lorentz_all_ref import Szlor, Syrot, Szrot

from sympy import simplify, sqrt
from sympy.physics import mgamma


def uH(heli, E, m, theta, phi):
    """
    Spinor eines Teilchens im Helizitätseigenzustand "heli" ("+"/"-"), in Richtung (theta, phi), mit Energie E und Masse m
    """
    if heli not in ['+', '-']:
        raise ValueError("Value of heli must be '+' or '-'")
    return  simplify(Szrot(-phi) * simplify(Syrot(-theta) * u((E, 0, 0, sqrt(E**2 - m**2)), m, (heli=='+'))))


def uHbar(heli, E, m, theta, phi):
    """
    Adjungierter Spinor eines Teilchens im Helizitätseigenzustand "heli" ("+"/"-"), in Richtung (theta, phi), mit Energie E und Masse m
    """
    return  (uH(heli, E, m , theta, phi)).H * mgamma(0)


def vH(heli, E, m, theta, phi):
    """
    Spinor eines Antiteilchens im Helizitätseigenzustand "heli" ("+"/"-"), in Richtung (theta, phi), mit Energie E und Masse m
    """
    if heli not in ['+', '-']:
        raise ValueError("Value of heli must be '+' or '-'")
    return  simplify(Szrot(-phi) * simplify(Syrot(-theta) * v((E, 0, 0, sqrt(E**2 - m**2)), m, (heli=='+'))))


def vHbar(heli, E, m, theta, phi):
    """
    Adjungierter Spinor eines Antiteilchens im Helizitätseigenzustand "heli" ("L"/"R"), in Richtung (theta, phi), mit Energie E und Masse m
    """
    return  (vH(heli, E, m , theta, phi)).H * mgamma(0)
