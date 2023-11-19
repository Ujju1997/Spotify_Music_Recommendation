
import streamlit as st
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


cid = "e01282b2f4404d24934cf5518c6e7caa"
secret = "c8d2e9e0bb4242f4af24232bcdb78fbd"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


songs = pickle.load(open('songs.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def get_poster_cover(artist_name, song_name):
    query = f"artist:{artist_name} track:{song_name}"
    results = sp.search(q = query, type = 'track', limit =1)
    #name = results['tracks']['items'][0]['name']
    try:
        image_url = results['tracks']['items'][0]['album']['images'][0]['url']
    except:
        image_url = "https://i.postimg.cc/0QNXYz4V/social.png"
    #print(name)
    return image_url

def get_song_link(artist_name, song_name):
    query = f"artist:{artist_name} track:{song_name}"
    results = sp.search(q = query, type = 'track', limit = 1)
    try:
        link = results['tracks']['items'][0]['external_urls']['spotify']
        return link
    except:
        return "no link found"

def recommend(song):
    song_index = songs[songs.song == song].index[0]
    song_list = sorted(enumerate(similarity[song_index]), reverse = True, key = lambda x: x[1])[1:6]
    recommended_songs_list = []
    song_poster_list = []
    hyperlinks = []
    for i in song_list:
        artist_name = songs.iloc[i[0]]['artist']
#         print(artist_name)
        song_name = songs.iloc[i[0]]['song']
        recommended_songs_list.append(song_name)
        image_poster = get_poster_cover(artist_name, song_name)
#         print(image_poster)
        song_poster_list.append(image_poster)
        hyperlink = get_song_link(artist_name, song_name)
        hyperlinks.append(hyperlink)

    return recommended_songs_list, song_poster_list, hyperlinks


# print(recommend('Chiquitita'))

st.title('Spotify Music Recommendation')
# url = "https://www.streamlit.io"
# st.write( 'check out' ,'%s' % url)

selected_song = st.selectbox(
   "How would you like to be contacted?",
   songs['song'],
   index=None,
   placeholder="Select a song",
)
if st.button('Recommend'): 
    recommended_songs_list, song_poster_list, hyperlinks = recommend(selected_song)
    # st.write('You selected:', hyperlinks)

    col1, col2, col3, col4, col5 = st.columns(5)
    column_list = [col1, col2, col3, col4, col5]
    for i in range(5):
        with column_list[i]:
            st.image(song_poster_list[i])
            st.write(recommended_songs_list[i])
            if hyperlinks[i] != 'no link found':
                st.write("[link](%s)" % hyperlinks[i])
            else:
                st.write('no link found')
        
    