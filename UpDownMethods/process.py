import numpy as np
import pandas as pd
import datetime as dt


def initiate_procedure():

    results = pd.DataFrame(columns=('Responses', 'Value', 'Reversal', 'Run',
                                    'Trial', 'Direction', 'DateTime'))

    return results


def append_result(res, resp, down, up, stepSize, value):

    # Fill in the response for presented value
    # Then pass to process to fill in extra details
    # And return next stimulation value and results

    res.loc[len(res)] = [resp, value, False, 0, len(res)+1, 0, createDT()]

    return process_results(res, down, up, stepSize)


def process_results(res, down, up, stepSize):

    run = 1             # What run are we in
    cntU = 0            # How many incorrect received in a row
    cntD = 0            # How many correct received in a row
    direction = 0       # Used to track the direction of staircase

    if type(stepSize) is list:
        sSize = stepSize[0]
    else:
        sSize = stepSize

    for t in res.index:

        if t == len(res)-1:                         # If most recent response
            res.loc[t, 'Run'] = run                 # then fill values
            res.loc[t, 'Direction'] = direction

        # Default action is no change in value
        nextValue = res.loc[t, 'Value']

        if res["Responses"][t]:         # Correct response given
            cntD += 1                   # Increment the counter for down
            cntU = 0                    # Reset the up counter
            if cntD == down:            # The correct number of down responses
                cntD = 0                # Reset the counter
                if direction != -1:     # We found a reversal
                    if direction != 0:  # The first movement is not a reversal

                        # Only edit values from most recent response
                        # This is necessary when having different step sizes
                        # or reversal conditions
                        if t == len(res)-1:
                            res.loc[t, 'Reversal'] = True

                            # Runs are calculated from first to last in a level
                            # and trials can be counted in multiple runs
                            n = 0
                            while res.loc[t-n, 'Value'] == res.loc[t, 'Value']:
                                res.loc[t-n, 'Run'] += 0.5
                                n += 1

                        run += 1

                        if type(stepSize) is list:
                            if run < len(stepSize):
                                sSize = stepSize[run-1]
                            else:
                                sSize = stepSize[-1]

                    direction = -1
                nextValue = res.loc[t, 'Value'] + direction * sSize

        else:                           # Incorrect response given
            cntU += 1
            cntD = 0
            if cntU == up:
                cntU = 0
                if direction != 1:
                    if direction != 0:

                        if t == len(res)-1:
                            res.loc[t, 'Reversal'] = True

                            n = 0
                            while res.loc[t-n, 'Value'] == res.loc[t, 'Value']:
                                res.loc[t-n, 'Run'] += 0.5
                                n += 1

                        run += 1

                        if type(stepSize) is list:
                            if run < len(stepSize):
                                sSize = stepSize[run-1]
                            else:
                                sSize = stepSize[-1]

                    direction = 1
                nextValue = res.loc[t, 'Value'] + direction * sSize

    return nextValue, res


def midpoints(res):

    runs = pd.DataFrame(columns=('Run', 'Midpoint', 'CentreTrial'))

    if not res.empty:

        i = 0
        for run in np.unique(np.round(res['Run'])):
            run_n = res[abs(res['Run'] - run) <= 0.5]
            values = np.unique(run_n["Value"])

            start = min(run_n["Trial"])
            end = max(run_n["Trial"])
            mid = start + (end-start)/2

            runs.loc[i] = [int(run), np.mean(values), mid]
            i += 1

    return runs


def runs(res):

    runs = pd.DataFrame(columns=('Run', 'Start', 'Finish'))

    if not res.empty:

        i = 0
        for run in np.unique(np.round(res['Run'])):

            run_n = res[abs(res['Run'] - run) <= 0.5]
            start = min(run_n["Trial"])
            end = max(run_n["Trial"])

            runs.loc[i] = [int(run), start, end]
            i += 1

    return runs


def reversals(res):

    if res.empty:

        return pd.DataFrame(columns=('Reversals', 'Value', 'Trial'))

    else:

        res = res[res.Reversal]
        reversal = res['Run']
        reversal = reversal - 0.5

        return pd.DataFrame({'Reversal': reversal,
                             'Value': res['Value'],
                             'Trial': res['Trial']})


def estimate_reversals(res, num=2):

    if res.empty:
        return None

    else:
        rev = reversals(res)

        if len(rev) < num:
            return None

        else:
            rev = rev['Value'].values
            num = num * -1
            rev = rev[num:]
            return np.mean(rev)


def createDT(sep1="-", sep2=":"):
    datestring = '%y' + sep1 + '%m' + sep1 + '%dT' \
            + sep2 + '%H' + sep2 + '%M' + sep2 + '%S'
    return dt.datetime.strftime(dt.datetime.now(),  datestring)
