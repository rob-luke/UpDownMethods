from UpDownMethods import CORRECT, INCORRECT
import UpDownMethods as ud
import numpy as np
import matplotlib.pyplot as plt
import unittest

#
# Simulation parameters
#

responses = [CORRECT, CORRECT, CORRECT, CORRECT, INCORRECT, CORRECT, INCORRECT,
             INCORRECT, CORRECT, INCORRECT, CORRECT, CORRECT, CORRECT, CORRECT,
             CORRECT, INCORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT,
             CORRECT, CORRECT, CORRECT, CORRECT]

initalValue = 0.0

stepSize = 1.0

down = 2

up = 1


#
# Test code
#

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.results = ud.initiate_procedure()
        nextValue, self.results = ud.append_result(self.results, responses[0],
                                                   down, up, stepSize,
                                                   initalValue)
        for resp in responses[1:]:
            nextValue, self.results = ud.append_result(self.results, resp,
                                                       down, up, stepSize,
                                                       nextValue)

    def test_initiateResults(self):
        self.results = ud.initiate_procedure()
        self.assertIs(len(self.results), 0)

    def test_calculateMidpoints(self):
        mids = ud.midpoints(self.results)
        mids = mids["Midpoint"]
        mids = mids[1:4].values
        self.assertIsNone(np.testing.assert_array_equal(mids, [0.0, 1.0, 1.5]))

    def test_plotResults(self):
        ud.plot_results(self.results)
        plt.savefig('test.png', bbox_inches='tight')

    def test_runs(self):
        runs = ud.runs(self.results)
        self.assertIsNone(np.testing.assert_array_equal(
            runs["Start"].values, [1, 5, 11, 15, 19]))
        self.assertIsNone(np.testing.assert_array_equal(
            runs["Finish"].values, [5, 12, 16, 20, 24]))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
