import UpDownMethods as ud


class UpDownMethod(object):

    def __init__(self, down=2, up=1, stepSize=2, initialValue=0,
                 maxValue=float("inf"), minValue=-float("inf"),
                 reversals=float("inf"), trials=float("inf")):

        self.results = ud.initiate_procedure()
        self.down = down
        self.up = up
        self.stepSize = stepSize
        self.nextValue = initialValue
        self.reversals = reversals
        self.maxValue = maxValue
        self.minValue = minValue
        self.maxTrials = trials

    def __call__(self, resp):

        if self.nextValue is not None:

            if (len(ud.reversals(self.results)) < self.reversals) & \
                    (len(self.results) < self.maxTrials):

                self.nextValue, self.results = \
                        ud.append_result(self.results, resp, self.down,
                                         self.up, self.stepSize,
                                         self.nextValue)

                if (self.nextValue > self.maxValue) | \
                   (self.nextValue < self.minValue):

                    self.nextValue = None
            else:
                self.nextValue = None

        return self.nextValue
