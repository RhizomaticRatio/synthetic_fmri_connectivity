import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyse_partial_corr(data):
    """
    Compute partial correlation matrix for the given DataFrame.

    Parameters:
    data (pd.DataFrame): Input DataFrame. (T X N Matrix where T is time points and N is ROIs)

    Returns:
    pd.DataFrame: Partial correlation matrix.
    """

    cov_matrix = np.cov(data, rowvar=False)
    precision_matrix = np.linalg.inv(cov_matrix)

    d = np.sqrt(np.diag(precision_matrix))
    partial_corr_matrix = -precision_matrix / np.outer(d, d)
    np.fill_diagonal(partial_corr_matrix, 1.0)

    return partial_corr_matrix

if __name__ == "__main__":
    df = pd.read_csv('data/simulated_ar_rois.csv')
    x = df.values

    correlation_matrix = np.corrcoef(x, rowvar=False)
    partial_corr_matrix = analyse_partial_corr(x)
    roi_labels = ["ROI_1", "ROI_2", "ROI_3"]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', xticklabels=roi_labels, yticklabels=roi_labels)
    plt.title('Correlation Matrix')

    plt.subplot(1, 2, 2)
    sns.heatmap(partial_corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', xticklabels=roi_labels, yticklabels=roi_labels )
    plt.title('Partial Correlation Matrix')

    plt.tight_layout()
    plt.savefig("figures/connectivity_matrices.png")
    print("Connectivity matrices saved to figures/connectivity_matrices.png")