from enum import Enum
import InputData as Data
import scr.MarkovClasses as MarkovCls

class HealthStats(Enum):
    """ health states of patients with stroke """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STROKE_DEATH = 3
    NORMAL_DEATH = 4


class Therapies(Enum):
    """ MONO VS COMBINATION THERAPY """
    NONE = 0
    ANTICOAG = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        #DISCOUNT RATE
        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL


        #annual stroke
        self._annualstrokecost=Data.STROKE_COST

        #annual treatment cost
        if self._therapy == Therapies.NONE:
            self._annualTreatmentCost = 0
        if self._therapy == Therapies.ANTICOAG:
            self._annualTreatmentCost = Data.ANTICOAG_COST


        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk
        self._treatmentRR = 0

         # calculate transition probabilities and treatment cost depending of which therapy options is in u
        # treatment cost baseline
        if therapy == Therapies.NONE:
            self._prob_matrix =calculate_prob_matrix()
            self._annualStateCosts = Data.STATE_COST
        else:
            self._prob_matrix = calculate_prob_matrix_anticoag()
            self._annualStateCosts = Data.ANTICOAG_STATE_COST

        # annual state costs and utilities
        self._annualStateUtilities = Data.ANNUAL_STATE_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        if state == HealthStats.STROKE_DEATH or state==HealthStats.NORMAL_DEATH:
            return 0
        else:
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        if state == HealthStats.STROKE_DEATH or state==HealthStats.NORMAL_DEATH:
            return 0
        else:
            return self._annualStateUtilities[state.value]

    def get_annualstrokecost(self):
        return self._annualstrokecost
    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost



def add_background_mortality(prob_matrix):

    # find the transition rate matrix
    rate_matrix = MarkovCls.discrete_to_continuous(prob_matrix, 1)
    # add mortality rates
    for s in HealthStats:
        if s not in [HealthStats.DEATH, HealthStats.NORMAL_DEATH]:
            rate_matrix[s.value][HealthStats.NORMAL_DEATH.value] \
                = -np.log(1 - Data.ANNUAL_PROB_BACKGROUND_MORT)

    # convert back to transition probability matrix
    prob_matrix[:], p = MarkovCls.continuous_to_discrete(rate_matrix, Data.DELTA_T)
    # print('Upper bound on the probability of two transitions within delta_t:', p)




def calculate_prob_matrix_anticoag():
    """ :returns transition probability matrix under anticoagulation use"""

    # create an empty matrix populated with zeroes
    prob_matrix = []
    for s in HealthStats:
        prob_matrix.append([0] * len(HealthStats))

    # for all health states
    for s in HealthStats:
        # if the current state is post-stroke
        if s == HealthStats.POST_STROKE:
            # post-stoke to stroke
            prob_matrix[s.value][HealthStats.STROKE.value]\
                = Data.RR_STROKE*Data.TRANSITION_MATRIX_NONE[s.value][HealthStats.STROKE.value]
            # post-stroke to death
            prob_matrix[s.value][HealthStats.DEATH.value] \
                = Data.RR_STROKE * Data .RR_BLEEDING * Data.TRANSITION_MATRIX_NONE[s.value][HealthStats.DEATH.value]
            # staying in post-stroke
            prob_matrix[s.value][s.value]\
                = 1 - prob_matrix[s.value][HealthStats.STROKE.value] - prob_matrix[s.value][HealthStats.DEATH.value]
        else:
            prob_matrix[s.value] = Data.TRANSITION_MATRIX_NONE[s.value]

    return prob_matrix
