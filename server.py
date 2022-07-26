from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from portrayal import portrayCell
from life_model import GameOfLifeModel


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 50, 50, 500, 500)

server = ModularServer(GameOfLifeModel, [canvas_element], "Game of Life", {"altura":50, "largura":50})
