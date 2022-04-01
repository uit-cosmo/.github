# Complex Systems Modelling - UiT 

`uit-cosmo` is a github organization providing numerical tools for creating, analyzing and visualizing data from complex systems. 

This guide is meant for students and employees of the complex systems modelling group at UiT. External collaborators or people with interest in the groups work are also welcome to use and contribute to the provided repositories. 

The latex expressions in this guide are created with [`readme2tex`](https://github.com/leegao/readme2tex). 

- [Repositories](#repos)
    - [`superposed-pulses`](#superposed-pulses)
    - [`2d-propagating-blobs`](#2d-propagating-blobs)
    - [`fpp-analysis-tools`](#fpp-analysis-tools)
    - [`fpp-closed-expressions`](#fpp-closed-expressions)
    - [`fpp-sle`](#fpp-sle)
    - [`cosmoplots`](#cosmoplots)
    - [`xblobs`](#xblobs)
    - [`Complexity-Entropy-Analysis`](#Complexity-Entropy-Analysis)
    - [`ebm`](#ebm)
    - [`SOFTX-D-16-00023`](#SOFTX-D-16-00023)
    - [`uit_sandpiles`](#uit_sandpiles)
    - [`PhD-thesis`](#PhD-thesis)

- [Publication specific repositories](#pub-repos)
    - [`dirac-comb-and-exponential-frequency-spectra-in-nonlinear-dynamics`](#dirac) 
- [Contributing to uit-cosmo ](#contributing)


## Repositories<a name="repos"></a>
### [`superposed-pulses`](https://github.com/uit-cosmo/superposed-pulses)<a name="superposed-pulses"></a>
This repository provides numerical realizations of stochastic processes, given by a superposition of pulses. For a given time <img src="svgs/8276c082cf9acef511891f138a922f74.svg?invert_in_darkmode" align=middle width=62.57408684999999pt height=24.65753399999998pt/> the process <img src="svgs/e92792f813c381b733318ac43a2728b7.svg?invert_in_darkmode" align=middle width=38.68165454999999pt height=24.65753399999998pt/> can be written as

<img src="svgs/98a5b4c5d09f47ace9e1894bbd96feab.svg?invert_in_darkmode" align=middle width=204.40029884999998pt height=37.80850590000001pt/>

Here, the random variables are defined as follows: <img src="svgs/10a4a3cc50840a98449846ec6934c3ee.svg?invert_in_darkmode" align=middle width=39.81174449999999pt height=24.65753399999998pt/> stands for the number of pulses arriving in the time interval <img src="svgs/aab0f08201b211261f795050337fa8df.svg?invert_in_darkmode" align=middle width=36.54685154999999pt height=24.65753399999998pt/>, <img src="svgs/1f0aa5770083d7bade7ac8aafcbfc008.svg?invert_in_darkmode" align=middle width=19.594827449999993pt height=22.465723500000017pt/> is the pulse amplitude, <img src="svgs/509bf7d4f0f63616580a39c4ed8b527d.svg?invert_in_darkmode" align=middle width=13.20212684999999pt height=20.221802699999984pt/> the pulse arrival time, <img src="svgs/f50853d41be7d55874e952eb0d80c53e.svg?invert_in_darkmode" align=middle width=9.794543549999991pt height=22.831056599999986pt/> the pulse shape and <img src="svgs/b222131e5e48239edd846762f39f9c93.svg?invert_in_darkmode" align=middle width=14.44641824999999pt height=14.15524440000002pt/> for the duration time. In the default case, these parameters are chosen so that <img src="svgs/e92792f813c381b733318ac43a2728b7.svg?invert_in_darkmode" align=middle width=38.68165454999999pt height=24.65753399999998pt/> is a Filtered Poisson Process with exponential pulses, however all variables can be chosen freely. See `superposed-pulses/mode/example.py` for further details. An example of a realization in the default case is shown below:

<img src="assets/fpp.png" alt="drawing" width="500"/>

### [`2d-propagating-blobs`](https://github.com/uit-cosmo/2d-propagating-blobs)<a name="2d-propagating-blobs"></a>

This repository can be regarded as an extension of superposed pulses by adding one or two spatial dimensions. The model is motivated by 2d propagating blobs in the scrape-off layer of fusion experiments, but can be used for any 1d or 2d system consisting of advecting pulses. An example is shown below.

Similarly to `superposed-pulses` all stochastic variables of the model can be chosen freely. The `README.md` file of the repository contains a documentation. Also the examples directory might be useful.
<img src="assets/2d_blobs.gif" alt="drawing" width="600"/>

### [`fpp-analysis-tools`](https://github.com/uit-cosmo/fpp-analysis-tools)<a name="fpp-analysis-tools"></a>
This repository provides a range of tools to analyze time series of intermittent fluctuations. Functions for the following tasks are provided:
- conditional averaging
- calculating correlation functions 
- deconvolution of Filtered Point Processes
- calculating distribution functions
- estimating Hurst exponents
- excess statistics 
- calculating running moments
- parameter estimation from the empirical characteristic function
- peak detection

This repository is meant as a centralized hub for functions and methods for time series analysis. Whenever you develop new methods for this purpose, we encourage you to add them to this repository to make them available for other group members. 
### [`fpp-closed-expressions`](https://github.com/uit-cosmo/fpp-closed-expressions) <a name ="fpp-closed-expressions"></a>
This repository is a collection of closed expressions for the most common functions related to shot noise processes such as expressions for PDFs, excess time statistics, PSDs and autocorrelation functions. Similarly to `fpp-analysis-tools` we encourage you to add newly derived expressions whenever you derive and/or publish any to make them available to other group members. 

### [`fpp-sle`](https://github.com/uit-cosmo/fpp-sle) <a name ="fpp-sle"></a>

This repository extends the [`superposed-pulses`](#superposed-pulses) repository by
implementing a forcing class that generates arrival times from varying rate processes.
How arrival times are generated from on the given rate function can be adjusted to the
users needs, but one implementation of the inhomogeneous Poisson process is provided.

In addition, different stochastic differential equations are provided, used when
comparing the statistics of the process created by the `superposed-pulses` library, when
used with the variable rate forcing this package provide.

### [`cosmoplots`](https://github.com/uit-cosmo/cosmoplots) <a name ="cosmoplots"></a>
`cosmoplots` provides default configurations for producing quality plots. We recommend using `cosmoplots` whenever you produce plots for manuscripts, talks or presentations. An example showing the advances of `complotots` compared to standard `matplotlib` is shown below. See the `README.md` file of the repository for a simple example.
| `matplotlib` | `cosmoplots` |
| :--------: | :--------: |
| ![matplotlib](./assets/matplotlib.png) | ![cosmoplots](./assets/cosmoplots.png) |
### [`xblobs`](https://github.com/uit-cosmo/xblobs)<a name ="xblobs"></a>
`xblobs` is a python tool to detect and analyse coherent structures in turbulence using xarray. The algorithm has been developed originally to detect and track coherent structures (blobs) in plasma turbulence simulations, but it can be applied on any 2D xarray Dataset with a Cartesian grid and constant spacing `dx`, `dy` and `dt`. Documentation is provided in the `README.md` file. An example is shown below:
![Density evolution](assets/turbulence_blobs.gif ) 

### [`Complexity-Entropy-Analysis`](https://github.com/uit-cosmo/Complexity-Entropy-Analysis)<a name ="Complexity-Entropy-Analysis"></a>
### [`ebm`](https://github.com/uit-cosmo/ebm)<a name ="ebm"></a>
A Julia script to solve the 1D-Energy Balance Equation on the Northern hemisphere, adapted from North et al. 

Options include:
- seasonal solar insolation
- time dependent albedo
- CO2-forcing
- noise
- historical forcing
- ensemble runs

### [`SOFTX-D-16-00023`](https://github.com/uit-cosmo/SOFTX-D-16-00023)<a name ="SOFTX-D-16-00023"></a>
### [`uit_sandpiles`](https://github.com/uit-cosmo/uit_sandpiles)<a name ="uit_sandpiles"></a>
Efficient C++ code that simulates sandpile models based on the Bak–Tang–Wiesenfeld and other well-known variants. These models display self-organized criticality, and study of the different time signals they produce serves as a training tool to analyze self oranized critial systems in nature.
### [`PhD-thesis`](https://github.com/uit-cosmo/PhD-thesis)<a name ="PhD-thesis "></a>
This repository contains the latex code of Gregor Decristoforo's PhD thesis. If you are looking for a latex template for your thesis at UiT this might be useful. A Makefile for compiling the latex code and instructions how to access the front page from the UiT website are provided. 

 ## Publication specific repositories<a name="pub-repos"></a>
### [`dirac-comb-and-exponential-frequency-spectra-in-nonlinear-dynamics`](https://github.com/uit-cosmo/dirac-comb-and-exponential-frequency-spectra-in-nonlinear-dynamics)<a name="dirac"></a>
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
