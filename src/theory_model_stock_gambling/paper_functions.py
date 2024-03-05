

def dict_to_latex_table(dictionary):
    """THis function generates the latex table to present the model run parameters."""
    keys = [
        "Initial Wealth Agent 1",
        "Initial Wealth Agent 2",
        "Stock Probability High",
        "Stock Probability Low",
        "Stock Payoff High",
        "Stock Payoff Low",
        "Endowment Probability High Agent 1",
        "Endowment Payoff High Agent 1",
        "Endowment Payoff Low Agent 1",
        "Endowment Probability High Agent 2",
        "Endowment Payoff High Agent 2",
        "Endowment Payoff Low Agent 2",
        "Risk Aversion Agent 1",
        "Risk Aversion Agent 2",
        "Skewness Weight",
        "Variance Weight",
    ]

    latex_table = ""
    for key in keys:
        value = dictionary.get(key.replace(" ", "_"), "")
        latex_table += f"{key} & {value} \\\\\n"
    return latex_table
