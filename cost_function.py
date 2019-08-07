def cost_function(x):

    k_spring, c_damper = x

    # import functions
    from numpy import linspace, max, abs
    from scipy.integrate import odeint
    import msd_ode
    
    # define constants
    init_cond = [0.3, -0.1]
    t_init    = 0.0
    t_final   = 100.0
    time_step = 0.005
    num_data =int((t_final-t_init)/time_step)

    # integrate 
    t_all = linspace(t_init, t_final, num_data)
    y_all = odeint(msd_ode.mass_spring_damper, init_cond, t_all, 
                   args=([k_spring, c_damper],))
    
    # find maximum undershoot               
    xout = y_all[:,0]
    x_negative = abs(xout[xout<0])
    max_undershoot = max(x_negative)
    return max_undershoot
