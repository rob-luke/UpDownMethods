import matplotlib.pyplot as plt
import UpDownMethods as ud


def plot_results(results, midpoints=False, figure=None, estimate=False,
                 reversals=False):

    if figure is None:
        figure = plt.figure()

    figure.clf()

    figure.add_subplot(111)
    plt.hold(True)

    # Plot correct responses
    corr = results[results['Responses'] == True]
    if len(corr) > 0:
        plt.scatter(corr.index+1, corr.Value, s=50, marker='+', c='k')

    # Plot incorrect responses
    incorr = results[results['Responses'] == False]
    if len(incorr) > 0:
        plt.scatter(incorr.index+1, incorr.Value, s=50, marker='_', c='k')

    # Indicate reversals
    if reversals:
        reversal = results[results['Reversal'] == True]
        if len(reversal) > 0:
            plt.scatter(reversal.index+1, reversal.Value, facecolors='none',
                        edgecolors='k', s=200)

    # Track the runs
    runs = ud.runs(results)
    for i in range(len(runs)):

        r = runs.iloc[[i]]

        start = r["Start"]
        end = r["Finish"]
        mid = start + (end-start)/2

        runY = min(results.Value)-1

        plt.errorbar(mid, runY, xerr=(end-start)/2, c='k')
        plt.annotate(str(int(i+1)), xy=(mid, runY-0.5), xytext=(mid, runY-0.5))

    if estimate is not False:
        est = ud.estimate_reversals(results, num=estimate)
        plt.axhline(y=est, ls='--')

    if midpoints:
        mids = ud.midpoints(results)
        for i in range(len(mids)):
            plt.scatter(mids['CentreTrial'].values[i],
                        mids['Midpoint'].values[i], c='r')

    if len(results) > 0:
        plt.xlim(-0.5, max(results.index) + 2.5)
    plt.ylabel('Stimulus Value', fontsize=14)
    plt.xlabel('Trial Number', fontsize=14)

    return figure
