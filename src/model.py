import mesa
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from random import random
import matplotlib.pyplot as plt
from mesa.datacollection import DataCollector
from src.agent import GameOfLifeAgent


def compute_likeness(model):
    """Função que retorna a semelhanca em porcentagem do estado atual do modelo, comparado ao estado passado."""

    soma = 0
    for grid_content, x, y in model.grid.coord_iter():
            celula_atual_estado = grid_content.estado
            celula_anterior_estado = model.lastGrid.grid[x][y].estado
            if celula_atual_estado != celula_anterior_estado:
                soma = soma + 1 
    number_of_cells = model.largura * model.altura
    semelhanca =  (number_of_cells - soma)/number_of_cells
    return semelhanca
def compute_alive_cells(model):
    """Função que retorna a porcentagem de celulas vivas (variavel dependente)"""

    alive_cells = 0
    # numero de celulas 
    number_of_cells = model.largura * model.altura

    for grid_content, x, y in model.grid.coord_iter():
        if grid_content.estado  == grid_content.VIVO:
            alive_cells = alive_cells + 1
    # porcentagem de celulas vivas = celulas_vivas/total_celulas
    alive_cells_percent = alive_cells / number_of_cells
    return alive_cells_percent
def compute_dead_cells(model):
    """Função que retorna a porcentagem de celulas mortas (variavel dependente)"""
    dead_cells = 0
     # numero de celulas 
    number_of_cells = model.largura * model.altura
    
    for grid_content, x, y in model.grid.coord_iter():
        if grid_content.estado  == grid_content.MORTO:
            dead_cells = dead_cells + 1
    # porcentagem de celulas mortas = celulas_mortas/total_celulas
    dead_cells_percent = dead_cells / number_of_cells

    return dead_cells_percent


class GameOfLifeModel(mesa.Model):
    """
    Classe para o modelo do Game Of Life
    """
    def __init__(self, largura=50, altura=50, survive=[2,3], born=[3],density=.5):
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

        print(born)
        print(survive)
        # coord_iter(): An iterator that returns coordinates as well as cell contents.

        for grid_content, x, y in self.grid.coord_iter():
            celula = GameOfLifeAgent((x,y), self, survive, born, self.semelhanca)
            celula2 = GameOfLifeAgent((x,y), self, survive, born, self.semelhanca)
            # para o nosso teste, os estados das celulas serao definidos aleatoriamente (50%)
            # semelhante a densidade de celulas vivas
            if random() > density :
                celula.estado = celula.VIVO
            self.grid.place_agent(celula, (x,y))
            self.lastGrid.place_agent(celula2, (x,y))
            self.schedule.add(celula)
        
        self.running = True

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()   



