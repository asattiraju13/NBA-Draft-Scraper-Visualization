# Main imports

import pandas as pd

import requests
from bs4 import BeautifulSoup

# Initialize dictionary and lists to be used in scraper

player_data = {'team_id':[],'pos':[],'player':[],'mp_per_g':[],'efg_pct':[],
               'pts_per_g':[],'trb_per_g':[],'ast_per_g':[],'ws':[],'bpm':[]}   # Columns for DataFrame

index_array = [[],[]]  # Used for MultiIndex

positions = ['Point Guard','Shooting Guard','Small Forward','Power Forward','Center'] # Used to scrape Positions

def get_doc(url):   # return BeautifulSoup parsed document
    response = requests.get(url)
    response.close()
    soup = BeautifulSoup(response.text,'html.parser')
    return soup


def scrape_draft(doc,year): # Scrape players' data for single draft
    tr_tags = doc.findAll('tr')
    for pick in range(2,12,1):
        get_advanced_stats(tr_tags, pick)  # Scrape certain stats from main draft page
        player_url = "https://www.basketball-reference.com" + tr_tags[pick].find('td',{'data-stat':'player'}).a['href']
        get_player_data(get_doc(player_url))  # Scrape stats from individual player pages
        index_array[0].append(year)
        index_array[1].append(pick - 1)
        
        
def get_advanced_stats(tags, pick):  # Scrape player's career advanced stats from the draft page
    for key in ['ws','bpm','player']:
        field = tags[pick].find('td',{'data-stat': key})
        if field is not None:
            player_data[key].append(field.text)
        else:
            player_data[key].append(np.NaN)

    
def get_player_data(doc):  # Scraper player's rookie season data off of individual page
    rookie_stats = doc.findAll('tr',{'class':'full_table'})[0]
    for key in player_data:
        if key not in ['pos','ws','bpm','player']:
            field = rookie_stats.find('td',{'data-stat': key})
            if field is not None:
                player_data[key].append(field.text) # Append values to dictionary
            else:
                player_data[key].append(np.NaN)   # Appends missing values dictionary if no data to scrape
    get_player_pos(doc)
    
        
def get_player_pos(doc):  # Scrape player positions
    test_sections = [doc.findAll('p')[i].text.strip() for i in range(1,5,1)]  # Possible lines with position titles
    test_string = ""
    for section in test_sections:
        test_string += section  
    pos = [pos for pos in positions if pos in test_string]  
    player_data['pos'].append(pos) # Appends list of positions on website to dictionary
    
    
def draft_scraper(start_year,end_year):   # Entire web scraper function
    for year in range(start_year, end_year + 1, 1):  # Iterates through all draft years
        draft_url = 'https://www.basketball-reference.com/draft/NBA_' + str(year) + '.html'
        scrape_draft(get_doc(draft_url),year)
 
 	# Form MultiIndex
    index_tuples = list(zip(*index_array))   
    index = pd.MultiIndex.from_tuples(index_tuples, names=["year", "pick"])  # Create a Pandas MultiIndex

    return pd.DataFrame(player_data,index=index)  # Returns DataFrame version of player_data dictionary

if __name__ == '__main__':
	draft_scraper(2001,2020).to_csv("2001_2020_drafts.csv")  # Writes to .csv file