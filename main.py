from money_model import MoneyModel
import matplotlib.pyplot as plt

def main(): 
    modelo = MoneyModel(10)
    # loop para dar 10 passos:
    for i in range(10):
        modelo.step() 
    
    
    
    # distribuicao de riqueza pelos agentes:
    # agent_wealth = [a.riqueza for a in modelo.schedule.agents]
    # plt.hist(agent_wealth)
    # plt.show()




    # media de distribuicao depois de 100 steps em que cada step gera 10 agentes
    toda_riqueza = []
    for j in range(100):
        model = MoneyModel(10)
        for i in range(10):
            model.step()

        # Store the results
        for agent in model.schedule.agents:
           toda_riqueza.append(agent.riqueza)

    plt.hist(toda_riqueza, bins=range(max(toda_riqueza) + 1))
    plt.show()



if __name__ == "__main__":
    main()
