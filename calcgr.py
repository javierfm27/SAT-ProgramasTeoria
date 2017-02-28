#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
    sys.exit("Usage: python3 calc.py operacion operando1 operando2")

_,operacion,operando1,operando2 = sys.argv

try:
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("Los operandos deben ser float")
