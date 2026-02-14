import numpy as np

def simulate_seir(
        parameters: list[float] | tuple[float], 
        init_conditions: list[float] | tuple[float], 
        days: int = 51
) -> tuple[np.ndarray]:
    """
    Simulates the progression of an SEIR (Susceptible, Exposed, Infected, Recovered) epidemiological model 
    over a given number of days based on provided parameters and initial conditions.

    Parameters
    ----------
    parameters : list or tuple of floats
        A sequence containing the following parameters:
        - beta : float
            The transmission rate, representing the likelihood of an exposed person becoming infected per 
            contact with a susceptible individual.
        - sigma : float
            The rate at which exposed individuals become infected.
        - gamma : float
            The rate at which infected individuals recover.

    init_conditions : list or tuple of floats
        A sequence containing the initial conditions for the simulation:
        - S0 : float
            The initial number of susceptible individuals.
        - E0 : float
            The initial number of exposed individuals.
        - I0 : float
            The initial number of infected individuals.
        - R0 : float
            The initial number of recovered individuals.

    days : int, optional, default: 51
        The number of days to simulate the SEIR model. 

    Returns
    -------
    tuple of numpy arrays
        A tuple containing four numpy arrays that represent the number of individuals in each compartment 
        (Susceptible, Exposed, Infected, Recovered) for each day:
        - S : numpy array of floats
            The number of susceptible individuals on each day.
        - E : numpy array of floats
            The number of exposed individuals on each day.
        - I : numpy array of floats
            The number of infected individuals on each day.
        - R : numpy array of floats
            The number of recovered individuals on each day.
    """



    # Extract parameters and initial conditions (Your code here)
    beta, sigma, gamma = parameters
    S0, E0, I0, R0 = init_conditions
    N = S0 + E0 + I0 + R0
    
       
    S = np.zeros(days)
    E = np.zeros(days)
    I = np.zeros(days)
    R = np.zeros(days)

    S[0] = S0
    E[0] = E0
    I[0] = I0
    R[0] = R0


    # For each day, perform SEIR update
    for t in range(1, days):

        # Compute new cases and update equations
        E_new = (beta*S[t-1]*I[t-1]) / N
        I_new = sigma*E[t-1]
        R_new = gamma*I[t-1]
      
        # Update equations
        S[t] = S[t-1] - E_new
        E[t] = E[t-1] + E_new - I_new
        I[t] = I[t-1] + I_new - R_new
        R[t] = R[t-1] + R_new

    return (S, E, I, R)
