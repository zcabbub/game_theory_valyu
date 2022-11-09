### Valyu Model - IDE version

*a model based on Boltzmann Wealth model, where agents move randomly on one of its 8 neighboring cells(Moore neighbourhood) and exchange money with a random cellmate.*

- agents with wealth are drawn in red
- agents who are broke (wealth 0) are drawn in *grey*, smaller, and above agents
who still have money.
- zero-wealth agents
  have a higher layer number, they are drawn on top of the red agents


    ## EXAMPLE USE
    model = ValyuModel(50, width=10, height=10)
    for i in range(20):
        model.step()
    
    ## visualize the number of agents residing in each cell
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        print(cell)
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count
    
    plt.imshow(agent_counts, interpolation="nearest")
    plt.colorbar()
    plt.show()