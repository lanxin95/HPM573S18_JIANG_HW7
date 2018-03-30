import numpy as np

SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the percentage of patients survived beyond 5 years
OBS_N = 573         # number of patients involved in the study
OBS_K = 400         #estimated number of patients survived beyond 5 years
OBS_Q = OBS_K/OBS_N #estimated percentage of patients survived beyond 5 years
#for a binomial distribution: variance for the estimated number =np(1-p)
OBS_Var=OBS_N*OBS_Q*(1-OBS_Q)
OBS_STDEV=np.sqrt(OBS_Var)

# minimum, maximum and the number of samples for the five year survival probability probablity
POST_L, POST_U, POST_N = 0.01, 0.15, 1000
