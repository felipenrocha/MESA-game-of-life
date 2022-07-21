# arquivo base de tutorial


import mesa 

class MoneyAgent(mesa.Agent):
    """Um agente com riqueza inicial: 1"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.riqueza = 1
    def step(self):
            # queremos agora que o agente de 1 dinheiro para outro se ele tiver algum dinheir:
            if self.riqueza == 0:
                return 
            agente_aleatorio = self.random.choice(self.model.schedule.agents)
            agente_aleatorio.riqueza += 1
            self.riqueza -= 1
    def move(self):
        celulas_vizinhas = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)




class MoneyModel(mesa.Model):
    """Modelo com um certo numero de agentes"""
    def __init__(self, N, width, height):
        super().__init__(N)
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width, height, True)


    # Cria agentes
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

        # Adiciona o agente a uma celular aleatoria do grid:
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(a, (x,y))
    def step(self):
        """Proximo passo  do modelo:"""        
        self.schedule.step()