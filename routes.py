import scraping
from main import app

@app.get('/')
def getAllProcurados():
  return scraping.getAllProcurados()