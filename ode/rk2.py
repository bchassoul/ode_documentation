def rk2(f, y0, t):
    """Second-order Runge-Kutta method for solving ODEs.

    Args:
        f (function): Function that returns the derivative of y at t.
        y0 (float): Initial value.
        t (list of floats): Time points.

    Returns:
        list of floats: Approximated solution at each time point.
    """
    y = [y0]
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        k1 = f(y[i-1], t[i-1])
        k2 = f(y[i-1] + dt * k1, t[i-1] + dt)
        y.append(y[i-1] + dt * (k1 + k2) / 2)
    return y
