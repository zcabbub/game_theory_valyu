#%%
import mesa
#%%
class ValyuModel(mesa.Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width, height, True)

        # Create agents
        for i in range(self.num_agents):
            agent = ValyuAgent(i, self)
            self.schedule.add(agent)

            # Add them to the grid
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
#%%
class ValyuAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_token(self):
        cellmates =  self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

    def step(self):
        self.move()
        if self.wealth > 0:
            self.give_token()
#%%
model = ValyuModel(50, width=10, height=10)
for i in range(20):
    model.step()
#%% md
## visualize the number of agents residing in each cell
#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
agent_counts = np.zeros((model.grid.width, model.grid.height))
#%%
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    print(cell)
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
#%%
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()
plt.show()