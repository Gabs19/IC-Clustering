import os

from sklearn.metrics import silhouette_score #metrica para medir o desempenho do algoritmo em clusterização
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

#from kmodes.kmodes import Kmodes
# from scipy.spatial.distance import cdist
# from yellowbrick.cluster import silhouette_visualizer

from settings import PATH, DATABASE_PATH

def read_database(csv):

    df = pd.read_csv(os.path.join(DATABASE_PATH, csv))
    df.head()
    study_name = df.studyName
    sample_number = df.Species
    region = df.Region
    island = df.Island
    stage = df.Stage


    plot = sns.violinplot(x=region, y=island)
    plot_swarm = sns.swarmplot(x=region, y=island, color="k", alpha=0.8)

    plt.show



read_database("penguins_lter.csv")