from UpDownMethods import CORRECT, INCORRECT
import UpDownMethods as ud
import unittest


# Figure 4 Levitt 1971
resp1 = [CORRECT, CORRECT, INCORRECT, INCORRECT, INCORRECT, INCORRECT,
         CORRECT, CORRECT, INCORRECT, INCORRECT, INCORRECT, CORRECT,
         CORRECT, CORRECT, CORRECT, CORRECT, INCORRECT, INCORRECT,
         INCORRECT, CORRECT, CORRECT, INCORRECT, INCORRECT, INCORRECT]

# Figure 5 Levitt 1971
resp2 = [CORRECT, CORRECT, CORRECT, CORRECT, INCORRECT, CORRECT, INCORRECT,
         INCORRECT, CORRECT, INCORRECT, CORRECT, CORRECT, CORRECT, CORRECT,
         CORRECT, INCORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT,
         CORRECT, CORRECT, CORRECT, CORRECT]


class TestSequenceFunctions(unittest.TestCase):

    def test_Levitt_fig4(self):
        self.stim1 = ud.UpDownMethod(down=1, up=1, stepSize=1, initialValue=0)
        for resp in resp1:
            self.stim1(resp)
        est = ud.estimate_reversals(self.stim1.results)
        self.assertEqual(est, 0)

    def test_Levitt_fig5(self):
        self.stim2 = ud.UpDownMethod(down=2, up=1, stepSize=1, initialValue=0)
        for resp in resp2:
            self.stim2(resp)
        est = ud.estimate_reversals(self.stim2.results)
        self.assertEqual(est, 1.5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
