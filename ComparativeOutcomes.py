import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov

# simulate no therapy
# create a cohort
cohort_none = MarkovCls.Cohort(id=0, therapy=P.Therapies.NONE)
# simulate cohort
simOutputs_NONE = cohort_none.simulate()

# simulate anticoagulation therapy
cohort_anticoag = MarkovCls.Cohort(id=1, therapy=P.Therapies.ANTICOAG)
simOutputs_ANTICOAG = cohort_anticoag.simulate()

SupportMarkov.draw_survival_curves_and_histograms(simOutputs_NONE, simOutputs_ANTICOAG)

SupportMarkov.print_outcomes(simOutputs_NONE, "No therapy")
SupportMarkov.print_outcomes(simOutputs_ANTICOAG, "Anticoagulation theraoy")

SupportMarkov.print_comparative_outcomes(simOutputs_NONE, simOutputs_ANTICOAG)

SupportMarkov.report_CEA_CBA(simOutputs_NONE, simOutputs_ANTICOAG)
