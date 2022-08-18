import mesa

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
        self.estado = self.proximoEstado
        
