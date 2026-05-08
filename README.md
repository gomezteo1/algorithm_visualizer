# Algorithm Visualizer

Sistema modular en Python para visualización,
análisis y aprendizaje profundo de algoritmos.

## Objetivo

Construir un motor visual educativo capaz de:

- visualizar algoritmos dinámicamente
- explicar funcionamiento interno
- mostrar ejecución paso a paso
- analizar complejidad
- detectar algoritmos automáticamente usando AST

---

# Tecnologías

- Python
- Pygame
- AST (Abstract Syntax Tree)

---

# Estado actual

## Bubble Sort Visualizer

Actualmente el sistema incluye:

- visualización dinámica de Bubble Sort
- barras persistentes optimizadas
- colores por estado
- HUD educativo
- mensajes semánticos
- estadísticas en tiempo real
- arquitectura orientada a objetos

---

# Características actuales

## Visualización

- barras animadas
- resaltado de comparaciones
- elementos ordenados en verde
- swaps visuales

## HUD

- comparaciones
- swaps
- mensajes explicativos
- nombre del algoritmo

## Rendimiento

- reutilización de objetos
- renderer persistente
- reducción de allocations

---

# Arquitectura

algorithm_visualizer/
│
├── algorithms/
├── core/
├── models/
├── rendering/
├── ui/

---

# Próximas fases

- pausa y reanudación
- control dinámico de velocidad
- interpolación suave
- sistema de eventos
- QuickSort
- MergeSort
- análisis AST
- detección automática de algoritmos

---

# Aprendizajes del proyecto

- arquitectura modular
- visualización de algoritmos
- separación de responsabilidades
- optimización de renderizado
- diseño orientado a objetos
- motores visuales en Python
