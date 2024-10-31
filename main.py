import numpy as np
import matplotlib.pyplot as plt
from hodgkin_huxley import HodgkinHuxleyModel
from matplotlib.animation import FuncAnimation

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

    # Live visualization
    fig, ax = plt.subplots()
    ax.set_title('Live Membrane Potential')
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Membrane Potential (mV)')
    line, = ax.plot([], [], 'b')

    def init():
        ax.set_xlim(0, T)
        ax.set_ylim(np.min(V) - 5, np.max(V) + 5)
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(time[:frame], V[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=1)
    plt.show()

if __name__ == "__main__":
    main()
