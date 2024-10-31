# Hodgkin-Huxley HH Compart Model Python Implementation 

Repo forthe Hodgkin-Huxley compartmental model of how action potentials are initiated and propagated using Python.

The visualisations will gradually get more complex. 

Fly past equations and background for installation:

## **Background**

The Hodgkin-Huxley model is a mathematical model described below, it describes how neurons generate and transmit electrical signals, specifically action potentials. It was developed by Alan Hodgkin and Andrew Huxley in 1952 based on their experiments with the giant squid axon. Their experimental results were one of the greatest feats in bio history, although it may be that the model is too complicated for most experiments used today. HH is still very helpful in understanding dynamics. 

The model incorporates ion channels, membrane potentials, and ionic currents, providing a quantitative description of the electrical characteristics of excitable cells.

## **Mathematical Equations**

Below you find the set of differential equations representing the ionic currents through the membrane.

### **Membrane Potential Equation**

$$
C_m \frac{dV}{dt} = I(t) - I_{\text{Na}} - I_{\text{K}} - I_{\text{L}}
$$

Where:

- $C_m$ is the membrane capacitance per unit area.
- $I(t)$ is the input (stimulus) current.
- $I_{\text{Na}}$, $I_{\text{K}}$, and $I_{\text{L}}$ are the sodium, potassium, and leak currents, respectively.

### **Ionic Currents**

$$
\begin{align*}
I_{\text{Na}} &= g_{\text{Na}} m^3 h (V - E_{\text{Na}}) \\
I_{\text{K}} &= g_{\text{K}} n^4 (V - E_{\text{K}}) \\
I_{\text{L}} &= g_{\text{L}} (V - E_{\text{L}})
\end{align*}
$$

Where:

- $g_{\text{Na}}$, $g_{\text{K}}$, and $g_{\text{L}}$ are the maximum conductances.
- $E_{\text{Na}}$, $E_{\text{K}}$, and $E_{\text{L}}$ are the reversal potentials.
- $m$, $h$, and $n$ are gating variables.

### **Gating Variables**

The gating variables evolve according to:

$$
\frac{dx}{dt} = \alpha_x(V)(1 - x) - \beta_x(V)x \quad \text{for } x = m, h, n
$$

With the voltage-dependent rate constants:

$$
\begin{align*}
\alpha_n(V) &= 0.01 \frac{V + 55}{1 - e^{-(V + 55)/10}} \\
\beta_n(V) &= 0.125 e^{-(V + 65)/80} \\
\alpha_m(V) &= 0.1 \frac{V + 40}{1 - e^{-(V + 40)/10}} \\
\beta_m(V) &= 4 e^{-(V + 65)/18} \\
\alpha_h(V) &= 0.07 e^{-(V + 65)/20} \\
\beta_h(V) &= \frac{1}{1 + e^{-(V + 35)/10}}
\end{align*}
$$

**Parameters:**

- $C_m = 1\, \mu\text{F/cm}^2$
- $g_{\text{Na}} = 120\, \text{mS/cm}^2$
- $g_{\text{K}} = 36\, \text{mS/cm}^2$
- $g_{\text{L}} = 0.3\, \text{mS/cm}^2$
- $E_{\text{Na}} = 50\, \text{mV}$
- $E_{\text{K}} = -77\, \text{mV}$
- $E_{\text{L}} = -54.387\, \text{mV}$


## **How the Model Works**

- **Membrane Potential (\( V \))**: The electrical potential difference across the neuron's membrane.
- **Ion Channels**: Pathways that allow ions (Na\+, K\+) to move across the membrane, affecting \( V \).
- **Gating Variables (\( m, h, n \))**: Represent the probability of ion channels being open or closed.

## **Simulation Explanation**

In this simulation:

- An external current \( I(t) \) is applied to the neuron between 10 ms and 40 ms.
- The neuron's response is calculated using the Hodgkin-Huxley equations.
- The live visualization shows how the membrane potential changes over time, illustrating action potentials.

## **Experimenting with Parameters**

You can modify parameters in `main.py` and `hodgkin_huxley.py` to see how they affect neuronal firing.

### **Examples**

1. **Changing Input Current Amplitude**

   Increase the amplitude of the input current:

   ```python
   I[int(10/dt):int(40/dt)] = 20.0  # Increase current to 20 µA/cm²
   ```
   
## **Files**

- `main.py`: The main script to run the simulation.
- `hodgkin_huxley.py`: Contains the Hodgkin-Huxley model implementation.
- `requirements.txt`: packages required.
- `README.md`: No explanation needed.

## **Requirements**

- Python 3.x
- NumPy
- Matplotlib

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/calarsenc/hodgkin-huxley-model.git

   cd hodgkin-huxley-model
```

## Ref:

Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. The Journal of physiology, 117(4), 500-544.
