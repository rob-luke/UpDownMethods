import UpDownMethods as ud
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.results = ud.initiate_procedure()

    def test_initiateResults(self):
        self.results = ud.initiate_procedure()
        self.assertIs(len(self.results), 0)

    def test_calculateMidpoints(self):
        mids = ud.midpoints(self.results)
        self.assertIsNone(mids)

    def test_reversals(self):
        revs = ud.reversals(self.results)
        self.assertIsNone(revs)

    def test_estimate_reversals(self):
        est = ud.estimate_reversals(self.results)
        self.assertIsNone(est)

    def test_runs(self):
        runs = ud.runs(self.results)
        self.assertIsNone(runs)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
