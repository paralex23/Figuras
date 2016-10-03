#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import unittest
from verificaEdad import verificar

def verificaEdad(edad):
 if edad <= 0:
 	print "No existes"
 elif edad < 13 and edad >0:
 	print "Eres niño"
 if edad < 18:
 	print "Eres adolescente"	
 if edad < 65:
 	print "Eres adulto"
 if edad < 120:
 	print "Eres adulto mayor"
 else:
 	print "Eres Mumm-Ra"

if __name__ == '__main__':
	unittest.main()