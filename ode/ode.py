def euler(f, y0, t):
    """Euler method for solving ODEs.

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
        y.append(y[i-1] + dt * f(y[i-1], t[i-1]))
    return y

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

def rk4(f, y0, t):
    """Fourth-order Runge-Kutta method for solving ODEs.

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
        k2 = f(y[i-1] + dt * k1 / 2, t[i-1] + dt / 2)
        k3 = f(y[i-1] + dt * k2 / 2, t[i-1] + dt / 2)
        k4 = f(y[i-1] + dt * k3, t[i-1] + dt)
        y.append(y[i-1] + dt * (k1 + 2*k2 + 2*k3 + k4) / 6)
    return y
