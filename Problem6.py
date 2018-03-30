#Problem 6: Projection (Weight 1): Recalibrate the model against a clinical study
# that reports 800 of 1146 participants survived at the end of the 5-year study period.
# What changes do you observe in the credible interval of the estimated annual mortality probability
# and in the projection interval of the mean survival time?

import scr.FigureSupport as Fig
import numpy as np
import CalibrationClasses as CalibClasses

#calibration settings
SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the percentage of patients survived beyond 5 years
OBS_N = 1146         # number of patients involved in the study
OBS_K = 800         #estimated number of patients survived beyond 5 years
OBS_Q = OBS_K/OBS_N #estimated percentage of patients survived beyond 5 years
#for a binomial distribution: variance for the estimated number =np(1-p)
OBS_Var=OBS_N*OBS_Q*(1-OBS_Q)
OBS_STDEV = np.sqrt(OBS_Var)

# minimum, maximum and the number of samples for the five year survival probability probablity
POST_L, POST_U, POST_N = 0.01, 0.15, 1000


# create a calibration object
calibration = CalibClasses.Calibration(POST_N)
# sample the posterior of the mortality probability
calibration.sample_posterior(OBS_N,POST_L,POST_U,POST_N,SIM_POP_SIZE,TIME_STEPS,OBS_K,OBS_STDEV,NUM_SIM_COHORTS)

#flat prior
mortalitySamples = np.random.uniform(
            low=POST_L,
            high=POST_U,
            size=POST_N)
#Fig.graph_histogram(
#    data=mortalitySamples,
#    title='Prior',
#    x_label='Mortality Probability',
#    y_label='Counts',
#    x_range=[POST_L, POST_U])

# create the histogram of the resampled mortality probabilities (posterior)
Fig.graph_histogram(
    data=calibration.get_mortality_resamples(),
    title='Histogram of Resampled Mortality Probabilities',
    x_label='Mortality Probability',
    y_label='Counts',
    x_range=[POST_L, POST_U])

# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(ALPHA, 4))

# effective sample size
txtEff = 'Effective sample size: {:.1f}'.format(calibration.get_effective_sample_size())
print(txtEff)

# initialize a calibrated model
calibrated_model = CalibClasses.CalibratedModel('CalibrationResults.csv')
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