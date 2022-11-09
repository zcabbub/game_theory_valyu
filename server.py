import mesa
from model import Valyu


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r": 0.5,
    }
    if agent.wealth > 0:
        portrayal['Color'] = 'red'
        portrayal['Layer'] = 0
    else:
        portrayal['Color'] = 'grey'
        portrayal['Layer'] = 1
        portrayal['r'] = 0.2
    return portrayal


def run_server(port=8521):
    grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)

    model_params = {
        "N": 100,
        "width": 10,
        "height": 10
    }

    server = mesa.visualization.ModularServer(
        Valyu,
        [grid],
        "Valyu Model",
        model_params)
    server.port = port
    server.launch()