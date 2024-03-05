import math

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sympy import nsolve, symbols

from theory_model_stock_gambling.config import p


def calculate_equilibrium_solution_power_utility(W_1, W_2, prob_e_1_high, return_e_1_high, return_e_1_low, prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, risk_aversion_1, risk_aversion_2, variance_weight = None):
    """This function calculates the equilibrium solution for the model with 2 agents,
    log utility and 1 asset.

    Args:
        W_1 (float): The initial wealth of agent 1
        W_2 (float): The initial wealth of agent 2
        prob_e_1_high (float): The probability of the high endowment of agent 1
        return_e_1_high (float): The return of the high endowment of agent 1
        return_e_1_low (float): The return of the low endowment of agent 1
        prob_e_2_high (float): The probability of the high endowment of agent 2
        return_e_2_high (float): The return of the high endowment of agent 2
        return_e_2_low (float): The return of the low endowment of agent 2
        prob_R_high (float): The probability of the high return of the stock
        return_R_high (float): The return of the high return of the stock
        return_R_low (float): The return of the low return of the stock
        risk_aversion_1 (float): The risk aversion parameter of agent 1
        risk_aversion_2 (float): The risk aversion parameter of agent 2
        variance_weight (float): The weight of the variance term in the utility function of agent 2

    Returns:
        dictionary: The equilibrium solution with (x_1, x_2, p)

    """
    #Initialize values

    p = symbols("p")

    x_1 = symbols("x_1")

    x_2 = symbols("x_2")

    #Calculate equilibrium solution

    optimization_condition_agent_1 = generate_optimization_condition_agent_power_utility_1_asset(W_1, x_1, prob_e_1_high, return_e_1_high, return_e_1_low, prob_R_high, return_R_high, return_R_low, risk_aversion_1, p)

    if variance_weight is None:

        optimization_condition_agent_2 = generate_optimization_condition_agent_power_utility_1_asset(W_2, x_2,prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, risk_aversion_2, p)

    else:

            optimization_condition_agent_2 = generate_optimization_condition_agent_power_and_variance_utility_1_asset(W_2, x_2,prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, risk_aversion_2, variance_weight)


    market_clearing_condition = generate_market_clearing_condition(x_1, x_2)

    system_of_equations_to_solve = generate_system_of_equations_to_solve(optimization_condition_agent_1, optimization_condition_agent_2, market_clearing_condition)

    return calculate_equilibrium(system_of_equations_to_solve)


def generate_optimization_condition_agent_power_and_variance_utility_1_asset(W, x, prob_e_high, Return_e_high, Return_e_low, prob_R_high, Return_R_high, Return_R_low, gamma, variance_weight):
    """This function generates the optimization condition for agent 2 with power utility
    and an extra weight on variance.

    Args:
           W_1 (float): The initial wealth of agent 1
           prob_e_high (float): The probability of the high endowment
           Return_e_high (float): The return of the high endowment
           Return_2_low (float): The return of the low endowment
           Prob_R_high (float): The probability of the high return of the stock
           Return_R_high (float): The return of the high return of the stock
           Return_R_low (float): The return of the low return of the stock
           gamma (float): The risk aversion parameter
           variance_weight (float): The weight of the variance term

    Returns:
           function expression: The first order condition for the agent

    """
    variance = calculate_variance_for_bernoulli_stock(prob_R_high, 1 - prob_R_high, Return_R_high, Return_R_low)


    return prob_e_high * prob_R_high * ((Return_e_high + x * (Return_R_high - p) + W) ** (-gamma)) * (Return_R_high - p) + \
                 prob_e_high * (1 - prob_R_high) * ((Return_e_high + x * (Return_R_low - p) + W) ** (-gamma)) * (Return_R_low - p) + \
                 (1 - prob_e_high) * prob_R_high * ((Return_e_low + x * (Return_R_high - p) + W) ** (-gamma)) * (Return_R_high - p) + \
                 (1 - prob_e_high) * (1 - prob_R_high) * ((Return_e_low + x * (Return_R_low - p) + W) ** (-gamma)) * (Return_R_low - p) + variance_weight * variance





def calculate_equilibrium_solution_log_utility(W_1, W_2, prob_e_1_high, return_e_1_high, return_e_1_low, prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, skewness_weight = None):
    """This function calculates the equilibrium solution for the model with 2 agents,
    log utility and 1 asset.

    Args:
        W_1 (float): The initial wealth of agent 1
        W_2 (float): The initial wealth of agent 2
        prob_e_1_high (float): The probability of the high endowment of agent 1
        return_e_1_high (float): The return of the high endowment of agent 1
        return_e_1_low (float): The return of the low endowment of agent 1
        prob_e_2_high (float): The probability of the high endowment of agent 2
        return_e_2_high (float): The return of the high endowment of agent 2
        return_e_2_low (float): The return of the low endowment of agent 2
        prob_R_high (float): The probability of the high return of the stock
        return_R_high (float): The return of the high return of the stock
        return_R_low (float): The return of the low return of the stock

    Returns:
        dictionary: The equilibrium solution with (x_1, x_2, p)

    """
    #Initialize variables to solve for
    symbols("p")

    x_1 = symbols("x_1")

    x_2 = symbols("x_2")


    optimization_condition_agent_1 = generate_optimization_condition_agent_log_utility_1_asset(W_1, x_1, prob_e_1_high, return_e_1_high, return_e_1_low, prob_R_high, return_R_high, return_R_low)

    if skewness_weight is None:

        optimization_condition_agent_2 = generate_optimization_condition_agent_log_utility_1_asset(W_2, x_2,prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low)

    else:

            optimization_condition_agent_2 = generate_optimization_condition_agent_log_and_skewness_utility_1_asset(W_2, x_2,prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, skewness_weight)


    market_clearing_condition = generate_market_clearing_condition(x_1, x_2)

    system_of_equations_to_solve = generate_system_of_equations_to_solve(optimization_condition_agent_1, optimization_condition_agent_2, market_clearing_condition)

    return calculate_equilibrium(system_of_equations_to_solve)





def generate_optimization_condition_agent_log_utility_1_asset(W,x, prob_e_high, Return_e_high, Return_e_low, prob_R_high, Return_R_high, Return_R_low):
    """This function generates the optimization condition for agent 1 with log utility
    and 1 asset.

    Args:
        W_1 (float): The initial wealth of agent 1
        prob_e_high (float): The probability of the high endowment
        Return_e_high (float): The return of the high endowment
        Return_2_low (float): The return of the low endowment
        Prob_R_high (float): The probability of the high return of the stock
        Return_R_high (float): The return of the high return of the stock
        Return_R_low (float): The return of the low return of the stock

    Returns:
        function expression: The first order condition for agent 1 with log utility and 1 asset.

    """
    return prob_e_high * prob_R_high * (Return_R_high - p) / (W + Return_e_high + x * (Return_R_high - p)) + prob_e_high* (1-prob_R_high) * (Return_R_low- p) / (W + Return_e_high+ x* (Return_R_low - p)) + (1-prob_e_high)* prob_R_high * (Return_R_high - p) / (W + Return_e_low + x * (Return_R_high - p)) + (1-prob_e_high) * (1-prob_R_high) * (Return_R_low - p) / (W + Return_e_low + x * (Return_R_low - p))


def generate_optimization_condition_agent_log_and_skewness_utility_1_asset(W, x, prob_e_high, Return_e_high, Return_e_low, prob_R_high, Return_R_high, Return_R_low, skewness_weight):

    skewness = (1 - 2 * prob_R_high) / math.sqrt(prob_R_high * (1 - prob_R_high))

    return prob_e_high * prob_R_high * (Return_R_high - p) / (W + Return_e_high + x * (Return_R_high - p)) + prob_e_high* (1-prob_R_high) * (Return_R_low- p) / (W + Return_e_high+ x* (Return_R_low - p)) + (1-prob_e_high)* prob_R_high * (Return_R_high - p) / (W + Return_e_low + x * (Return_R_high - p)) + (1-prob_e_high) * (1-prob_R_high) * (Return_R_low - p) / (W + Return_e_low + x * (Return_R_low - p)) + skewness_weight * skewness



def generate_optimization_condition_agent_power_utility_1_asset(W,x, prob_e_high, Return_e_high, Return_e_low, prob_R_high, Return_R_high, Return_R_low, gamma, p):
    """This function generates the optimization condition for agent 1 with power utility
    and 1 asset.

    Args:
        W_1 (float): The initial wealth of agent 1
        x (sympy symbol): The fraction of wealth invested in the stock
        prob_e_high (float): The probability of the high endowment
        Return_e_high (float): The return of the high endowment
        Return_2_low (float): The return of the low endowment
        Prob_R_high (float): The probability of the high return of the stock
        Return_R_high (float): The return of the high return of the stock
        Return_R_low (float): The return of the low return of the stock
        gamma (float): The risk aversion parameter
        p (sympy symbol): The price of the stock

    Returns:
        function expression: The first order condition for agent 1 with power utility and 1 asset.

    """
    return prob_e_high * prob_R_high * ((Return_e_high + x * (Return_R_high - p) + W) ** (-gamma)) * (Return_R_high - p) + \
                 prob_e_high * (1 - prob_R_high) * ((Return_e_high + x * (Return_R_low - p) + W) ** (-gamma)) * (Return_R_low - p) + \
                 (1 - prob_e_high) * prob_R_high * ((Return_e_low + x * (Return_R_high - p) + W) ** (-gamma)) * (Return_R_high - p) + \
                 (1 - prob_e_high) * (1 - prob_R_high) * ((Return_e_low + x * (Return_R_low - p) + W) ** (-gamma)) * (Return_R_low - p)



def generate_market_clearing_condition(x_1, x_2):
    """This function generates the market clearing condition."""
    return x_1 + x_2 - 1


def generate_system_of_equations_to_solve(optimization_condition_agent_1, optimization_condition_agent_2, market_clearing_condition):
    """This function generates the system of equations to solve."""
    return [optimization_condition_agent_1, optimization_condition_agent_2, market_clearing_condition]


def calculate_equilibrium(system_of_equations_to_solve):
    """This function calculates the equilibrium.

    Args:
        system_of_equations_to_solve (tuple): A tuple containing the system of equations to solve.

    Returns:
        dict: A dictionary containing the equilibrium values with keys 'x_1', 'x_2', and 'p'.

    """
    #Initialize variables to solve for
    p = symbols("p")

    x_1 = symbols("x_1")

    x_2 = symbols("x_2")


    # Solve the system of equations
    result = nsolve(system_of_equations_to_solve, (x_1, x_2, p), (0.5, 0.5, 1))

    # Store the equilibrium values in a dictionary
    return {"x_1": result[0], "x_2": result[1], "p": result[2]}


def calculate_expected_utility_log(W_0, x, prob_e_high, Return_e_high,    Return_e_low, prob_R_high, Return_R_high, Return_R_low, price):
    """This function calculates the expected utility of an agent with log utility and 1
    asset.

    Args:
        W_0 (float): The initial wealth of the agent
        x (float): The fraction of wealth invested in the stock
        prob_e_high (float): The probability of the high endowment
        Return_e_high (float): The return of the high endowment
        Return_2_low (float): The return of the low endowment
        Prob_R_high (float): The probability of the high return of the stock
        Return_R_high (float): The return of the high return of the stock
        Return_R_low (float): The return of the low return of the stock
        p (float): The price of the stock

    Returns:
        float: The expected utility of the agent

    """
    return prob_e_high * prob_R_high * math.log(W_0 + Return_e_high + x *(Return_R_high - price)) + \
               prob_e_high * (1 - prob_R_high) * math.log(W_0 + Return_e_high + x * (Return_R_low - price)) + \
              (1 - prob_e_high) * prob_R_high * math.log(W_0 + Return_e_low + x * (Return_R_high - price)) + \
             (1 - prob_e_high) * (1 - prob_R_high) * math.log(W_0 + Return_e_low + x * (Return_R_low - price))


def calculate_expected_utility_power(W_0, x, prob_e_high, Return_e_high,    Return_e_low, prob_R_high, Return_R_high, Return_R_low, price, gamma):
    """This function calculates the expected utility of an agent with power utility and
    1 asset.

    Args:
        W_0 (float): The initial wealth of the agent
        x (float): The fraction of wealth invested in the stock
        prob_e_high (float): The probability of the high endowment
        Return_e_high (float): The return of the high endowment
        Return_2_low (float): The return of the low endowment
        Prob_R_high (float): The probability of the high return of the stock
        Return_R_high (float): The return of the high return of the stock
        Return_R_low (float): The return of the low return of the stock
        price (float): The price of the stock
        gamma (float): The risk aversion parameter

    Returns:
        float: The expected utility of the agent

    """
    return prob_e_high * prob_R_high * ((W_0 + Return_e_high + x * (Return_R_high - price)) ** (1 - gamma)) / (1 - gamma) + \
               prob_e_high * (1 - prob_R_high) * ((W_0 + Return_e_high + x * (Return_R_low - price)) ** (1 - gamma)) / (1 - gamma) + \
              (1 - prob_e_high) * prob_R_high * ((W_0 + Return_e_low + x * (Return_R_high - price)) ** (1 - gamma)) / (1 - gamma) + \
             (1 - prob_e_high) * (1 - prob_R_high) * ((W_0 + Return_e_low + x * (Return_R_low - price)) ** (1 - gamma)) / (1 - gamma)



def calculate_variance_for_bernoulli_stock(prob_high, prob_low, R_high, R_low):
    """This function calculates the variance of a Bernoulli distributed stock.

    Args:
        prob_high (float): The probability of the high return
        prob_low (float): The probability of the low return
        R_high (float): The high return
        R_low (float): The low return

    Returns:
        float: The variance of the stock

    """
    return prob_high * (R_high ** 2) + prob_low * (R_low ** 2) - (prob_high * R_high + prob_low * R_low) ** 2



def sensitivity_analysis_variance_weight(W_1, W_2, prob_e_1_high, return_e_1_high, return_e_1_low, prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, risk_aversion_1, risk_aversion_2):
    """This function generates a sensitivity analysis for the variance weight in the
    power utility model.

    Args:
        W_1 (float): The initial wealth of agent 1
        W_2 (float): The initial wealth of agent 2
        prob_e_1_high (float): The probability of the high endowment of agent 1
        return_e_1_high (float): The return of the high endowment of agent 1
        return_e_1_low (float): The return of the low endowment of agent 1
        prob_e_2_high (float): The probability of the high endowment of agent 2
        return_e_2_high (float): The return of the high endowment of agent 2
        return_e_2_low (float): The return of the low endowment of agent 2
        prob_R_high (float): The probability of the high return of the stock
        return_R_high (float): The return of the high return of the stock
        return_R_low (float): The return of the low return of the stock
        risk_aversion_1 (float): The risk aversion parameter of agent 1
        risk_aversion_2 (float): The risk aversion parameter of agent 2

    Returns:
        pd.DataFrame: A dataframe containing the sensitivity analysis for the variance weight
            columns: "Variance_Weight", "x_1", "x_2", "p", "Utility_Agent_1", "Utility_Agent_2".

    """
    #Initialize empty arrays
    variance_weights_agent_2 = np.arange(0, 0.01, 0.001)

    holding_stock_agent_1 = np.zeros(len(variance_weights_agent_2))
    holding_stock_agent_2 = np.zeros(len(variance_weights_agent_2))
    price = np.zeros(len(variance_weights_agent_2))
    utility_agent_1 = np.zeros(len(variance_weights_agent_2))
    utility_agent_2 = np.zeros(len(variance_weights_agent_2))

    for i in range(len(variance_weights_agent_2)):
        result = calculate_equilibrium_solution_power_utility(W_1, W_2, prob_e_1_high, return_e_1_high, return_e_1_low, prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, risk_aversion_1, risk_aversion_2, variance_weights_agent_2[i])

        holding_stock_agent_1[i] = result["x_1"]
        holding_stock_agent_2[i] = result["x_2"]
        price[i] = result["p"]

        utility_agent_1[i] = calculate_expected_utility_power(W_1, holding_stock_agent_1[i], prob_e_1_high, return_e_1_high, return_e_1_low, prob_R_high, return_R_high, return_R_low, price[i], risk_aversion_1)

        utility_agent_2[i] = calculate_expected_utility_power(W_2, holding_stock_agent_2[i], prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, price[i], risk_aversion_2)

    return pd.DataFrame({"Variance_Weight": variance_weights_agent_2, "x_1": holding_stock_agent_1, "x_2": holding_stock_agent_2, "p": price, "Utility_Agent_1": utility_agent_1, "Utility_Agent_2": utility_agent_2})


import plotly.graph_objects as go


def plot_sensitivity_analysis_variance_weight_output(data):
    """This function generates a plotly plot for the sensitivity analysis of the
    variance weight.

    Args:
        data (pd.DataFrame): A dataframe containing the sensitivity analysis for the variance weight
            columns: "Variance_Weight", "x_1", "x_2", "p", "Utility_Agent_1", "Utility_Agent_2".

    Returns:
        plotly.graph_objects.Figure: A plotly figure object.

    """
    data["Utility_Agent_1"] = (data["Utility_Agent_1"] + 1) / abs(data["Utility_Agent_1"].loc[0] + 1)
    data["Utility_Agent_2"] = (data["Utility_Agent_2"] + 1) / abs(data["Utility_Agent_2"].loc[0] + 1)

    # Define a custom color palette
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["Variance_Weight"],
        y=data["x_1"],
        mode="lines",
        name="Agent 1 Holding Stock",
        line={"color": colors[0]},
    ))

    fig.add_trace(go.Scatter(
        x=data["Variance_Weight"],
        y=data["x_2"],
        mode="lines",
        name="Agent 2 Holding Stock",
        line={"color": colors[1]},
    ))

    fig.add_trace(go.Scatter(
        x=data["Variance_Weight"],
        y=data["p"],
        mode="lines",
        name="Price",
        line={"color": colors[2]},
    ))

    fig.add_trace(go.Scatter(
        x=data["Variance_Weight"],
        y=data["Utility_Agent_1"],
        mode="lines",
        name="Utility Agent 1",
        line={"color": colors[3]},
    ))

    fig.add_trace(go.Scatter(
        x=data["Variance_Weight"],
        y=data["Utility_Agent_2"],
        mode="lines",
        name="Utility Agent 2",
        line={"color": colors[4]},
    ))

    fig.update_layout(
        title="Sensitivity Analysis of the Variance Weight",
        xaxis_title="Variance Weight",
        yaxis_title="Value",
        font={
            "family": "Arial, sans-serif",
            "size": 12,
            "color": "black",
        },
        legend={
            "orientation": "h",
            "yanchor": "top",
            "y": 1.12,
            "xanchor": "right",
            "x": 1,
        },
        plot_bgcolor="white",
        xaxis={
            "gridcolor": "rgb(230, 230, 230)",
            "zerolinecolor": "rgb(255, 255, 255)",
        },
        yaxis={
            "gridcolor": "rgb(230, 230, 230)",
            "zerolinecolor": "rgb(255, 255, 255)",
        },
    )

    return fig
