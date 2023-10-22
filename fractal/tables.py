import matplotlib.pyplot as plt
import numpy as np

# Data from the table
threads = [1, 2, 3, 4, 5, 6, 7, 8, 16, 32]
runtime = [1.929459, 0.992957, 0.650215, 0.519064, 0.532648, 0.464947, 0.420342, 0.453607, 0.408382, 0.395018]
static = [1.962043, 1.631087, 1.154847, 0.875224, 0.854356, 0.834111, 0.635462, 0.596909, 0.490235, 0.394378]
dynamic = [1.862061, 0.975043, 0.642499, 0.517764, 0.557087, 0.447634, 0.445413, 0.440298, 0.394201, 0.395836]
dynamic2 = [1.984556, 0.977965, 0.644529, 0.531864, 0.538642, 0.435481, 0.407679, 0.396401, 0.401213, 0.407133]
dynamic4 = [1.806108, 0.980817, 0.66625, 0.52123, 0.450086, 0.419002, 0.402354, 0.458863, 0.377573, 0.388905]
guided = [1.986603, 1.015132, 0.692445, 0.496775, 0.42804, 0.40472, 0.375895, 0.34756, 0.36308, 0.370895]
guided2 = [1.892675, 1.054512, 0.67471, 0.523144, 0.44767, 0.430821, 0.435042, 0.447842, 0.372399, 0.368005]
guided4 = [1.971576, 1.045595, 0.697055, 0.506328, 0.445281, 0.439386, 0.380129, 0.407168, 0.366686, 0.364028]

# Calculate Speedup, Efficiency, and Parallelizability
speedup_static = [runtime[0] / t for t in runtime]
speedup_dynamic = [runtime[0] / t for t in static]
speedup_dynamic2 = [runtime[0] / t for t in dynamic]
speedup_dynamic4 = [runtime[0] / t for t in dynamic2]
speedup_guided = [runtime[0] / t for t in guided]
speedup_guided2 = [runtime[0] / t for t in guided2]
speedup_guided4 = [runtime[0] / t for t in guided4]

efficiency_static = [s / t for s, t in zip(speedup_static, threads)]
efficiency_dynamic = [s / t for s, t in zip(speedup_dynamic, threads)]
efficiency_dynamic2 = [s / t for s, t in zip(speedup_dynamic2, threads)]
efficiency_dynamic4 = [s / t for s, t in zip(speedup_dynamic4, threads)]
efficiency_guided = [s / t for s, t in zip(speedup_guided, threads)]
efficiency_guided2 = [s / t for s, t in zip(speedup_guided2, threads)]
efficiency_guided4 = [s / t for s, t in zip(speedup_guided4, threads)]

parallelizability_static = [e / t for e, t in zip(efficiency_static, threads)]
parallelizability_dynamic = [e / t for e, t in zip(efficiency_dynamic, threads)]
parallelizability_dynamic2 = [e / t for e, t in zip(efficiency_dynamic2, threads)]
parallelizability_dynamic4 = [e / t for e, t in zip(efficiency_dynamic4, threads)]
parallelizability_guided = [e / t for e, t in zip(efficiency_guided, threads)]
parallelizability_guided2 = [e / t for e, t in zip(efficiency_guided2, threads)]
parallelizability_guided4 = [e / t for e, t in zip(efficiency_guided4, threads)]

# Create the plots
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(threads, speedup_static, label="Static")
plt.plot(threads, speedup_dynamic, label="Dynamic")
plt.plot(threads, speedup_dynamic2, label="Dynamic(2)")
plt.plot(threads, speedup_dynamic4, label="Dynamic(4)")
plt.plot(threads, speedup_guided, label="Guided")
plt.plot(threads, speedup_guided2, label="Guided(2)")
plt.plot(threads, speedup_guided4, label="Guided(4)")
plt.xlabel("Threads")
plt.ylabel("Speedup")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(threads, efficiency_static, label="Static")
plt.plot(threads, efficiency_dynamic, label="Dynamic")
plt.plot(threads, efficiency_dynamic2, label="Dynamic(2)")
plt.plot(threads, efficiency_dynamic4, label="Dynamic(4)")
plt.plot(threads, efficiency_guided, label="Guided")
plt.plot(threads, efficiency_guided2, label="Guided(2)")
plt.plot(threads, efficiency_guided4, label="Guided(4)")
plt.xlabel("Threads")
plt.ylabel("Efficiency")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(threads, parallelizability_static, label="Static")
plt.plot(threads, parallelizability_dynamic, label="Dynamic")
plt.plot(threads, parallelizability_dynamic2, label="Dynamic(2)")
plt.plot(threads, parallelizability_dynamic4, label="Dynamic(4)")
plt.plot(threads, parallelizability_guided, label="Guided")
plt.plot(threads, parallelizability_guided2, label="Guided(2)")
plt.plot(threads, parallelizability_guided4, label="Guided(4)")
plt.xlabel("Threads")
plt.ylabel("Parallelizability")
plt.legend()

plt.tight_layout()
plt.show()
