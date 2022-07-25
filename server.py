from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from portrayal import portrayCell
from life_model import GameOfLife


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 50, 50, 250, 250)

server = ModularServer(GameOfLife, [canvas_element], "Game of Life",
                       50, 50)
