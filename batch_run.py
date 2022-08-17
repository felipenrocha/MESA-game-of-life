

import mesa
import pandas as pd
import numpy as np
from datetime import datetime
import json
from src.model import GameOfLifeModel
from mesa.batchrunner import FixedBatchRunner



rules ={}
with open('src/rules.json') as json_file:
    rules = json.load(json_file)
print(rules)


# parameter lists for each parameter to be tested in batch run
param1 = {
    "largura": 50,
    "altura": 50,
    "density": .5,
    "survive": [2,3],
    "born":[3]
}
param2 = {
    "largura": 50,
    "altura": 50,
    "density": .5,
    "survive": [2,3],
    "born":[4]
}
param3 = {
    "largura": 50,
    "altura": 50,
    "density": .5,
    "survive": [1,3,5,7],
    "born":[1,3,5,7]
}

params = [param1, param2, param3]


experiments_per_parameter_configuration = 100
max_steps_per_simulation = 300
max_steps = 100

params  = {
    "largura": [50],
    "altura": [50],
    "density": [.5],
    "survive": [[1,3,5,7]],
    "born":[[1,3,5,7]]
}

if __name__ == "__main__":
    # data = FixedBatchRunner(
    #     GameOfLifeModel,
    #     parameters_list=params,
    #     max_steps=max_steps        
    # )
    # data.run_all()
    data = mesa.batch_run(
        GameOfLifeModel,
        parameters = params,
        max_steps = max_steps_per_simulation,
        number_processes = 1,
        data_collection_period = -1,
        display_progress = True,
    )
    results_df = pd.DataFrame(data)
    now = str(datetime.now()).replace(":", "-").replace(" ", "-")
    file_name_suffix = ("_iter_" + str(experiments_per_parameter_configuration) + "_steps_" + str(max_steps_per_simulation) + "_" + now)
    results_df.to_csv("Game_of_life_model_data" + file_name_suffix + ".csv")
