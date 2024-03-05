from theory_model_stock_gambling.config import BLD, MODEL_RUN_CONFIGURATION
from theory_model_stock_gambling.paper_functions import dict_to_latex_table


def task_create_model_run_configuration_table(produces = BLD / "Python Input for Paper" / "tables" / "model_run_configuration.tex"):

    latex_table = dict_to_latex_table(MODEL_RUN_CONFIGURATION)
    with open(produces, "w") as f:
        f.write(latex_table)
