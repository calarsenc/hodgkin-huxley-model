import numpy as np

class HodgkinHuxleyModel:
    """Implementation of the Hodgkin-Huxley neuron model."""

    def __init__(self):
        # Membrane capacitance per unit area (µF/cm^2)
        self.C_m = 1.0

        # Maximum conductances (mS/cm^2)
        self.g_Na = 120.0
        self.g_K = 36.0
        self.g_L = 0.3

        # Reversal potentials (mV)
        self.E_Na = 50.0
        self.E_K = -77.0
        self.E_L = -54.387

    # Channel gating kinetics
    def alpha_n(self, V):
        return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))

    def beta_n(self, V):
        return 0.125 * np.exp(-(V + 65.0) / 80.0)

    def alpha_m(self, V):
        return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))

    def beta_m(self, V):
        return 4.0 * np.exp(-(V + 65.0) / 18.0)

    def alpha_h(self, V):
        return 0.07 * np.exp(-(V + 65.0) / 20.0)

    def beta_h(self, V):
        return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))

    def simulate(self, time, I):
        # Initialize variables
        V = np.zeros(len(time))      # Membrane potential
        m = np.zeros(len(time))      # Sodium activation gating variable
        h = np.zeros(len(time))      # Sodium inactivation gating variable
        n = np.zeros(len(time))      # Potassium activation gating variable

        # Initial conditions
        V[0] = -65.0
        m[0] = self.alpha_m(V[0]) / (self.alpha_m(V[0]) + self.beta_m(V[0]))
        h[0] = self.alpha_h(V[0]) / (self.alpha_h(V[0]) + self.beta_h(V[0]))
        n[0] = self.alpha_n(V[0]) / (self.alpha_n(V[0]) + self.beta_n(V[0]))

        dt = time[1] - time[0]

        # Simulation loop
        for i in range(1, len(time)):
            V_prev = V[i-1]
            m_prev = m[i-1]
            h_prev = h[i-1]
            n_prev = n[i-1]

            # Compute conductances
            g_Na_t = self.g_Na * m_prev**3 * h_prev
            g_K_t = self.g_K * n_prev**4
            g_L_t = self.g_L

            # Compute currents
            I_Na = g_Na_t * (V_prev - self.E_Na)
            I_K = g_K_t * (V_prev - self.E_K)
            I_L = g_L_t * (V_prev - self.E_L)

            # Update membrane potential
            V[i] = V_prev + (dt / self.C_m) * (I[i-1] - I_Na - I_K - I_L)

            # Update gating variables
            m[i] = m_prev + dt * (self.alpha_m(V_prev) * (1 - m_prev) - self.beta_m(V_prev) * m_prev)
            h[i] = h_prev + dt * (self.alpha_h(V_prev) * (1 - h_prev) - self.beta_h(V_prev) * h_prev)
            n[i] = n_prev + dt * (self.alpha_n(V_prev) * (1 - n_prev) - self.beta_n(V_prev) * n_prev)

        return V, m, h, n
