import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs


# create cohort for no treatment
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE
)

simOutputs_None = cohort_none.simulate()

# create a cohort for the anticoagulant
cohort_anticoag = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG
)
simOutputs_Anticoag = cohort_anticoag.simulate()


#results
SupportMarkov.print_outcomes(simOutputs_None, "Without Drug...:")
SupportMarkov.print_outcomes(simOutputs_Anticoag, "With anticoagulant...:")

##comp outcomes if needed
SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_anticoag)


###PROBLEM 5####
# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticoag)
