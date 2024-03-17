import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.billboard.com/charts/hot-100'
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Find the list of songs
song_list = soup.find('div',class_='chart-result-list')
songs_container=soup.find('div', class_='chart-results-list')
songs=songs_container.find_all('div', class_='o-chart-results-list-row-container')

# Extract rank, song title, and singer
for i in range(50):
    song=songs[i]
    song_name=song.find('h3',class_='c-title').text.strip()
    artists = song.find('li', class_='lrv-u-width-100p')
    artist_name = artists.find('span', class_='c-label').text.strip()

    print(f"{i+1} / {song_name} // {artist_name}")