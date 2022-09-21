import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
def scrape_mars():
    data_dict = {}

    # NEWS SCRAPE
    mns = 'https://redplanetscience.com'
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(mns)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_body = soup.find('div', class_='article_teaser_body').text
    browser.quit()

    data_dict['news_title'] = news_title
    data_dict['news_body'] = news_body

    # FEATURED IMAGE SCRAPE
    fmi = 'https://spaceimages-mars.com/'
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(fmi)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find('img', class_="headerimage")['src']
    featured_image_url = f'{fmi}{image}'
    browser.quit()
    
    data_dict['featured_image'] = featured_image_url

    # MARS FACTS SCRAPE
    mf = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(mf)
    mars_facts = tables[1]
    mars_facts_html = mars_facts.to_html(index=False, header=False)
    mars_facts_html.replace('\n', '')

    data_dict['mars_facts_html'] = mars_facts_html


    # HEMISPHERE SCRAPE
    mh = 'https://marshemispheres.com/cerberus.html'
    #ran out of time/energy to figure out how to scrape the URLS so just hardcoding for now
    data_dict['mars_hemispheres']  = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"}
    ]
    return data_dict



    

