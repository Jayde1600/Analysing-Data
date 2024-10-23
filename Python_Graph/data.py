import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.float_format = '{:,.0f}'.format

spotify_data = pd.read_csv('Spotify_Most_Streamed_Songs.csv')

spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')
cleaned_data = spotify_data.dropna(subset=['streams'])

# Removing duplicates if any
cleaned_data = cleaned_data.drop_duplicates()

# Sort the data by 'streams'
top_10_songs = cleaned_data.sort_values(by='streams', ascending=False).head(10)

print("Top 10 Most Streamed Songs on Spotify:")
print(top_10_songs[['track_name', 'streams']])

plt.figure(figsize=(12, 6))

# Bar plot for the top 10 songs based on streams with full numbers on x-axis
sns.barplot(y=top_10_songs['track_name'], x=top_10_songs['streams'], palette='Blues_d', hue=top_10_songs['track_name'], dodge=False)
plt.title('Top 10 Most Streamed Songs on Spotify')
plt.xlabel('Streams')
plt.ylabel('Track Name')

plt.legend([], [], frameon=False)

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.tight_layout()
plt.show()
