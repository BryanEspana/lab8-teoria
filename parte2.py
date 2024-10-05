import time
import matplotlib.pyplot as plt

def function(n):
    if n <= 1:
        return
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            break

def medir_tiempos(ns):
    tiempos = []
    for n in ns:
        inicio = time.time()
        function(n)
        fin = time.time()
        tiempo = fin - inicio
        tiempos.append(tiempo)
        print(f"n = {n}, tiempo = {tiempo:.6f} segundos")
    return tiempos

def graficar(ns, tiempos):
    plt.figure(figsize=(10, 6))
    plt.plot(ns, tiempos, marker='o', linestyle='-', color='b')
    plt.xlabel('Tamaño de input n')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución vs. Tamaño de input n')
    plt.xscale('log')  # Escala logarítmica para el eje X
    plt.yscale('log')  # Escala logarítmica para el eje Y
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ns = [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    tiempos = medir_tiempos(ns)
    
    print("\nResultados:")
    print("n\tTiempo (segundos)")
    for n, t in zip(ns, tiempos):
        print(f"{n}\t{t:.6f}")
    
    graficar(ns, tiempos)
