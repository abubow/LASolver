from multiprocessing import Pool, Queue
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

def multiprocessingEquationGenerator(varList, eqNum:int):
    """
    Generates equations with random variables and random coefficients.
    """
    que = Queue()
    equations = []
    pool = Pool(processes=4)
    for i in range(4):
        pool.apply_async(equationGenerator, args=(varList, eqNum), callback=que.put)
    pool.close()
    pool.join()
    while not que.empty():
        equations.extend(que.get())
    return equations



start = time.time()
res = equationGenerator(['x', 'y', 'z', 'w', 'v', 'u'], 4000)
print(res.__len__())
print(time.time() - start)
start = time.time()
res = multiprocessingEquationGenerator(['x', 'y', 'z', 'w', 'v', 'u'], 1000)
print(res.__len__())
print(time.time() - start)

