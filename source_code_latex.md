
### superposed-pulses<a name="superposed-pulses"></a>
This repository provides numerical realizations of stochastic processes, given by a superposition of pulses. For a given time $t \in [0,T]$ the process $\Phi_k(t)$ can be written as
$
\Phi_k(t) = \sum_{k=1}^{K(T)}A_k\phi\left(\frac{t-t_k}{\tau_\mathrm{d}}\right).
$
Here, the random variables are defined as follows: $K(T)$ stands for the number of pulses arriving in the time interval $[0,T]$, $A_k$ is the pulse amplitude, $t_k$ the pulse arrival time, $\phi$ the pulse shape and $\tau_\mathrm{d}$ for the duration time. In the default case, these parameters are chosen so that $\Phi_k(t)$ is a Filtered Poisson Process with exponential pulses, however all variables can be chosen freely. 