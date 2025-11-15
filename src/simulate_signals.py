# We will use autoregressive model -> xt​=ϕxt−1​+ϵt​ where the current value depends on the previous value multipled with a 
# coefficient controlling how strongly the past influences the present plus some noise.

import numpy as np 
import pandas as pd

def simulate_ar_rois(
        length=300, 
        pi=0.6, 
        gamma=0.3, 
        beta=0.8, 
        sigma=0.3, 
        seed=42):
    """
    Simulate 3 autoregressive (AR) signalS of given length 300 time steps choosen by default.

    Parameters:
    length (int): Length of the signal to be generated.
    phi (float): Autoregressive coefficient.
    gamma (float): The strength of the shared global drive (common fluctuation added to all ROIs).
    sigma (float): Standard deviation of the noise.
    seed (int, optional): Random seed for reproducibility.

    Returns:
    simulated_ar_rois: Simulated AR ROI signals.
    """

    rng=np.random.default_rng(seed) # ensuring reproducibility

    g=np.zeros(length)
    
    for t in range(1,length):
        g[t]=gamma*g[t-1]+rng.normal(scale=0.5) #global drive
    
    direct_coupling = np.array([[0, 0, 0],
                                [0.6, 0, 0], # ROI 2 influenced by ROI1
                                [0, 0, 0]])
    
    x = np.zeros((length, 3)) # 3 ROIs

    eps = rng.normal(scale=sigma, size=(length, 3)) # noise

    for t in range(1, length):
        autoregressive_term = pi * x[t-1]
        coupling_term = x[t-1] @ direct_coupling.T
        shared_drive = beta * g[t]
        x[t] = autoregressive_term + coupling_term + shared_drive + eps[t]

    x=(x-x.mean(axis=0))/x.std(axis=0, ddof=1) # z-score normalization
    return x

if __name__ == "__main__":
    x = simulate_ar_rois()
    df = pd.DataFrame(x, columns=['ROI_1', 'ROI_2', 'ROI_3'])
    df.to_csv('data/simulated_ar_rois.csv', index=False)
    print("Simulated AR ROI signals saved to 'data/simulated_ar_rois.csv'")
    print(df.head())