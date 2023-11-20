# Project Name : Spotify Music Recommendation
  
<p align="center">
    <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*GMikfjbGYyPGDTYdJuMwhg.png" alt="Logo" width="400" height="300">
</p>

## Introduction

The Music Recommendation project aims to recommend movies to users. This is a content-based recommendation system.


## Dataset
- https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

## Methodology

The following methodology was used to accomplish the project objectives:

1. **Data Loading:** The movie data was loaded from the CSV file into the Pandas dataframe. 


2. **Data Cleaning and Pre-processing:** The data cleaning process encompassed eliminating irrelevant data, addressing missing values, standardizing formats, removing duplicates, and applied NLP techniques like removing stopwords, punctuations, stemming to make the data useful for creating the vectorization matrix.

3. **Streamlit App:** A web-based app was built using Streamlit and python 

![Sample_User_interface](https://drive.google.com/uc?export=download&id=16MKcV3ocDpu6zv78LBbAg_OeXyiaZrEk)


 <p>&nbsp;</p>


## Results

- 5 recommended music similar to the movie you searched for.


## Limitations:
   
- One limitation of this project is the size of the data, it might vary for a large dataset. This limitation can impact the ability to identify long-term trends and patterns accurately.
-  This is a content-based system so no involvement of users

## Challenges: 
   
- The challenge was to learn about NLP and which techniques to use to make the recommendation
- Learning about Spotipy library rather than making the API call directly which involved generating User Authentication tokens


## References

- NLTK from  https://www.nltk.org/
- pandas from https://pandas.pydata.org/docs/
- Spotipy from https://spotipy.readthedocs.io/en/2.22.1/


 
