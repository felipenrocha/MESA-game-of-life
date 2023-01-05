

import mesa
import pandas as pd
import numpy as np
from datetime import datetime
from src.model import GameOfLifeModel
from random_rules import generate_rule


experiments_per_parameter_configuration = 100
max_steps_per_simulation = 300
# number of rules generated randomly
sample_size = 500
max_steps = 350
iterations = 1
rules = []

#  append rules to batch run
while len(rules) != sample_size:
    rule = generate_rule()
    if rule not in rules:
        rules.append(rule)

print("out")


params  = {
    "largura": 50,
    "altura": 50,
    "density": .5,
    "rule": rules
}

if __name__ == "__main__":
    # running the test
    results= mesa.batch_run(
	GameOfLifeModel,
	parameters=params,
	iterations=iterations,
	max_steps=max_steps,
	data_collection_period=-1,
	display_progress=True
    )


    # converting results to csv
    results_df=pd.DataFrame(results)
    now = str(datetime.now()).replace(":", "-").replace(" ", "-")
    file_name_suffix = ("_iter_" + str(experiments_per_parameter_configuration) + "_steps_" + str(max_steps_per_simulation) + "_" + now)
    results_df.to_csv("results/Game_of_life_model_data" + file_name_suffix + ".csv", sep=',')





