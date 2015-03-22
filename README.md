# Up Down Methods
Python module implementing the transformed Up-Down procedure


## Description
Framework for generating psychoacoustic stimuli parameters based on [Levitt 1970](http://www.ncbi.nlm.nih.gov/pubmed/5541744).


## Implementation

### Functions

#### Stimulation

* `initiate_procedure` returns an empty result data frame
* `append_results` appends the last result and returns the next value for stimulation


#### Results and visualisation

* `process_results` calculates procedure values and results
* `midpoints` returns the midpoints for each run
* `runs` returns the start and finish point of each run in results
* `plot_results` plots the procedure results in the same format as the original Levitt paper

### Parameters

#### Stimulation

* Up: Number of incorrect responses to go one step up
* Down: Number of correct responses to go one step down
* InitialValue: The level used on the very first run
* InitialStepSize: The increments by which the stimulus is either increased or decreased. The step size is halved after the first, third, seventh, fifteenth runs
* MaxTrials: The maximum number of trials before the procedure exits
* MaxReversals: The maximum number of reversals before the procedure exits. 
* MaxStimValue: The maximum value the parameter may take
* MinStimValue: The minimum value the parameter may take


#### Results and visualisation
* IgnoreReversals: The number of reversals to ignore when calculating the parameter	estimation


## Example

```python

import UpDownMethods as ud

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
# Experiment
#

results = ud.initiate_results()

nextValue, self.results = ud.append_result(results, responses[0], down, up, stepSize, initalValue)
                                   
for resp in responses[1:]:
    nextValue, results = ud.append_result(results, resp, down, up, stepSize, nextValue)
 

#
# Process results
#
    
ud.plot_results(self.results)
plt.savefig(‘test.png’, bbox_inches=‘tight’)

```

![Levitt Example](doc/images/Levitt-Fig4.png)
