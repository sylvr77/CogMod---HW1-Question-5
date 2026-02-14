import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np


def plot_results(
        infected: np.ndarray
) -> Figure:
    """Plots the time series of infected cases.

    Parameters
    ----------
    infected : numpy array of floats
        The number of people that are infected as a float.

        
    Returns
    -------
    matplot figure class instance

    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.plot(infected, color='#AA0000', linestyle='dashed', marker='o')
    ax.set_xlabel('Day', fontsize=16)
    ax.set_ylabel('Number of Infected Cases', fontsize=16)
    ax.set_title('Simulated Oubreak', fontsize=20)
    ax.grid(alpha=0.2)
    return fig
