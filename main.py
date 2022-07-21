from money_model import MoneyModel
import matplotlib.pyplot as plt
import numpy as np


def main(): 
    modelo = MoneyModel(50, 10, 10)
    # loop para dar 10 passos:
    for i in range(20):
        modelo.step() 
        
    agent_counts = np.zeros((modelo.grid.width, modelo.grid.height))
    for cell in modelo.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count
    gini = modelo.datacollector.get_model_vars_dataframe()
    gini.plot()
    plt.imshow(agent_counts, interpolation="nearest")
    plt.colorbar()
    plt.show()


    
    
    
    # distribuicao de riqueza pelos agentes:
    # agent_wealth = [a.riqueza for a in modelo.schedule.agents]
    # plt.hist(agent_wealth)
    # plt.show()




    # media de distribuicao depois de 100 steps em que cada step gera 10 agentes
    # toda_riqueza = []
    # for j in range(100):
    #     model = MoneyModel(10)
    #     for i in range(10):
    #         model.step()

    #     # Store the results
    #     for agent in model.schedule.agents:
    #        toda_riqueza.append(agent.riqueza)

    # plt.hist(toda_riqueza, bins=range(max(toda_riqueza) + 1))
    # plt.show()



if __name__ == "__main__":
    main()
