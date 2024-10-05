import time
import matplotlib.pyplot as plt

def function(n):
    counter = 0
    for i in range(n//2, n + 1):
        for j in range(1, n - n//2 + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

def medir_tiempos(ns):
    tiempos = []
    for n in ns:
        print(f"Procesando n = {n}...")
        inicio = time.time()
        function(n)
        fin = time.time()
        tiempo = fin - inicio
        tiempos.append(tiempo)
        print(f"n = {n}, tiempo = {tiempo:.6f} segundos\n")
    return tiempos

def graficar(ns, tiempos):
    plt.figure(figsize=(10, 6))
    plt.plot(ns, tiempos, marker='o', linestyle='-', color='b')
    plt.xlabel('Tamaño de input n')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución vs. Tamaño de input n')
    plt.xscale('log') 
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.tight_layout()
    
    plt.savefig('tiempo_ejecucion_vs_n.png')
    print("La gráfica ha sido guardada como 'tiempo_ejecucion_vs_n.png'.")
    
    plt.show()

if __name__ == "__main__":
    ns = [1, 10, 100, 1000, 10000, 20000, 50000]
    
    tiempos = medir_tiempos(ns)
    
    print("\nResultados:")
    print("n\tTiempo (segundos)")
    for n, t in zip(ns, tiempos):
        print(f"{n}\t{t:.6f}")
    
    graficar(ns, tiempos)
