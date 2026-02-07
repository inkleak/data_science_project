import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture             # Importing necessary libraries
from sklearn.decomposition import PCA

def gauss_cluster(X):
    save_results_to = 'C:/Projects/project_a/graphs/important/'

    X_np = X.to_numpy()
    feature_names = X.columns

    gmm = GaussianMixture(
        n_components=5, 
        covariance_type='full', 
        random_state=0)
    gmm.fit(X_np)
    labels = gmm.predict(X_np) # Hard clusters
    probs = gmm.predict_proba(X_np) # Soft clusters
    means = gmm.means_ #Table of means as discovered by the GMM.

    print(X_np.shape)

    aic = gmm.aic(X_np) #Aikaike Information Criterion, looks at model quality
    bic = gmm.bic(X_np) #Bayesian information criterion

    print(f"AIC: {aic:.2f}")
    print(f"BIC: {bic:.2f}")

    if X_np.shape[1] > 2:
        pca = PCA(n_components=2)
        X_proj = pca.fit_transform(X_np) # This transforms the shape of the DataFrame from (580, 30) to (580, 2).
        x_label = "PC1 (largest variance)"
        y_label = "PC2 (second largest variance)"
        means_proj = pca.transform(means)
    else:
        X_proj = X_np
        means_proj = means
        x_label = feature_names[0] #For general data sets, if there are already only two components then it is left untouched.
        y_label = feature_names[1]

    plt.scatter(X_proj[:,0], X_proj[:,1],c=labels, s=20, cmap='viridis') #Plotting as a scatter plot

    # Plot centroids
    plt.scatter(means_proj[:,0], means_proj[:,1],  s=200, c='red', marker="X", label='Centroids') #Plots centroids of clusters

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title("GMM Clustering (5 components)")
    plt.legend()
    plt.savefig(save_results_to + "gmm_clustering.png", dpi=300) # Saving the figiure


def components_finding(data):
    K = range(1,20)
    bics = []
    aics = []

    for k in K:
        gmm = GaussianMixture(
            n_components=k,
            covariance_type="full",     #Iterates AICs and BICs for each value of k. The aim here is to find the one that minimises BIC.
            random_state = 0
        )
        gmm.fit(data)
        bics.append(gmm.bic(data))
        aics.append(gmm.aic(data)) #Adds to lists
    print(aics)
    print(bics)


#Data Loading and Selecting only Numerical Values for Cluster Analysis

df = pd.read_csv('data/raw/premier-player-23-24.csv') # Loading data set
df_clean = df.select_dtypes(include = 'number')

#components_finding(df_clean), Determines the optimal value to set n_components to. The answer is 5.
gauss_cluster(df_clean) 
