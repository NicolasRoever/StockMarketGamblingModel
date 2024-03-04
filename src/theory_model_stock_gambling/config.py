"""All the general configuration of the project."""
from pathlib import Path

from sympy import symbols

SRC = Path(__file__).parent.resolve()
BLD = SRC.joinpath("..", "..", "bld").resolve()

TEST_DIR = SRC.joinpath("..", "..", "tests").resolve()

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
    "Skewness_Weight": None}

p = symbols("p")

x_1 = symbols("x_1")

x_2 = symbols("x_2")



__all__ = ["BLD", "SRC", "TEST_DIR", "GROUPS"]
