# Edison Ogonaga - Taller 04: Interpolación y polinomios de Taylor
import numpy as np
import matplotlib.pyplot as plt


def taylor_ln(x, n):
    """Polinomio de Taylor de grado n de ln(x) alrededor de x0 = 1."""
    suma = 0
    for k in range(1, n + 1):
        suma = suma + ((-1)**(k + 1) / k) * (x - 1)**k
    return suma


# 1. Verificación y cálculos del taller
print(f"P_3(1.5)  = {taylor_ln(1.5, 3):.6f}")
print(f"P_10(1.5) = {taylor_ln(1.5, 10):.6f}")
print(f"P_10(2.5) = {taylor_ln(2.5, 10):.6f}")

for n in range(1, 31):
    err = abs(np.log(1.5) - taylor_ln(1.5, n))
    if err < 1e-6:
        print(f"Menor grado n con error < 10^-6 en x=1.5: n = {n} (error = {err:.2e})")
        break

# 2. Gráfica 1: ln(x) y P_1, P_2, P_3, P_6 en [0.1, 3]
x = np.linspace(0.1, 3, 400)

plt.figure(figsize=(8, 5), dpi=150)
plt.plot(x, np.log(x), 'k-', linewidth=2.2, label=r'$\ln(x)$')
plt.plot(x, taylor_ln(x, 1), 'b--', linewidth=1.8, label=r'$P_1(x)$')
plt.plot(x, taylor_ln(x, 2), 'g-.', linewidth=1.8, label=r'$P_2(x)$')
plt.plot(x, taylor_ln(x, 3), 'm:', linewidth=2.0, label=r'$P_3(x)$')
plt.plot(x, taylor_ln(x, 6), 'c--', linewidth=1.8, label=r'$P_6(x)$')
plt.plot(1, 0, 'ro', markersize=7, zorder=5, label=r'Punto $(1, 0)$')

plt.ylim(-3, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Gráfica 1: $\ln(x)$ y Polinomios de Taylor alrededor de $x_0 = 1$')
plt.grid(True, alpha=0.3)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('grafica1.png', dpi=150)
plt.savefig('Jair Ogonaga grafica1_taylor_ln.png', dpi=150)

# 3. Gráfica 2: Error |ln(x) - P_n(x)| para n = 1, 2, ..., 30 en x = 1.5 y x = 2.5
n_vals = np.arange(1, 31)
err_15 = [abs(np.log(1.5) - taylor_ln(1.5, n)) for n in n_vals]
err_25 = [abs(np.log(2.5) - taylor_ln(2.5, n)) for n in n_vals]
cota_15 = (0.5**(n_vals + 1)) / (n_vals + 1)

plt.figure(figsize=(8, 5), dpi=150)
plt.semilogy(n_vals, err_15, 'bo-', markersize=4, label=r'Error en $x = 1.5$: $|\ln(1.5) - P_n(1.5)|$')
plt.semilogy(n_vals, cota_15, 'g--', linewidth=2, label=r'Cota en $x = 1.5$: $\frac{0.5^{n+1}}{n+1}$')
plt.semilogy(n_vals, err_25, 'rs-', markersize=4, label=r'Error en $x = 2.5$: $|\ln(2.5) - P_n(2.5)|$')

plt.xlabel('Grado del polinomio (n)')
plt.ylabel(r'Error absoluto $|\ln(x) - P_n(x)|$ (escala log)')
plt.title(r'Gráfica 2: Error del Polinomio de Taylor de $\ln(x)$ y Cota Teórica')
plt.grid(True, which='both', linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.savefig('grafica2.png', dpi=150)
plt.savefig('Jair Ogonaga grafica2_error_taylor_ln.png', dpi=150)
plt.show()
