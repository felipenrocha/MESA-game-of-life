from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer


from portrayal import portrayCell
from src.model import GameOfLifeModel

import json


canvas_element = CanvasGrid(portrayCell, 50, 50, 500, 500)

chart = ChartModule([{"Label": "likeness",
                      "Color": "black"}],
                      canvas_height=50,
                      canvas_width=100,
                    data_collector_name='datacollector'
                    )
chart2 = ChartModule([{"Label": "alive_cells",
                      "Color": "green"}, {"Label": "dead_cells",
                      "Color": "red"}],  canvas_height=50,
                      canvas_width=100,
                    data_collector_name='datacollector')


rules ={}
rule = "B3/S23"

# with open('src/rules.json') as json_file:
#     rules = json.load(json_file)
# survive = rules['survive']
# born = rules['born']

server = ModularServer(GameOfLifeModel, [canvas_element, chart, chart2], "Game of Life", {"altura":50, "largura":50, "rule":rule})
