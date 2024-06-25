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
