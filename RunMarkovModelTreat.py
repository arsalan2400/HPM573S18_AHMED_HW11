import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create and cohort
cohort_ANTICOAG = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)

simOutputs_ANTICOAG = cohort.simulate()

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs_ANTICOAG, 'Treatment Group:')


# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)
