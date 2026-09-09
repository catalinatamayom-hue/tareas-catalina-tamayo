import h5py
import matplotlib.pyplot as plt

def graficar_datos_hd5(ruta_archivo):
    with h5py.File(ruta_archivo, 'r') as f:
        x = f['x'][:]
        y = f['y'][:]
        e = f['e'][:]
        
    # Crear la figura
    plt.figure(figsize=(8, 6))
    
    # Graficar
    plt.errorbar(x, y, yerr=e, fmt='o', capsize=4, color='blue', ecolor='red', markersize=4, label='Datos')
    
    # Configuración de los ejes y el diseño
    plt.xlabel('Variable Independiente (x)')
    plt.ylabel('Variable Dependiente (y)')
    plt.title('Visualización de Datasets')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()
