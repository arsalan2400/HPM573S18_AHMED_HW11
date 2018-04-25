POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 5  # length of simulation (years)
ALPHA = 0.05        #significance level for calculating confidence intervals
DELTA_T = 1/52        #time-step length
DISCOUNT = 0.03     #annual discount rate

#NORMAL MATRIX
TRANSITION_MATRIX_NONE = [
    [None, 0.0135,      0,  0.0015, 0.017638],   # WELLNESS
    [0   ,   None,     52,       0,   0.00],   # STROKE
    [0   ,0.02981,   None, 0.00746, 0.017638],   # Post-StROKEY
    [0   ,      0,      0,    None,    0.0],   # STROKE DEAD
    [0.0 ,    0.0,    0.0,     0.0,   None]   # NO-STROKE DeaD
    ]


###ANTICOAG MATRIX####
TRANSITION_MATRIX_ANTICOAG = [
    [None, 0.0135,      0,  0.0015, 0.017638],   # WELLNESS
    [0   ,   None,     52,       0,   0.00],   # STROKE
    [0   ,0.02238,   None, 0.00746, 0.0186],   # Post-StROKEY
    [0   ,      0,      0,    None,    0.0],   # STROKE DEAD
    [0.0 ,    0.0,    0.0,     0.0,   None]   # NO-STROKE DeaD
    ]


STATE_COST = [
    0,      #WELLL
    5000,  # stroke
    200,  # PS
    0       #DEAD


ANNUAL_STATE_UTILITY = [
    1,  # well
    0.2,  # stroke
    0.9,  # post-stroke
    0  # dead
]

ANTICOAG_STATE_COST = [
    0,
    0,  # stroke
    750,  # new PS according to Q5
    0
]

ANTICOAG_COST = 1000 #suggested to try and see
RR_STROKE = 0.65
RR_BLEEDING = 1.05
STROKE_COST = 5000
ANNUAL_PROB_BACKGROUND_MORT = True
