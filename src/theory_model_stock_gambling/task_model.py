
import numpy as np
import pandas as pd
import plotly.express as px

from theory_model_stock_gambling.config import BLD, MODEL_RUN_CONFIGURATION
from theory_model_stock_gambling.model_functions import (
    calculate_equilibrium_solution_log_utility,
    calculate_equilibrium_solution_power_utility,
    calculate_expected_utility_log,
    calculate_expected_utility_power,
    plot_sensitivity_analysis_variance_weight_output,
    sensitivity_analysis_variance_weight,
)


def task_calculate_sensitivity_analysis_power_utility_variance_weight(produces= BLD / "sensitivity_analysis_variance_weight.csv"):

    output = sensitivity_analysis_variance_weight(
    W_1 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"],
    W_2 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
    prob_e_1_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"], return_e_1_high=MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"],
    return_e_1_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
    return_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_2"],
    return_e_2_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_2"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    risk_aversion_1=MODEL_RUN_CONFIGURATION["Risk_Aversion_Agent_1"],
    risk_aversion_2=MODEL_RUN_CONFIGURATION["Risk_Aversion_Agent_2"])

    output.to_csv(produces, index=False)


def task_plot_sensitivity_analysis_power_utility_variance_weight(depends_on = BLD / "sensitivity_analysis_variance_weight.csv", produces= BLD / "sensitivity_analysis_variance_weight.png"):

    data = pd.read_csv(depends_on)
    plot = plot_sensitivity_analysis_variance_weight_output(data)
    plot.write_image(produces)





def task_calculate_equilibrium_result(produces= BLD / "equilibrium_result_power_utility.csv"):

    result = calculate_equilibrium_solution_power_utility(
    W_1 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"],
    W_2 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
    prob_e_1_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"], return_e_1_high=MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"],
    return_e_1_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
    return_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_2"],
    return_e_2_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_2"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    risk_aversion_1=MODEL_RUN_CONFIGURATION["Risk_Aversion_Agent_1"],
    risk_aversion_2=MODEL_RUN_CONFIGURATION["Risk_Aversion_Agent_2"],
    variance_weight=MODEL_RUN_CONFIGURATION["Variance_Weight"])


    result["Utility_Agent_1"] = calculate_expected_utility_power(
    W_0 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"], x = result["x_1"], prob_e_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"],
    Return_e_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"], Return_e_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], Return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    Return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    price=result["p"],
    gamma=MODEL_RUN_CONFIGURATION["Risk_Aversion_Agent_1"])


    result["Utility_Agent_2"] = calculate_expected_utility_power(
    W_0 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
    x = result["x_2"], prob_e_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
    Return_e_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_2"], Return_e_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_2"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], Return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    Return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    price=result["p"],
    gamma=MODEL_RUN_CONFIGURATION["Risk_Aversion_Agent_2"])


    print(result)

    pd.DataFrame(result, index=["Value"], columns=["x_1", "x_2", "p", "Utility_Agent_1", "Utility_Agent_2"]).to_csv(produces, index=True)





def task_calculate_equilibrium_result_log_utility(produces= BLD / "equilibrium_result_log_utility.csv"):


    result = calculate_equilibrium_solution_log_utility(
    W_1 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"],
    W_2 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
    prob_e_1_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"], return_e_1_high=MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"],
    return_e_1_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
    return_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_2"],
    return_e_2_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_2"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    skewness_weight=MODEL_RUN_CONFIGURATION["Skewness_Weight"])


    result["Utility_Agent_1"] = calculate_expected_utility_log(
    W_0 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"], x = result["x_1"], prob_e_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"],
    Return_e_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"], Return_e_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], Return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    Return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    price = result["p"])

    result["Utility_Agent_2"] = calculate_expected_utility_log(
    W_0 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
    x = result["x_2"], prob_e_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
    Return_e_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_2"], Return_e_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_2"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], Return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
    Return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
    price = result["p"])


    print(result)

    pd.DataFrame(result, index=["Value"], columns=["x_1", "x_2", "p", "Utility_Agent_1", "Utility_Agent_2"]).to_csv(produces, index=True)


def task_calculate_equilibrium_result_sensitivity_riskiness_endowment_agent_2(produces= BLD / "equilibrium_result_sensitivity.csv"):

    endowment_high_payoff_range = np.arange(1, 2.1, 0.1)
    endowment_low_payoff_range = np.flip(np.arange(0, 1.1, 0.1))

    holding_agent_1 = np.zeros(len(endowment_high_payoff_range))
    holding_agent_2 = np.zeros(len(endowment_high_payoff_range))
    price = np.zeros(len(endowment_high_payoff_range))
    welfare_agent_1 = np.zeros(len(endowment_high_payoff_range))
    welfare_agent_2 = np.zeros(len(endowment_high_payoff_range))

    for i in range(len(endowment_high_payoff_range)):
        result = calculate_equilibrium_solution_log_utility(
        W_1 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"],
        W_2 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
        prob_e_1_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"], return_e_1_high=MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"],
        return_e_1_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_e_2_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
        return_e_2_high = endowment_high_payoff_range[i],
        return_e_2_low = endowment_low_payoff_range[i], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
        return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
        skewness_weight = MODEL_RUN_CONFIGURATION["Skewness_Weight"])

        holding_agent_1[i] = result["x_1"]
        holding_agent_2[i] = result["x_2"]
        price[i] = result["p"]

        welfare_agent_1[i] = calculate_expected_utility_log(W_0 = MODEL_RUN_CONFIGURATION["Initial_Wealth_Agent_1"], x = result["x_1"], prob_e_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_1"],
        Return_e_high = MODEL_RUN_CONFIGURATION["Endowment_Payoff_High_Agent_1"], Return_e_low = MODEL_RUN_CONFIGURATION["Endowment_Payoff_Low_Agent_1"], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], Return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
        Return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
        price = result["p"])

        welfare_agent_2[i] = calculate_expected_utility_log(W_0 = MODEL_RUN_CONFIGURATION["Intial_Wealth_Agent_2"],
        x = result["x_2"], prob_e_high = MODEL_RUN_CONFIGURATION["Endowment_Probability_High_Agent_2"],
        Return_e_high = endowment_high_payoff_range[i],
        Return_e_low = endowment_low_payoff_range[i], prob_R_high = MODEL_RUN_CONFIGURATION["Stock_Probability_High"], Return_R_high = MODEL_RUN_CONFIGURATION["Stock_Payoff_High"],
        Return_R_low = MODEL_RUN_CONFIGURATION["Stock_Payoff_Low"],
        price = result["p"])

    result = pd.DataFrame({"Endowment_High_Payoff_Agent_2": endowment_high_payoff_range, "Endowment_Low_Payoff_Agent_2": endowment_low_payoff_range, "Holding_Agent_1": holding_agent_1, "Holding_Agent_2": holding_agent_2, "Price": price, "Welfare_Agent_1": welfare_agent_1, "Welfare_Agent_2": welfare_agent_2})

    result.to_csv(produces, index=False)


def task_plot_sensitivity_analysis_payoff_agent_2(depends_on = BLD / "equilibrium_result_sensitivity.csv", produces= BLD / "equilibrium_result_sensitivity.png"):

    result = pd.read_csv(depends_on)

    fig = px.scatter(result, x="Endowment_High_Payoff_Agent_2", y="Holding_Agent_1", title="Sensitivity Analysis of the Payoff of Agent 2")

    fig.add_scatter(x=result["Endowment_High_Payoff_Agent_2"], y=result["Holding_Agent_2"], mode="lines", name="Agent 2")

    fig.add_scatter(x=result["Endowment_High_Payoff_Agent_2"], y=result["Price"], mode="lines", name="Price")

    fig.add_scatter(x=result["Endowment_High_Payoff_Agent_2"], y=result["Welfare_Agent_1"], mode="lines", name="Welfare Agent 1")

    fig.add_scatter(x=result["Endowment_High_Payoff_Agent_2"], y=result["Welfare_Agent_2"], mode="lines", name="Welfare Agent 2")

    fig.write_image(produces)
