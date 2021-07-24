## Project Overview:

### Objective:

I wish to collect the career stats of top picks from the past 20 NBA drafts. I will compare numerical stats among players in drafts using graphs and visualization techniques and will also explore interesting relationships among the scraped data with different visualization techniques.

### Tasks:

1. From www.basketball-reference.com/draft, scrape the rookie stats of the top 10 overall picks of last 20 NBA drafts (2001 - 2020)
2. Scrape data into a single Pandas MultiIndexDataFrame with outer index of draft year and inner index of pick number
3. Run DataFrame manipulations and various visualization techniques to gain insight into questions regarding drafting teams, picks, and player stats.

*** In this analysis, "Drafting teams" includes teams that trade for a pick. Drafting teams are teams that a rookie plays for for the entire season. Therefore, teams that trade or receive picks midway through the season will not be counted in this analysis.

### Here are some of the plots and realizations from the 6 visual analysis questions (Analysis 1 is a DataFrame manipulation):

##### Analysis 2: Of the top 5 teams with the most top-10 picks play for them their rookie season, which typically chose the rookies with the most career win shares?

![barplot](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/barplot.png)
##### Analysis 3: Have guards had increasing 3PT% in years closer to 2020 than 2001 due to the transition to a distance shooting era?

![jointplot](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/jointplot.png)
##### Analysis 4: Can we visualize clear groupings by position based on players' points, assists, and rebounding averages?

![plotly](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/3dscatterplot.png)
![lda](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/ldascatter.png)
##### Analysis 5: Is there a clear relationship between career box score plus minus or win shares with pick number?

![scatterplots](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/scatterplots.png)
![boxplots](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/boxplots.png)
##### Analysis 6: Are there differences in the rookie median minutes per game between positions among the top 6 drafting teams?

![barplot_grid](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/barplot_grid.png)


### Libraries Involved:
Requests, Beautiful Soup, NumPy, SciPy, Pandas, Matplotlib, Seaborn, Plotly, Scikit-learn
