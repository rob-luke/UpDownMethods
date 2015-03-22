import matplotlib.pyplot as plt
import numpy as np


def plot_results(results):

    figure = plt.figure()
    figure.add_subplot(111)
    plt.hold(True)

    # Plot correct responses
    corr = results[results['Responses'] == True]
    plt.scatter(corr.index+1, corr.Value, s=50, marker='+', c='k')

    # Plot incorrect responses
    incorr = results[results['Responses'] == False]
    plt.scatter(incorr.index+1, incorr.Value, s=50, marker='_', c='k')

    # Indicate reversals
    # reversal = results[results['Reversal'] == True]
    # plt.scatter(reversal.index+1, reversal.Value, facecolors='none',
    # edgecolors='k', s=200)

    # Track the runs
    runY = min(results.Value)-1
    for run in np.unique(np.round(results['Run']))[:-1]:

        run_n = results[abs(results['Run'] - run) <= 0.5]
        start = min(run_n["Trial"])
        end = max(run_n["Trial"])
        mid = start + (end-start)/2

        plt.errorbar(mid, runY, xerr=(end-start)/2, c='k')
        plt.annotate(str(int(run)), xy=(mid, runY-0.5), xytext=(mid, runY-0.5))

    plt.xlim(-0.5, max(results.index) + 2.5)
    plt.ylabel('Stimulus Value', fontsize=14)
    plt.xlabel('Trial Number', fontsize=14)

    return figure
