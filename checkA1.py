#!/usr/bin/env python3

import unittest
from datetime import datetime, date, timedelta
from random import randint
import sys, os
import subprocess as sp
from importlib import import_module
import ast, inspect

'''
ASSIGNMENT 1 CHECK SCRIPT
Author: Eric Brauer eric.brauer@senecapolytechnic.ca

Description:
TestAfter .. TestDBDA all are testing functions inside students' code. 
TestFinal will run the code as a subprocess and evaluate the std.output.

The precise requirements of each student-created function are specified elsewhere.

The script assumes that the student's filename is named 'assignment1.py' and exists in the same directory as this check script.

NOTE: Feel free to _fork_ and modify this script to suit needs. I will try to fix any issues that arise but this script is provided as-is, with no obligation of warranty or support.
'''

class TestAfter(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dtypes(self):
        "after() is returning string"
        i = '2023-01-10'
        error_msg = 'Your after() function should accept one string as arg, and return a string.'
        self.assertIsInstance(self.a1.after(i), str, error_msg)

        
    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{y}-{m:02}-{d:02}'

    def test_after_date(self):
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%Y-%m-%d')
            
            eobj = dobj1 + timedelta(1)
            e = eobj.strftime('%Y-%m-%d')
            error_msg = (f'after function not returning correct answer.\n'
                         f'inputs: {date1}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.after(date1), e, error_msg)
    
    def test_leap(self):
        "after() works with leap year"
        i = '2020-02-28'
        e = '2020-02-29'
        error_msg = "Your after() function is returning the wrong answer for a leap year"
        self.assertEqual(self.a1.after(i), e, error_msg)


class TestBefore(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_dtypes(self):
        "before() is returning string"
        i = '2023-01-10'
        error_msg = 'Your before() function would accept one string as arg, and return a string.'
        self.assertIsInstance(self.a1.before(i), str, error_msg)

        
    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{y}-{m:02}-{d:02}'

    def test_before_date(self):
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%Y-%m-%d')
            
            eobj = dobj1 + timedelta(-1)
            e = eobj.strftime('%Y-%m-%d')
            error_msg = (f'before function not returning correct answer.\n'
                         f'inputs: {date1}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.before(date1), e, error_msg)
    
    def test_leap(self):
        "before() works with leap year"
        i = '2020-03-01'
        e = '2020-02-29'
        error_msg = "Your before() function is returning the wrong answer for a leap year"
        self.assertEqual(self.a1.before(i), e, error_msg)


class TestMonMax(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_mon_max(self):
        "test the mon_max function"
        y = 2023
        mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for i, e in mon_dict.items():
            error_msg = f'bad output from mon_max function. Input month: {i}. Expected: {e}'
            self.assertEqual(self.a1.mon_max(i, y), e, error_msg)

    def test_leap_max(self):
        "test mon_max with feb of leap/non-leap years"
        years = {2022: 28, 2020: 29, 2024: 29, 2023: 28, 1960: 29, 1969: 28, 2000: 29, 1900: 28}
        for i, e in years.items():
            error_msg = f'bad output from mon_max function. Input year: {i}. Input month: 2. Expected: {e}'
            self.assertEqual(self.a1.mon_max(2, i), e, error_msg)


class TestLeap(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_leap_func(self):
        "leap_year function exists and returns True/False"
        test_dat = {
            2022: False,
            2020: True,
            2024: True,
            2023: False,
            1960: True,
            1969: False,
            1900: False,
            2000: True
        }
        error_msg = 'leap_year() not returning correct True/False for a specific year'
        for i,e in test_dat.items():
            self.assertEqual(self.a1.leap_year(i), e, error_msg)


class TestValidDate(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def test_valid_dates(self):
        "making sure valid dates return True"
        test_dat = [
            '2022-01-25',
            '2011-03-13',
            '2001-01-01',
            '1539-11-30',
            '2020-02-29',
            '2038-01-19'
        ]
        error_msg = 'valid_date() not returning true for a valid date'
        for date in test_dat:
            self.assertEqual(self.a1.valid_date(date), True, error_msg)
    
    def test_invalid_dates(self):
        "making sure invalid dates return False"
        test_dat = [
            '2022-25-01',
            '20-03-13',
            '2001-20-01',
            '1539-11-00',
            '2021-02-29',
            '2023-04-31'
        ]
        error_msg = 'valid_date() not returning false for an invalid date'
        for date in test_dat:
            self.assertEqual(self.a1.valid_date(date), False, error_msg)


class TestDBDA(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        try:
            self.a1 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")

    def rando_date_str(self):
        invalid = True
        while invalid:
            y = randint(1800, 2100)
            m = randint(1, 12)
            d = randint(1, 31)
            try:
                x = date(y, m, d)
                invalid = False
            except ValueError:
                pass
        return f'{y}-{m:02}-{d:02}'
    
    def test_after_dbda(self):
        "does dbda work with positive numbers"
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%Y-%m-%d')
            num = randint(0, 500)
            eobj = dobj1 + timedelta(num)
            e = eobj.strftime('%Y-%m-%d')
            error_msg = (f'dbda function not returning correct answer.\n'
                         f'inputs: {date1} {num}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.dbda(date1, num), e, error_msg)
    
    def test_before_dbda(self):
        "does dbda work with negative numbers"
        for _ in range(1, 11):
            date1 = self.rando_date_str()
            dobj1 = datetime.strptime(date1, '%Y-%m-%d')
            num = randint(-500, -1)
            eobj = dobj1 + timedelta(num)
            e = eobj.strftime('%Y-%m-%d')
            error_msg = (f'dbda function not returning correct answer.\n'
                         f'inputs: {date1} {num}.\n'
                         f'expected: {e}.\n')
            self.assertEqual(self.a1.dbda(date1, num), e, error_msg)



class TestModuleRestriction(unittest.TestCase):
    "no modules apart from allowed are being imported"
    
    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        try:
            self.assertTrue(os.path.exists(file), msg=error_output)
        except AssertionError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")
    
    def test_unallowed_module(self):
        "you have imported a prohibited module"
        allowed = ["sys"]  # list of permitted modules
        try:
            src = inspect.getsource(import_module(self.filename.split('.')[0]))
            tree = ast.parse(src)
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment1.py. Do not rename or delete any of the required functions.")
        stimp = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for alias in node.names:
                    stimp.append(alias.name)
        for modname in stimp:
            if modname not in allowed:
                raise AssertionError(f'You have imported a prohibited module.\n'
                    f'module {modname} is not allowed. Review the Wiki' 
                    ' instructions again.')


class TestFinal(unittest.TestCase):

    def setUp(self):
        self.filename = 'assignment1.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)

    def test_proper_step(self):
        "main print returning proper step"
        steps = [2, 3, 4, 5, 6, 7, 8]
        expects = [r"182", r"122", r"91", r"73", r"61", r"52", r"46"]
        for step, expect in zip(steps, expects):
            input = ['2023-01-25', str(step)]
            error_msg = (f"\nError in {self.filename}: Incorrect output for wrong letters.\n"
                    f"I entered: {input}\n"
                    f"I expected: {expect}")
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate()
            if p.returncode != 0:
                raise IOError("Error running the script.")
            self.assertRegex(output.decode('utf-8'), expect, error_msg)

    def test_proper_before(self):
        "output contain 'XX days ago' w/ correct date"
        testdates = [
            '2023-01-23', 
            '2022-11-01', 
            '2024-06-15', 
            '2022-03-01', 
            '2022-01-01',
            '2020-02-14' 
        ]
        error_msg = 'dbda() not returning the expected end date'
        for datestr in testdates:
            step = randint(1, 9)
            numdays = round(365 / step) * -1
            dobj = date.fromisoformat(datestr)
            deltobj = timedelta(days=numdays)
            input = [datestr, str(step)]
            e = str(dobj+deltobj)
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate()
            if p.returncode != 0:
                raise IOError("Error running the script.")
            self.assertRegex(output.decode('utf-8'), e, error_msg)

    def test_proper_after(self):
        "output contain XX days from now w/ correct date"
        testdates = [
            '2023-01-23', 
            '2022-11-01', 
            '2024-06-15', 
            '2022-03-01', 
            '2022-01-01',
            '2020-02-14' 
        ]
        error_msg = 'dbda() not returning the expected end date'
        for datestr in testdates:
            step = randint(1, 9)
            numdays = round(365 / step)
            dobj = date.fromisoformat(datestr)
            deltobj = timedelta(days=numdays)
            input = [datestr, str(step)]
            e = str(dobj+deltobj)
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate()
            if p.returncode != 0:
                raise IOError("Error running the script.")
            self.assertRegex(output.decode('utf-8'), e, error_msg)
        

    def test_invalid_date(self):
        "output contains usage when bad date"
        test_dat = [
            '2022-25-01',
            '20-03-13',
            '2001-20-01',
            '1539-11-00',
            '2021-02-29',
            '2023-04-31'
        ]
        error_msg = "Error: Entering an invalid date should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        for datestr in test_dat:
            input = [datestr, '2']
            cmd = [self.pypath, self.filename] + input
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = p.communicate()
            self.assertRegex(output.decode('utf-8'), e, error_msg)


    def test_invalid_step(self):
        "output contains usage when bad step"
        error_msg = "Error: Entering an invalid step should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        input = ['2023-01-25', '0']
        cmd = [self.pypath, self.filename] + input
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = p.communicate()
        self.assertRegex(output.decode('utf-8'), e, error_msg)

    def test_arg_length(self):
        "when args != 2, output contains usage"
        error_msg = "Error: Entering wrong number of args should call the usage function, return a usage message, and exit."
        e = r'(?i)Usage.*'  # ignore case
        input = ['2023-01-25']
        cmd = [self.pypath, self.filename] + input
        p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = p.communicate()
        self.assertRegex(output.decode('utf-8'), e, error_msg)

if __name__ == "__main__":
    unittest.main(buffer=True)  # buffer line suppresses a1 printlines from check script output.


