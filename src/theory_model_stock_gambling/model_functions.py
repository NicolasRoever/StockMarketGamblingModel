import math

from sympy import nsolve

from theory_model_stock_gambling.config import p, x_1, x_2


def calculate_equilibrium_solution(W_1, W_2, prob_e_1_high, return_e_1_high, return_e_1_low, prob_e_2_high, return_e_2_high, return_e_2_low, prob_R_high, return_R_high, return_R_low, skewness_weight = None):
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
    # Solve the system of equations
    result = nsolve(system_of_equations_to_solve, (x_1, x_2, p), (0.5, 0.5, 1))

    # Store the equilibrium values in a dictionary
    return {"x_1": result[0], "x_2": result[1], "p": result[2]}


def calculate_expected_utility(W_0, x, prob_e_high, Return_e_high,    Return_e_low, prob_R_high, Return_R_high, Return_R_low, price):
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
