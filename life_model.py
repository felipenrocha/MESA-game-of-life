import mesa
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from random import random
import matplotlib.pyplot as plt
from mesa.datacollection import DataCollector

variable = {}


def compute_likeness(model):
    print(model.semelhanca)
    return model.semelhanca


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

        self.datacollector = DataCollector(model_reporters={"likeness": compute_likeness})



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


    def setSemelhanca(self, elementos_diferentes):
        """
            Funcao que calcula a a porcentagem de diferença entre dois grids de tamanho number_of_cells
        """
        number_of_cells = self.largura * self.altura
        return (number_of_cells - elementos_diferentes)/number_of_cells


    def diferencaEntrePassos(self):
        soma = 0
        # cellmates = self.model.grid.get_cell_list_contents([self.pos])

        for grid_content, x, y in self.grid.coord_iter():
            celula_atual_estado = grid_content.estado
            celula_anterior_estado = self.lastGrid.grid[x][y].estado
            if celula_atual_estado != celula_anterior_estado:
                soma = soma + 1 
        self.semelhanca = self.setSemelhanca(soma)

        return soma

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()   
        self.diferencaEntrePassos()







class GameOfLifeAgent(mesa.Agent):
    """Representacao dos agentes do jogo da vida: Celulas"""
    
    VIVO = 1
    MORTO = 0

    def __init__(self, posicao, modelo , survive, born, estado_inicial=MORTO):
        """
        Criacao da celula, precismos de um modelo, posicao, regras do jogo estado inicial(vivo ou morto)
        """
        super().__init__(posicao, modelo)
        self.x, self.y = posicao
        self.estado = estado_inicial
        # proximo estado inicializado como None ja que precisamos avaliar os vizinhos
        self.proximoEstado = None
        self.semelhanca = 0
        # regras do jogo
        # list of number of neighbors alive to cell to survive
        self.survive = survive
        # list of number of neighbors alive to cell to born
        self.born = born
        

    @property
    def estaVivo(self):
        if self.estado == self.VIVO:
            return True
        return False                
    @property
    def getVizinhos(self):
            return self.model.grid.iter_neighbors((self.x, self.y), True)
    
    
    def step(self):
        """Define se a celula estara viva ou morta no proximo passo
        """
        numero_vizinhos_vivos = 0
        # contando os vizinhos vivos:
        for vizinho in self.getVizinhos:
            if vizinho.estaVivo:
                numero_vizinhos_vivos += 1 

        
        # game of life rules:

        self.model.lastGrid[self.x][self.y].estado = self.estado
        if self.estaVivo:
            # se o numero de vizinhos nao for igual a algum numero 
            if numero_vizinhos_vivos not in self.survive:
                self.proximoEstado = self.MORTO
            else:
                self.proximoEstado = self.VIVO
        else:         
            if numero_vizinhos_vivos in self.born:
                    self.proximoEstado = self.VIVO
        



    def advance(self):
        '''
            Declara o proximo estado do grid, definido em step;
        '''
        self.semelhanca = self.model.semelhanca
        self.estado = self.proximoEstado
        

