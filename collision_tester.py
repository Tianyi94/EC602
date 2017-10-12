"""this is the main part of the assignment"""

# Copyright 2017 tianyiz tianyiz@bu.edu

import unittest
import subprocess

#please change this to valid author emails
AUTHORS = ['tianyiz@bu.edu']

PROGRAM_TO_TEST = "cf/collisionc_40_hard"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)

def removezero(a):
    return a.replace(".0000","")

class CollisionTestCase(unittest.TestCase):
    "empty class - write this"
    def test_one(self):
        strin = "one 20 10 -2 1"
        correct_out = "3\none 14 13 -2 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(removezero(out),correct_out)
        self.assertEqual(errs,"")

    def test_coll(self):
        strin = "A 0 0 1 0\nB 20 0 -1 0"
        correct_out = "10\nA 0 0 -1 0\nB 20 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["10"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(removezero(out),correct_out)
        self.assertEqual(errs,"")

    def test_morefield(self):
        strin = "A 0 0 1 1 1"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_invalidnumber(self):
        strin = "A 0 0 1"
        (rc, out) = runprogram(PROGRAM_TO_TEST, ["3"], strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")

    def test_invalidnumber(self):
        strin = "A 0 0 1 A "
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        self.assertEqual(rc,1)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")
	
    def test_negtime(self):
        strin = "A 0 0 1 0"
        correct_out = "1\nA 1 0 1 0\n3\nA 3 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1","-2","3"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(removezero(out),correct_out)
        self.assertEqual(errs,"")

    def test_rtime(self):
        strin = "A 0 0 1 0"
        correct_out = "0\nA 0 0 1 0\n3\nA 3 0 1 0\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3","0"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(removezero(out),correct_out)
        self.assertEqual(errs,"")

    def test_emptyinput(self):
        strin = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,[""],strin)
        self.assertEqual(rc,2)
        self.assertEqual(out,"")
        self.assertEqual(errs,"")



    def test_longtime(self):
        strin = "A 0 0 1 1"
        correct_out = "999999\nA 999999 999999 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["999999"],strin)
        self.assertEqual(rc,0)
        self.assertEqual(removezero(out),correct_out)
        self.assertEqual(errs,"")  


#    def test_collision(self):
#        strin = "BAL001 0 0 1 0\nBAL002 20 0 -1 0\nBAL003 30 15 0 -2.1111111\nBAL004 30 -15 0 3.1111111"
#        correct_out = "0\nBAL001 0 0 1 0\nBAL002 20 0 -1 0\nBAL003 30 15 0 -2.1111111\nBAL004 30 -15 0 3.1111111\n2\nBAL001 2 0 1 0\nBAL002 18 0 -1 0\nBAL003 30 10.777778 0 -2.1111111\nBAL004 30 -8.7777778 0 3.1111111\n7\nBAL001 3 0 -1 0\nBAL002 17 0 1 0\nBAL003 30 16.777778 0 3.1111111\nBAL004 30 -9.7777777 0 -2.1111111\n"
#        (rc,out,errs) = runprogram(PROGRAM_TO_TEST, ["0", "2", "7"], strin)
#        self.assertEqual(rc,0)
#        self.assertEqual(out,correct_out)
#        self.assertEqual(errs,"") 
def main():
    "show how to use runprogram"

#    print(runprogram('./test_program.py', ["4", "56", "test"], "my input"))
    unittest.main()

if __name__ == '__main__':
    main()

