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

    for t in res.index:

        res.loc[t, 'Run'] = run
        res.loc[t, 'Direction'] = direction

        nextValue = res.loc[t, 'Value']

        if res["Responses"][t]:         # Correct
            cntD += 1
            cntU = 0
            if cntD == down:
                cntD = 0
                if direction != -1:
                    if direction != 0:  # The first movement is not a reversal
                        res.loc[t, 'Reversal'] = True

                        # Runs are calculated from first to last in a level
                        # and trials can be counted in multiple runs
                        n = 0
                        while res.loc[t-n, 'Value'] == res.loc[t, 'Value']:
                            res.loc[t-n, 'Run'] += 0.5
                            n += 1
                        run += 1
                    direction = -1
                nextValue = res.loc[t, 'Value'] + direction * stepSize

        else:                                   # Incorrect
            cntU += 1
            cntD = 0
            if cntU == up:
                cntU = 0
                if direction != 1:
                    if direction != 0:
                        res.loc[t, 'Reversal'] = True

                        n = 0
                        while res.loc[t-n, 'Value'] == res.loc[t, 'Value']:
                            res.loc[t-n, 'Run'] += 0.5
                            n += 1

                        run += 1
                    direction = 1
                nextValue = res.loc[t, 'Value'] + direction * stepSize

    return nextValue, res


def midpoints(res):
    runs = pd.DataFrame(columns=('Run', 'Midpoint'))

    i = 0
    for run in np.unique(np.round(res['Run'])):
        run_n = res[abs(res['Run'] - run) <= 0.5]
        values = np.unique(run_n["Value"])

        runs.loc[i] = [int(run), np.mean(values)]
        i += 1

    return runs


def runs(res):
    runs = pd.DataFrame(columns=('Run', 'Start', 'Finish'))

    i = 0
    for run in np.unique(np.round(res['Run'])):

        run_n = res[abs(res['Run'] - run) <= 0.5]
        start = min(run_n["Trial"])
        end = max(run_n["Trial"])

        runs.loc[i] = [int(run), start, end]
        i += 1

    return runs


def createDT():
    return dt.datetime.strftime(dt.datetime.now(),  '%y-%m-%dT%H:%M:%S')