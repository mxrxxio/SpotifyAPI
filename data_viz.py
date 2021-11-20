import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requestsfunctions as rf

def valenceAccoustic(data):
    df = pd.DataFrame(data)
    df['release_date'] = pd.to_datetime(df['release_date'])
    df = df.sort_values(by='release_date')
    df = df.query('short_album_name != "The Song Remains The Same"')
    df = df[~df['track_name'].str.contains('Live|Mix|Track')]
    plt.figure(figsize=(10,10))

    ax = sns.scatterplot(data=df, x='valence', y='acousticness', 
                     hue='short_album_name', palette='rainbow', 
                     size='duration_ms', sizes=(50,1000), 
                     alpha=0.7)

    h,labs = ax.get_legend_handles_labels()
    ax.legend(h[1:10], labs[1:10], loc='best', title=None)
    plt.show()