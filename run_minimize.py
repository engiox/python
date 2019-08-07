from scipy.optimize import minimize
import cost_function as cf

x0 = [0.1,0.1]
bnds = ((0, None), (0, None))

result = minimize(cf.cost_function, x0, method='SLSQP', bounds=bnds)

print(result.x)
