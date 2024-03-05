import numpy as np
from theory_model_stock_gambling.model_functions import (
    calculate_equilibrium_solution_power_utility,
)


def test_calculate_equilibrium_solution_power_utility_equal_input_equal_weights():

    MODEL_RUN_CONFIGURATION = {
    "Initial_Wealth_Agent_1": 1,
    "Intial_Wealth_Agent_2": 1,
    "Stock_Probability_High" :0.1,
    "Stock_Probability_Low": 0.9,
    "Stock_Payoff_High": 10,
    "Stock_Payoff_Low": 0.8,
    "Endowment_Probability_High_Agent_1": 0.5,
    "Endowment_Payoff_High_Agent_1":1.2,
    "Endowment_Payoff_Low_Agent_1":0.8,
    "Endowment_Probability_High_Agent_2": 0.5,
    "Endowment_Payoff_High_Agent_2":1.2,
    "Endowment_Payoff_Low_Agent_2":0.8,
    "Risk_Aversion_Agent_1": 2,
    "Risk_Aversion_Agent_2": 2,
    "Skewness_Weight": None,
    "Variance_Weight": None}

    actual_result = calculate_equilibrium_solution_power_utility(
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

    expected_weight_x_1 = 0.5
    expected_weight_x_2 = 0.5

    assert np.isclose(actual_result["x_1"] == expected_weight_x_1)
    assert np.isclose(actual_result["x_2"] == expected_weight_x_2)
