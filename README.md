**Report: Analysis of Spotify's Most Streamed Songs**

This report presents the analysis of the most streamed songs on Spotify, including the Python code used for:
- data handling
- cleaning
- exploration
- visualization along with explanations and interpretations of the results.

**Data Handling**
Code Snippet:
spotify_data = pd.read_csv('Spotify_Most_Streamed_Songs.csv')

cleaned_data = cleaned_data.drop_duplicates()

The dataset containing Spotify's most streamed songs is loaded into a pandas DataFrame. The dataset is now ready for further cleaning and exploration


**Data Exploration**
Code Snippet:

spotify_data['streams'] = pd.to_numeric(spotify_data['streams'], errors='coerce')
cleaned_data = spotify_data.dropna(subset=['streams'])

I ensured that the streams column is in numeric format, converting any invalid entries into NaN values using pd.to_numeric. 
The rows with missing stream data were dropped using dropna, as incomplete data would affect the accuracy of the analysis.

All rows with missing or invalid stream data have been removed, leaving clean and valid data for further analysis.
