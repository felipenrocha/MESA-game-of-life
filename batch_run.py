

import mesa
import pandas as pd
import numpy as np
from datetime import datetime
from src.model import GameOfLifeModel



experiments_per_parameter_configuration = 100
max_steps_per_simulation = 300
max_steps = 350
iterations = 10

params  = {
    "largura": 50,
    "altura": 50,
    "density": .5,
    "rule": ["B2/S34", "B3/S23", "B6/S16", "B36/S23", "B1357/S1357",
    "B34/S34", "B15/S28", "B1/S1",  "B12/S12", "B45/S12", "B872/S356",
    "B6731/S1234", "B58912/S34", "B6213/S912", "B91/S82", "B73/S65",
    "B51238/S38", "B86/S124659", "B87/S87542", "B234/S1235", "B1357/S2468",
    "B123456789/S123456789", "B12345/S76532", "B1/S1233456789", "B123456789/S1", 
    "B8735/S2", "B1235/23", "B123847/S2", "B983/S314678"]
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
    results_df.to_csv("results/Game_of_life_model_data" + file_name_suffix + ".csv", sep=';')
