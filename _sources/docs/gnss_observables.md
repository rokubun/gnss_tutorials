---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# GNSS observables

We understand by GNSS observables as

- pseudorange
- carrier phase
- Doppler
- Signal-to-Noise ratio

These are delivered usually in RINEX format

## Observable model

The GNSS observables can be modelled usign the following expressions for the code and phase

$$
P = \rho + c \cdot (dt_r - dt^s) +  \frac{40.3}{f^2}\cdot STEC_r^s+T + b_P + \varepsilon_P
$$

$$
L = \rho + c \cdot (dt_r - dt^s) -  \frac{40.3}{f^2}\cdot STEC_r^s+ T + b_L + \lambda \cdot N + \varepsilon_P
$$

where:

- $P$ and $L$ represent the pseudorange and carrier-phase respectively
- $\rho$ is the geometric (Euclidean) distance between the receiver and satellite
- $dt_r$ and $dt^s$ is the clock bias for the receiver and satellite. $c$ is the speed of light
- $f$ is the frequency of the signal (and $\lambda$ is the corresponding wavelength)
- $b_P$ and $b_L$ are the code and phase hardware biases respectively
- $N$ is the integer phase ambiguity


## Observable combination

### Ionospheric (geometry-free) combination

Between frequencies $a$ and $b$. Assuming that $f_b > f_a$, the code combination
can be expressed as:

$$
PI_{a,b} = P_a - P_b = 40.3 \cdot \left ( \frac{1}{f_a^2} - \frac{1}{f_b^2} \right) \cdot STEC_r^s + b_{P,a} - b_{P,b} + \sqrt{2} \cdot \varepsilon_P
$$

On the other hand, the ionospheric combination of phases can be expressed as:

```{math}
:label: iono_comb_phase
LI_{a,b} = P_b - P_a = 40.3 \cdot \left ( \frac{1}{f_a^2} - \frac{1}{f_b^2} \right) \cdot STEC_r^s + b_{L,b} - b_{L,a} + {\lambda}_b \cdot N_b - {\lambda}_a \cdot N_a + \sqrt{2} \cdot \varepsilon_L
```


In GNSS textbooks, the term $40.3 \cdot \left ( \frac{1}{f_a^2} - \frac{1}{f_b^2} \right)$ is usually referred to the alpha constant $\alpha_{LI}$ for the given frequencies

For example, the $\alpha_{LI}$ for GPS L1 and L2 frequencies can be computed as follows:

```{code-cell}
40.3 * (1 / (10.23e6*120)**2 - 1 / (10.23e6*154)**2)
```

On the other hand, the term $b_{P,a} - b_{P,b}$ is known as the Differential
Code Bias (DCB) between the codes $P_a$ and $P_b$ (i.e. $DCB(P_a, P_b)$).

This combination is usually employed when building models for ionospheric estimation
due to the fact that the Slant Total Electron Content (STEC) is exposed.
