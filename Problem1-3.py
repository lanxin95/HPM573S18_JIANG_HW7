#Problem1 test for the survival model
#a cohort of 573 patients over 5 years.
import SurvivalModel as SurvivalCls
MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 573     # population size of the simulated cohort
ALPHA = 0.05            # significance level
NUM_SIM_COHORTS=1000
# create a cohort of patients
myCohort = SurvivalCls.Cohort(id=571, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)
print("The five year survival percentage if the annual mortality probability is",MORTALITY_PROB,":", myCohort.get_5year_survival())

# create multiple cohorts
multiCohort = SurvivalCls.MultiCohort(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[SIM_POP_SIZE] * NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*NUM_SIM_COHORTS  # [p, p, ....]
)
# simulate all cohorts
multiCohort.simulate(TIME_STEPS)
print("Multicohort 1",multiCohort.get_cohort_5yearSurvivalPct(1))



#Problem 2: Likelihood Assumption: If the probability of 5-year survival is 𝑞,
# what probability distribution “the number of participants that survived beyond 5 years
# in a cohort of 𝑁 participants” would follow? Make sure to also specify the parameters of this distribution.
#Hint: Review the probability distributions that are discussed at the end of the Review of Probability class notes.




print("Problem2: \n"
      "the number of participants that survived beyond 5 years in a cohort of 𝑁 participants follows the binomial distibution: Bin(N,q)")

#Problem 3: Likelihood Calculation: If our survival model represents the reality,
#then the “percentage of patients survived beyond 5 years” (calculated in Problem 1)
#will represent the true probability of 5-year survival (𝑞 in Problem 2).
#Write a Python statement to calculate the likelihood that a clinical study reports 400 of 573 participants
#survived at the end of the 5-year study period if 50% of the patients in our simulated cohort survived beyond 5 years?

from scipy.stats import binom
k,n,p=400,573,0.5
print("Problem3: \n"
      "the likelihood that a clinical study reports 400 of 573 participants survived at the end of the 5-year study \n"
      "period if 50% of the patients in our simulated cohort survived beyond 5 years",binom._pmf(k, n, p))