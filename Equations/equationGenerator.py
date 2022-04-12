import multiprocessing
import random
import time

def equationGenerator(varList, eqNum:int):
    """
    Generates equations with random variables and random coefficients.
    """
    equations = []
    for i in range(eqNum):
        equation = []
        for _ in varList:
            equation.append(random.randint(-10, 10))
        for _ in varList:
            equation.append(random.choice(varList))
        equations.append(equation)
    
    return equations

def equationGeneratorHelper(varList, eqNum):
    """
    Generates equations with random variables and random coefficients.
    """
    equations = []
    for i in range(eqNum):
        equation = []
        for _ in varList:
            equation.append(random.randint(-10, 10))
        for _ in varList:
            equation.append(random.choice(varList))
        equations.append(equation)
    #print(equations.__len__())
    return equations

def multiprocessingEquationGenerator(varList, eqNum:int):
    """
    Generates equations with random variables and random coefficients.
    """
    equations = []
    pool1 = multiprocessing.Pool(processes=8)
    
    for i in range(4):
        equations.extend(pool1.apply_async(equationGeneratorHelper, args=(varList, eqNum//4)).get())
    
    pool1.close()
    pool1.join()
    return equations

def printEquations(equations):
    """
    Prints the equations.
    """
    for equation in equations:
        i = 0
        while i < len(equation)//2:
            mid = len(equation)//2
            print(f"{equation[i]}{equation[i+mid]} +", end=" ")
            i += 1
        print("\n")


# averageNormaltime = 0
# averageMultiprocessingtime = 0
# numOfRuns = 50
# for i in range(numOfRuns):
#     start = time.time()
#     res = equationGenerator(['x', 'y', 'z', 'w', 'v', 'u'], 40000)
#     end = time.time()
#     averageNormaltime += end - start

# for i in range(numOfRuns):
#     start = time.time()
#     res = multiprocessingEquationGenerator(['x', 'y', 'z', 'w', 'v', 'u'], 40000)
#     end = time.time()
#     averageMultiprocessingtime += end - start

# print(averageNormaltime/numOfRuns)
# print(averageMultiprocessingtime/numOfRuns)

printEquations(equationGenerator(['x', 'y', 'z', 'w', 'v', 'u'], 6))