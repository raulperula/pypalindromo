#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       palindromo.py
#       
#       Copyright 2011 Manuel Pedrero Luque <manuel@manuel-desktop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



def esPalindromo(frase):
    """
    Devuelve Verdadero si la frase usada como parámetro es palíndromo,
    ignorando espacios y signos de puntuación.
    """
    letras = [c for c in frase.lower() if c.isalpha()]
    return (letras == letras[::-1])
