#!/usr/bin/python3
"""TEST TEST TEST essah sssah saah...
Fine it's working"""

from console import HBNBCommand
from unittest.mock import patch
import os, sys
from io import StringIO
from unittest import TestCase

class TestConsole(TestCase):
    """test for console"""
    def tst(self):
        """unitest"""
        pass

    def tst1(self):
        """unitest"""
        try:
            os.remove('file.json')
        except:
            pass
    def testcreat(self):
        """unitest"""
        with patch('sys.stdout', new=StringIO()) as a:
            HBNBCommand().onecmd("create cheking")
        out = a.getvalue()[:-1]
        self.assertEqual(out, "** class doesn't exist **")
    
    def testcre(self):
        """unitest"""
        with patch('sys.stdout', new=StringIO()) as a:
            HBNBCommand().onecmd("create")
        out = a.getvalue()[:-1]
        self.assertEqual(out, "** class name missing **")

    def testcreatebasemodel(self):
        """unitest"""
        with patch('sys.stdout', new=StringIO()) as a:
            HBNBCommand().onecmd("basemdl creating")
        out = a.getvalue()[:-1]
        self.assertEqual(type(out), str)

    def unittestaa(self):
        """unitest"""
        with patch('sys.stdout', new=StringIO()) as a:
            HBNBCommand().onecmd('create State name="Sfax"')
            HBNBCommand().onecmd('all State')
        out = a.getvalue()[:-1]
        self.assertTrue("'name': 'Sfax'" in out)

     
    def test(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place nbr_zeb=2 price=5.5')
            HBNBCommand().onecmd('all Place')
        out = f.getvalue()[:-1]
        self.assertTrue("'nbr_zeb': 2" in out)
        self.assertTrue("'price': 5.5" in out)