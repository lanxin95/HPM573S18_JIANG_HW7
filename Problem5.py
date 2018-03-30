#Problem 5: Projection (Weight 3): Use the calibrated model to estimate
#the mean survival time of the cohort of size 1,000. Report the 95% projection interval.
import CalibrationClasses as CalibSupport
import scr.FigureSupport as Fig

#calibration settings
SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# initialize a calibrated model
calibrated_model = CalibSupport.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(SIM_POP_SIZE, TIME_STEPS,NUM_SIM_COHORTS)

# plot the histogram of mean survival time
Fig.graph_histogram(
    data=calibrated_model.get_all_mean_survival(),
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count',
    x_range=[11, 20])

# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(ALPHA, deci=4))
