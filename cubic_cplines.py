# %%
import numpy as np 
import matplotlib.pyplot as plt

# %%
def natural_cubic_spline(x, y):
    n = len(x)
    h = np.diff(x)

    # Step 1: Hitung RHS
    RHS = np.zeros(n - 2)
    for i in range(1, n - 1):
        RHS[i - 1] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

    # Step 2: Bentuk matriks tridiagonal A secara eksplisit
    A = np.zeros((n - 2, n - 2))
    for i in range(n - 2):
        if i > 0:
            A[i, i - 1] = h[i]              # bawah diagonal
        A[i, i] = 2 * (h[i] + h[i + 1])     # diagonal utama
        if i < n - 3:
            A[i, i + 1] = h[i + 1]          # atas diagonal

    # Step 3: Selesaikan sistem linear
    c_inner = np.linalg.solve(A, RHS)

    # Step 4: Gabungkan dengan boundary natural c0 = 0 dan cn = 0
    c = np.zeros(n)
    c[1:n - 1] = c_inner

    # Step 5: Hitung koefisien a, b, d
    a = y[:-1]
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)

    for i in range(n - 1):
        b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i+1]) / 3
        d[i] = (c[i+1] - c[i]) / (3 * h[i])

    return a, b, c[:-1], d  # c[:-1] untuk kesesuaian per segmen


# %%
def clamped_cubic_spline(x, y, fp_start, fp_end):
    n = len(x)
    h = np.diff(x)

    # Step 1: Compute RHS vector
    RHS = np.zeros(n)
    RHS[0] = 3 * ((y[1] - y[0]) / h[0] - fp_start)
    RHS[-1] = 3 * (fp_end - (y[-1] - y[-2]) / h[-1])
    for i in range(1, n - 1):
        RHS[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

    # Step 2: Build full tridiagonal matrix A (size n x n)
    A = np.zeros((n, n))
    A[0, 0] = 2 * h[0]
    A[0, 1] = h[0]
    A[-1, -2] = h[-1]
    A[-1, -1] = 2 * h[-1]

    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]

    # Step 3: Solve the system A * c = RHS
    c = np.linalg.solve(A, RHS)

    # Step 4: Compute spline coefficients a, b, d
    a = y[:-1]
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)

    for i in range(n - 1):
        b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i+1]) / 3
        d[i] = (c[i+1] - c[i]) / (3 * h[i])

    return a, b, c[:-1], d


# %%
def select_spline(x, y, bc_type='natural', fp_start=None, fp_end=None):
    if bc_type == 'natural':
        
        a, b, c, d = natural_cubic_spline(x, y)
        # return a,b,c,d

    elif bc_type == 'clamped':
        a, b, c, d = clamped_cubic_spline(x, y, fp_start, fp_end)
        if fp_start is None or fp_end is None:
            raise ValueError("Clamped spline requires fp_start and fp_end.")
            

        
    else:
        raise ValueError("Unknown boundary condition type. Use 'natural' or 'clamped'.")
    return a,b,c,d

# %%
def evaluate_spline_segment(xi, ai, bi, ci, di, x_eval):
    return ai + bi*(x_eval - xi) + ci*(x_eval - xi)**2 + di*(x_eval - xi)**3

# %%
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 0.5, 2.0, 1.5, 0])
a,b,c,d = select_spline(x, y, bc_type='natural', fp_start=None, fp_end=None)
a_clamped, b_clamped, c_clamped, d_clamped = select_spline(x, y, bc_type='clamped', fp_start=1, fp_end=0)

# %%
print(y)
print(f" Parameter a adalah: {a}")
print(f" Parameter b adalah: {b}")
print(f" Parameter c adalah: {c}")
print(f" Parameter d adalah: {d}")
for i in range(len(a)):
    print(f"Spline {i}: f(x) = {a[i]:.4f} + {b[i]:.4f}(x - {x[i]}) + {c[i]:.4f}(x - {x[i]})^2 + {d[i]:.4f}(x - {x[i]})^3")

# %%
plt.figure(figsize=(10,6))
plt.plot(x, y, 'ro', label='Data points')

# Natural spline (biru)
for i in range(len(x)-1):
    xs = np.linspace(x[i], x[i+1], 100)
    ys_n = evaluate_spline_segment(x[i], a[i], b[i], c[i], d[i], xs)
    plt.plot(xs, ys_n, 'b', label='Natural Spline' if i == 0 else "")

# Clamped spline (hijau)
for i in range(len(x)-1):
    xs = np.linspace(x[i], x[i+1], 100)
    ys_c = evaluate_spline_segment(x[i], a_clamped[i], b_clamped[i], c_clamped[i], d_clamped[i], xs)
    plt.plot(xs, ys_c, 'g--', label='Clamped Spline' if i == 0 else "")

plt.title('Perbandingan Natural vs Clamped Cubic Spline')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()



