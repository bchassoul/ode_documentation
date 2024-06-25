# Numerical Methods for Solving ODEs

This documentation provides an overview of numerical methods for solving ordinary differential equations (ODEs) using Python. The methods covered include the Euler method, the second-order Runge-Kutta method (RK2), and the fourth-order Runge-Kutta method (RK4).

## Euler Method

The Euler method is a first-order numerical procedure for solving ODEs. It is the simplest Runge-Kutta method. The formula for the Euler method is:

    y_{n+1} = y_n + h f(t_n, y_n)

where:

    y_{n+1} is the approximated solution at the next point.
    y_n is the current value of the solution.
    h is the step size.
    f(t_n, y_n) is the derivative of y at t_n.

## Second-order Runge-Kutta Method (RK2)

The second-order Runge-Kutta method provides better accuracy than the Euler method. The formula for RK2 is:

    k_1 = h f(t_n, y_n)
    k_2 = h f(t_n + \frac{h}{2}, y_n + \frac{k_1}{2})
    y_{n+1} = y_n + k_2

where:

    k_1 and k_2 are intermediate increments.
    y_{n+1} is the approximated solution at the next point.

## Fourth-order Runge-Kutta Method (RK4)

The fourth-order Runge-Kutta method is one of the most widely used methods due to its balance between simplicity and accuracy. The formula for RK4 is:

    k_1 = h f(t_n, y_n)

    k_2 = h f(t_n + \frac{h}{2}, y_n + \frac{k_1}{2})

    k_3 = h f(t_n + \frac{h}{2}, y_n + \frac{k_2}{2})

    k_4 = h f(t_n + h, y_n + k_3)

    y_{n+1} = y_n + \frac{1}{6} (k_1 + 2k_2 + 2k_3 + k_4)

where:

    k_1, k_2, k_3, and k_4 are intermediate increments.

    y_{n+1} is the approximated solution at the next point.


---

## Reference

For detailed documentation of the functions, visit the [Reference Page](reference.md).

These numerical methods are fundamental for solving ODEs and are widely used in various scientific and engineering applications.
