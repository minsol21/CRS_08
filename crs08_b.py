import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha_r = 0.6
alpha_p = 0.2
tau_a = 2
tau_h = 15
delta_t = 0.0001
t_max = 160
n_steps = int(t_max / delta_t)

# Initial conditions
ns_0 = 1
m_0 = 1
nh_0 = 0

# Time array
t = np.arange(0, t_max, delta_t)

# Initialize arrays for ns, nh, and m
ns = np.zeros(n_steps)
nh = np.zeros(n_steps)
m = np.zeros(n_steps)
ns[0] = ns_0
m[0] = m_0
nh[0] = nh_0

# Forward integration using Euler method
for i in range(1, n_steps):
    current_time = i * delta_t
    
    if current_time < tau_a:
        ns_tau_a = ns_0
    else:
        ns_tau_a = ns[int((current_time - tau_a) / delta_t)]
        
    if current_time < tau_h:
        nh_tau_h = nh_0
    else:
        nh_tau_h = nh[int((current_time - tau_h) / delta_t)]
    
    dns_dt = -alpha_r * ns[i-1] * (ns[i-1] + 1) + alpha_r * ns_tau_a * (ns_tau_a + 1) - alpha_p * ns[i-1] * m[i-1] + (1 / tau_h) * nh_tau_h
    dnh_dt = alpha_p * ns[i-1] * m[i-1] - (1 / tau_h) * nh[i-1]
    dm_dt = -alpha_p * ns[i-1] * m[i-1]
    
    ns[i] = ns[i-1] + dns_dt * delta_t
    nh[i] = nh[i-1] + dnh_dt * delta_t
    m[i] = m[i-1] + dm_dt * delta_t
    
    # Reset puck ratio at time t = 80 to m(80) = 0.5
    if current_time >= 80 and current_time < 80 + delta_t:
        m[i] = 0.5

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, ns, label='n_s(t)')
plt.xlabel('Time')
plt.ylabel('n_s(t)')
plt.title('Normalized Number of Searching Robots')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, nh, label='n_h(t)', color='green')
plt.xlabel('Time')
plt.ylabel('n_h(t)')
plt.title('Normalized Number of Homing Robots')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, m, label='m(t)', color='orange')
plt.xlabel('Time')
plt.ylabel('m(t)')
plt.title('Normalized Number of Uncollected Pucks')
plt.legend()

plt.tight_layout()

plt.savefig('crs08_b_homing.png')

plt.show()
