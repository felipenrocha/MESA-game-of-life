from typing import Tuple
import mesa
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from random import random


class GameOfLifeModel(mesa.Model):
    """
    Classe para o modelo do Game Of Life
    """
    def __init__(self, largura, altura):
        # ativacao simultanea (ao inves de aleatoria) 
        # utilizamos ativacao simultanea por que o proximo estado de cada celula
        # depende do estado atual.
        self.schedule = SimultaneousActivation(self)
        # novo grid com a altura e largura passado na construcao do objeto
        self.grid = Grid(largura, altura, torus=True)

        # adicionar celulas aleatoriamente: 
        # TODO: adicionar com um clique para mudar estado da celula
        # coord_iter(): An iterator that returns coordinates as well as cell contents.

        for grid_content, x, y in self.grid.coord_iter():
            celula = GameOfLifeAgent((x,y), self)
            if random() > 0.4:
                celula.estado = celula.VIVO
            self.grid.place_agent(celula, (x,y))
            self.schedule.add(celula)
        self.running = True


    def step(self):
        self.schedule.step()      



class GameOfLifeAgent(mesa.Agent):
    """Representacao dos agentes do jogo da vida: Celulas"""
    
    VIVO = 1
    MORTO = 0

    def __init__(self, posicao: Tuple, modelo: mesa.Model, estado_inicial=MORTO):
        """
        Criacao da celula, precismos de um modelo, posicao e estado inicial(vivo ou morto)
        """
        super().__init__(posicao, modelo)
        self.x, self.y = posicao
        self.estado = estado_inicial
        # proximo estado inicializado como None ja que precisamos avaliar os vizinhos
        self.proximoEstado = None

    @property
    def estaVivo(self):
        if self.estado == self.VIVO:
            return True
        return False                
    @property
    def getVizinhos(self):
            return self.model.grid.neighbor_iter((self.x, self.y), True)
    
    
    def step(self):
        """Define se a celula estara viva ou morta no proximo passo
        """
        # TODO: variaveis independentes aqui de forma dinamica

        numero_vizinhos_vivos = 0
        # contando os vizinhos vivos:
        for vizinho in self.getVizinhos:
            if vizinho.estaVivo:
                numero_vizinhos_vivos += 1 

        # game of life basico:
        # se a celula esta viva e possui 2 ou 3 vizinhos vivos, ela permanece viva
        if self.estaVivo:
            if numero_vizinhos_vivos == 2 or numero_vizinhos_vivos == 3:
                self.proximoEstado = self.VIVO
            else:
                self.proximoEstado = self.MORTO
        # se a celula esta morta e possui exatamente 3 vizinhos, ela nasce
        else: 
            if numero_vizinhos_vivos == 3:
                self.proximoEstado = self.VIVO



    def advance(self):
        '''
            Declara o proximo estado do grid, definido em step;
        '''
        self.estado = self.proximoEstado
        

