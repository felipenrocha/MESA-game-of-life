def portrayCell(celula):
    '''
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the celula in its current state.
    :param celula:  the celula in the simulation
    :return: the portrayal dictionary.
    '''
    assert celula is not None
    return {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "Layer": 0,
        "x": celula.x,
        "y": celula.y,
        "Color": "black" if celula.estaVivo else "white"
    }
