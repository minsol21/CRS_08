import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha_r = 0.6
alpha_p = 0.2
tau = 2
delta_t = 0.0001
t_max = 50
n_steps = int(t_max / delta_t)

# Initial conditions
ns_0 = 1
m_0 = 1

# Time array
t = np.arange(0, t_max, delta_t)

# Initialize arrays for ns and m
ns = np.zeros(n_steps)
m = np.zeros(n_steps)
ns[0] = ns_0
m[0] = m_0

# Handling delay for the initial steps
delay_steps = int(tau / delta_t)

# Forward integration using Euler method
for i in range(1, n_steps):
    if i < delay_steps:
        ns_tau = ns_0
    else:
        ns_tau = ns[i - delay_steps]
    
    dns_dt = -alpha_r * ns[i-1] * (ns[i-1] + 1) + alpha_r * ns_tau * (ns_tau + 1)
    dm_dt = -alpha_p * ns[i-1] * m[i-1]
    
    ns[i] = ns[i-1] + dns_dt * delta_t
    m[i] = m[i-1] + dm_dt * delta_t

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, ns, label='n_s(t)')
plt.xlabel('Time')
plt.ylabel('n_s(t)')
plt.title('Normalized Number of Searching Robots')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, m, label='m(t)', color='orange')
plt.xlabel('Time')
plt.ylabel('m(t)')
plt.title('Normalized Number of Uncollected Pucks')
plt.legend()

plt.tight_layout()

plt.savefig('crs08_a_searching_and_avoiding.png')


# Show the plots
plt.show()
