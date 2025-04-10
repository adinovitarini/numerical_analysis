import numpy as np
import matplotlib.pyplot as plt

# Persamaan diferensial: dy/dt = f(t, y)
def f(t, y):
    return y - t**2 + 1

# Solusi eksak dari dy/dt = y - t^2 + 1 dengan y(0) = 0.5
def exact_solution(t):
    return (t + 1)**2 - 0.5 * np.exp(t)

# Implementasi metode Heun
def heun_method(f, t0, y0, h, t_end):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    while t < t_end:
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        y = y + h * 0.5 * (k1 + k2)
        t = t + h
        t_values.append(t)
        y_values.append(y)
    return np.array(t_values), np.array(y_values)

# Implementasi metode Euler
def euler_method(f, t0, y0, h, t_end):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    while t < t_end:
        y = y + h * f(t, y)
        t = t + h
        t_values.append(t)
        y_values.append(y)
    return np.array(t_values), np.array(y_values)
# Parameter awal
t0 = 0
y0 = 0.5
h = 0.2
t_end = 2.0
t_vals = np.linspace(t0, t_end, 100)
y_exact = exact_solution(t_vals)

# Jalankan metode numerik
t_heun, y_heun = heun_method(f, t0, y0, h, t_end)
t_euler, y_euler = euler_method(f, t0, y0, h, t_end)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_exact, label='Solusi Eksak', linewidth=2)
plt.plot(t_heun, y_heun, 'o-', label='Heun Method (RK2)', markersize=5)
plt.plot(t_euler, y_euler, 's--', label='Euler Method', markersize=5)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Perbandingan Solusi ODE: Heun vs Euler vs Solusi Eksak')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
