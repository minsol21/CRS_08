# CRS08 Exercise

## Team Members
- **Minsol Kim**
- **Bhargav Solanki**

## Task (a): Searching and Avoiding Robots
### Implementation Issues

In our simulation, we encountered an unexpected issue where \( n_s(t) \) remained constant at 1 throughout the simulation duration. It was unexpected result since our expectation was that it should decrease as robots detect obstacles and engage in avoiding behavior. We attempted to adjust parameters and verify the implementation, but the behavior persisted. Plots were generated as 'crs_08_a_searching_and_avoiding.png'

One potential reason for this issue could be a misunderstanding in the implementation of the delay term \( n_s(t - \tau) \). Ensuring correct handling of the delay in the differential equations is crucial, since it directly affects how robots transition between searching and avoiding states.

## Task (b): Extending with Homing Behavior
### Simulation and Results

We simulated the extended model over a longer duration to observe the interactions between searching, avoiding, and homing behaviors, and their impact on puck collection dynamics. Plots were generated as 'crs_08_b_homing.png'

### Analysis and Interpretation

1. Normalized Number of Searching Robots ns (t):
    - Initially, all robots are in the searching state.
    - As robots find pucks and transition to the homing state, ns (t) decreases.
    - Periodically, robots return from the homing state to the searching state, leading to fluctuations in ns (t).

2. Normalized Number of Homing Robots nh (t):
    - Starts at zero and increases as robots find pucks and start homing.
    - Shows periodic decreases as robots complete the homing process and return to searching.

3. Normalized Number of Uncollected Pucks m(t):
    - Decreases over time as robots collect pucks.
    - At t=80, m(t) is reset to 0.5, causing a visible jump in the plot.
    - After the reset, the rate of puck collection depends on the number of searching robots, leading to a gradual decrease in m(t) again. 
