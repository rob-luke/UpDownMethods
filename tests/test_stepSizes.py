import UpDownMethods as ud
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.proc = ud.UpDownMethod(stepSize=[4, 4, 2, 2, 1, 1])
        self.proc(False)
        self.proc(False)
        self.proc(True)
        self.proc(True)
        self.proc(True)
        self.proc(True)
        self.proc(False)
        self.proc(False)
        self.proc(True)
        self.proc(True)
        self.proc(True)
        self.proc(True)
        self.proc(False)
        self.proc(False)
        self.proc(True)
        self.proc(True)
        self.proc(True)
        self.proc(True)
        self.proc(False)
        self.proc(False)
        self.proc(True)
        self.proc(True)
        self.proc(False)
        self.proc(False)
        self.proc(True)
        self.proc(True)
        self.proc(False)
        self.proc(False)
        self.proc(True)
        self.proc(True)

    def test_0Reversals(self):
        lastStep = self.proc.results["Value"][2] - \
            self.proc.results["Value"][1]
        self.assertEqual(lastStep, 4)

    def test_1Reversals(self):
        lastStep = self.proc.results["Value"][6] - \
            self.proc.results["Value"][5]
        self.assertEqual(lastStep, -4)

    def test_2Reversals(self):
        lastStep = self.proc.results["Value"][7] - \
            self.proc.results["Value"][6]
        self.assertEqual(lastStep, 2)

    def test_3Reversals(self):
        lastStep = self.proc.results["Value"][10] - \
            self.proc.results["Value"][9]
        self.assertEqual(lastStep, -2)

    def test_4Reversals(self):
        lastStep = self.proc.results["Value"][13] - \
            self.proc.results["Value"][12]
        self.assertEqual(lastStep, 1)

    def test_5Reversals(self):
        lastStep = self.proc.results["Value"][16] - \
            self.proc.results["Value"][15]
        self.assertEqual(lastStep, -1)

    def test_6Reversals(self):
        lastStep = self.proc.results["Value"][19] - \
            self.proc.results["Value"][18]
        self.assertEqual(lastStep, 1)

    def test_7Reversals(self):
        lastStep = self.proc.results["Value"][22] - \
            self.proc.results["Value"][21]
        self.assertEqual(lastStep, -1)

    def test_8Reversals(self):
        lastStep = self.proc.results["Value"][27] - \
            self.proc.results["Value"][26]
        self.assertEqual(lastStep, 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
