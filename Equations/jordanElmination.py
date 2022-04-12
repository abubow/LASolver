from equationGenerator import equationGenerator

def jordanElmination(equations, varList):
    """
    Performs gauss jordan elimination on the equations.
    """
    for i in range(len(equations)):
        for j in range(len(equations)):
            if equations[i][j] != 0:
                break
        if equations[i][j] == 0:
            continue
        for k in range(len(equations[i])):
            equations[i][k] /= equations[i][j]
        for k in range(len(equations)):
            if k == i:
                continue
            factor = equations[k][j]
            for l in range(len(equations[k])):
                equations[k][l] -= factor * equations[i][l]
    return equations

equation = equationGenerator(['x', 'y', 'z'], 4)
