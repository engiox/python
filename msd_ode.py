def mass_spring_damper(state, t, k_c_set):
    x, x_dot = state
    k_spring, c_damper = k_c_set
    
    f = [x_dot,
         -k_spring*x - c_damper*x_dot] 
    return f
