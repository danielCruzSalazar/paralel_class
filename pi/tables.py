import matplotlib.pyplot as plt

# Data from the table
threads = [1, 2, 3, 4, 5, 6, 7, 8, 16, 32]
spmd = [3.193047, 4.242078, 4.916284, 5.411704, 5.513289, 5.410025, 4.559431, 4.605065, 3.37687, 2.292892]
pad_8 = [3.381773, 1.739152, 1.137117, 0.851713, 1.171623, 1.082363, 1.021851, 0.896793, 0.922081, 0.88065]
critical = [2.744352, 1.41563, 0.97023, 1.074481, 0.790846, 0.905494, 0.734326, 0.664956, 0.780952, 0.749797]
for_reduction = [2.648814, 1.487365, 0.976619, 0.705602, 0.888716, 0.855342, 0.874365, 0.661805, 0.758935, 0.738649]
for_static = [2.78412, 1.343718, 0.947269, 0.978309, 0.850938, 0.855167, 0.827946, 0.859864, 0.80265, 0.687606]
for_dynamic = [2.79679, 1.517212, 1.026065, 0.903141, 0.903333, 0.851166, 0.791687, 0.818348, 0.785907, 0.693851]
for_guided = [2.829872, 1.502496, 1.053152, 0.860332, 0.83023, 0.784378, 0.751357, 0.811531, 0.740424, 0.685266]
for_auto = [2.837239, 1.432262, 0.9997, 1.030562, 0.921653, 0.83061, 0.735503, 0.738501, 0.724168, 0.670795]

# Calculate speedup, efficiency, and parallelizability
speedup = [spmd[i] / critical[i] for i in range(len(threads))]
efficiency = [speedup[i] / threads[i] for i in range(len(threads))]
parallelizability = [critical[i] / spmd[i] for i in range(len(threads))]

# Plot speedup
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.plot(threads, speedup, marker='o')
plt.title("Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")

# Plot efficiency
plt.subplot(132)
plt.plot(threads, efficiency, marker='o')
plt.title("Efficiency")
plt.xlabel("Number of Threads")
plt.ylabel("Efficiency")

# Plot parallelizability
plt.subplot(133)
plt.plot(threads, parallelizability, marker='o')
plt.title("Parallelizability")
plt.xlabel("Number of Threads")
plt.ylabel("Parallelizability")

plt.tight_layout()
plt.show()
