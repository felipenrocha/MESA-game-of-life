import mesa
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from random import random
import matplotlib.pyplot as plt
from mesa.datacollection import DataCollector
from src.agent import GameOfLifeAgent


def compute_likeness(model):
    soma = 0
        # cellmates = self.model.grid.get_cell_list_contents([self.pos])

    for grid_content, x, y in model.grid.coord_iter():
            celula_atual_estado = grid_content.estado
            celula_anterior_estado = model.lastGrid.grid[x][y].estado
            if celula_atual_estado != celula_anterior_estado:
                soma = soma + 1 
    number_of_cells = model.largura * model.altura
    semelhanca =  (number_of_cells - soma)/number_of_cells
    return semelhanca
def compute_alive_cells(model):
    alive_cells = 0

    for grid_content, x, y in model.grid.coord_iter():
        if grid_content.estado  == grid_content.VIVO:
            alive_cells = alive_cells + 1
        
    return alive_cells
def compute_dead_cells(model):
    dead_cells = 0
    for grid_content, x, y in model.grid.coord_iter():
        if grid_content.estado  == grid_content.MORTO:
            dead_cells = dead_cells + 1
    return dead_cells


class GameOfLifeModel(mesa.Model):
    """
    Classe para o modelo do Game Of Life
    """
    def __init__(self, largura, altura, rules,initial_born=.5):
        # ativacao simultanea (ao inves de aleatoria) 
        # utilizamos ativacao simultanea por que o proximo estado de cada celula
        # depende do estado atual.
        self.schedule = SimultaneousActivation(self)

        # novo grid com a altura e largura passado na construcao do objeto
        self.grid = Grid(largura, altura, torus=False)
        # rules of game (variavel independente)


        # mantemos um grid do ultimo passo para fazer o calcula da diferenca entre estados. Inicializado como nenhum.
        self.lastGrid = Grid(largura, altura, torus=False)
        self.semelhanca = 0
        #  altura, largura
        self.altura = altura
        self.largura = largura

        self.datacollector = DataCollector(model_reporters={"likeness": compute_likeness, "alive_cells": compute_alive_cells, "dead_cells":compute_dead_cells})



        # adicionar celulas aleatoriamente: 


        # coord_iter(): An iterator that returns coordinates as well as cell contents.

        for grid_content, x, y in self.grid.coord_iter():
            celula = GameOfLifeAgent((x,y), self, rules['survive'],rules['born'], self.semelhanca)
            celula2 = GameOfLifeAgent((x,y), self, rules['survive'],rules['born'], self.semelhanca)
            # para o nosso teste, os estados das celulas serao definidos aleatoriamente (50%)
            if random() > initial_born :
                celula.estado = celula.VIVO
            self.grid.place_agent(celula, (x,y))
            self.lastGrid.place_agent(celula2, (x,y))
            self.schedule.add(celula)
        
        self.running = True

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()   



