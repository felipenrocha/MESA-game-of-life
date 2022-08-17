from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer


from portrayal import portrayCell
from life_model import GameOfLifeModel

import json


canvas_element = CanvasGrid(portrayCell, 50, 50, 500, 500)

chart = ChartModule([{"Label": "likeness",
                      "Color": "black"}],
                    data_collector_name='datacollector')
chart2 = ChartModule([{"Label": "alive_cells",
                      "Color": "green"}, {"Label": "dead_cells",
                      "Color": "red"}],
                    data_collector_name='datacollector')


rules ={}
with open('rules.json') as json_file:
    rules = json.load(json_file)
 

server = ModularServer(GameOfLifeModel, [canvas_element, chart, chart2], "Game of Life", {"altura":50, "largura":50, "rules": rules})
