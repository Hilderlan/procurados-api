import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.novo.justica.gov.br/procurados/capa_interna')

if req.status_code == 200:
  print('Success!')
  content = req.content
else:
  print('Error!')

  # Using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
procurados_aux = soup.find(id='content-core')

procurados = procurados_aux.find_all('div', class_='photoAlbumEntry')

dict = {}
data = []

for procurado in procurados:
  aux = procurado.find('a').find('span', class_='photoAlbumEntryWrapper')

  name = aux.find('img')['title']
  nick = procurado.find('a').find('span', class_='photoAlbumEntryTitle').text
  photo = aux.find('img')['data-src']

  data.append({
    'name': name,
    'nick': nick,
    'photo': photo
  })

dict['data'] = data

print(dict)