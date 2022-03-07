# Complex Systems Modelling - UiT 

`uit-cosmo` is a github organization providing numerical tools for creating, analyzing and visualizing data from complex systems. 

This guide is meant for students and employees of the complex systems modelling group at UiT. External collaborators or people with interest in the groups work are also welcome to use and contribute to the provided repositories. 


- [Repositories](#repos)
    - [superposed-pulses](#superposed-pulses)
    - [2d-propagating-blobs ](#2d-propagating-blobs)
    - [fpp-analysis-tools](#fpp-analysis-tools)
    - [fpp-closed-expressions ](#fpp-closed-expressions)
    - [cosmoplots](#cosmoplots)
    - [xblobs](#xblobs)
    - [Complexity-Entropy-Analysis](#Complexity-Entropy-Analysis)
    - [ebm](#ebm)
    - [SOFTX-D-16-00023](#SOFTX-D-16-00023)
    - [uit_sandpiles](#uit_sandpiles)
    - [PhD-thesis](#PhD-thesis)

- [Publication specific repositories](#pub-repos)
    - [dirac-comb-and-exponential-frequency-spectra-in-nonlinear-dynamics](#dirac) 
- [Contributing to uit-cosmo ](#contributing)


## Repositories<a name="repos"></a>
### superposed-pulses<a name="superposed-pulses"></a>
This repository provides numerical realizations of stochastic processes, given by a superposition of pulses. For a given time $t \in [0,T]$ the process $\Phi_k(t)$ can be written as

$\Phi_k(t) = \Sigma_{k=1}^{K(T)}A_k\phi(\frac{t-t_k}{\tau_\mathrm{d}})$.

Here, the random variables are defined as follows: $K(T)$ stands for the number of pulses arriving in the time interval $[0,T]$, $A_k$ is the pulse amplitude, $t_k$ the pulse arrival time, $\phi$ the pulse shape and $\tau_\mathrm{d}$ for the duration time. In the default case, these parameters are chosen so that $\Phi_k(t)$ is a Filtered Poisson Process with exponential pulses, however all variables can be chosen freely. See `superposed-pulses/mode/example.py` for further details.

### 2d-propagating-blobs<a name="2d-propagating-blobs"></a>

This repository can be regarded as an extension of superposed pulses by adding one or two spatial dimensions. The model is motivated by 2d propagating blobs in the scrape-off layer of fusion experiments, but can be used for any 1d or 2d system consisting of advecting pulses. An example is shown below:

![Density evolution](readme_gifs/2d_blobs.gif ) 

### fpp-analysis-tools<a name="fpp-analysis-tools"></a>
### fpp-closed-expressions <a name ="fpp-closed-expressions"></a>
### cosmoplots <a name ="cosmoplots"></a>
### xblobs<a name ="xblobs"></a>
### Complexity-Entropy-Analysis<a name ="Complexity-Entropy-Analysis"></a>
### ebm<a name ="ebm"></a>
### SOFTX-D-16-00023<a name ="SOFTX-D-16-00023"></a>
### uit_sandpiles<a name ="uit_sandpiles"></a>
### PhD-thesis<a name ="PhD-thesis "></a>


 ## Publication specific repositories<a name="pub-repos"></a>
### dirac-comb-and-exponential-frequency-spectra-in-nonlinear-dynamics<a name="dirac"></a>
Repository containing scripts to generate and plot data used in Manuscript "Dirac comb and exponential frequency spectra in nonlinear dynamics" (arXiv:2106.15904).

 ## Contributing to uit-cosmo<a name="contributing"></a>
Contributions of any kind are welcome!

The workflow used is essentially ["GitHub flow"](https://docs.github.com/en/get-started/quickstart/github-flow). The **main** branches of most repositories are protected from direct commits. Instead, do the following:
1. Create a new feature branch
2. (Optional) Push feature branch to Github to share and create backup
3. Commit changes to the feature branch
4. Submit pull request into **main** branch 

For new repositories, please provide a license (we recommend MIT) and a useful README file containing installation instructions and a simple example. Make sure that your code contains useful documentation (docstrings, examples, etc.).

## TODO list:
- [ ] unify naming conventions across repositories
- [ ] unify documentation across repositories
- [ ] provide tests for all repositories
