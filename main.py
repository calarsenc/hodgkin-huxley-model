import numpy as np
import matplotlib.pyplot as plt
from hodgkin_huxley import HodgkinHuxleyModel

def main():
    # Time parameters
    T = 50.0  # Total time in ms
    dt = 0.01  # Time step in ms
    time = np.arange(0, T + dt, dt)

    # Input current
    I = np.zeros(len(time))
    I[int(10/dt):int(40/dt)] = 10.0  # Inject current between 10 ms and 40 ms

    # Initialize the model
    neuron = HodgkinHuxleyModel()

    # Run the simulation
    V, m, h, n = neuron.simulate(time, I)

    # Plot the results
    plt.figure(figsize=(12, 8))

    # Membrane potential subplot
    plt.subplot(2, 1, 1)
    plt.plot(time, V, 'b')
    plt.title('Hodgkin-Huxley Neuron Model Simulation')
    plt.ylabel('Membrane Potential (mV)')

    # Input current subplot
    plt.subplot(2, 1, 2)
    plt.plot(time, I, 'r')
    plt.xlabel('Time (ms)')
    plt.ylabel('Input Current ($\mu$A/cm$^2$)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
