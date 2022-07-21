# arquivo base de tutorial


import mesa 
def compute_gini(model):
    agent_wealths = [agent.riqueza for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B

class MoneyAgent(mesa.Agent):
    """Um agente com riqueza inicial: 1"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.riqueza = 5
    def step(self):
            # queremos agora que o agente de 1 dinheiro para outro se ele tiver algum dinheir:
            # if self.riqueza == 0:
            #     return 
            # agente_aleatorio = self.random.choice(self.model.schedule.agents)
            # agente_aleatorio.riqueza += 1
            # self.riqueza -= 1
            self.move()
            if self.riqueza > 0:
                self.give_money()
    def move(self):
        """Funcao para mover os agentes pelo grid."""

        posicoes_possiveis = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(posicoes_possiveis)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        celulas_com_vizinho = self.model.grid.get_cell_list_contents([self.pos])
        if len(celulas_com_vizinho) > 1:
            vizinho = self.random.choice(celulas_com_vizinho)
            vizinho.riqueza += 1
            self.riqueza -= 1





class MoneyModel(mesa.Model):
    """Modelo com um certo numer o de agentes"""
    def __init__(self, N, width, height):
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
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        )
    def step(self):
        """Proximo passo  do modelo:"""        
        self.datacollector.collect(self)
        self.schedule.step()