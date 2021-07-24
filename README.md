## Project Overview:

### Objective:

I wish to collect the career stats of top picks from the past 20 NBA drafts. I will compare numerical stats among players in drafts using graphs and visualization techniques and will also explore interesting relationships among the scraped data with different visualization techniques.

### Tasks:

1. From www.basketball-reference.com/draft, scrape the rookie stats of the top 10 overall picks of last 20 NBA drafts (2001 - 2020)
2. Scrape data into a single Pandas MultiIndexDataFrame with outer index of draft year and inner index of pick number
3. Run DataFrame manipulations and various visualization techniques to gain insight into questions regarding drafting teams, picks, and player stats.

*** In this analysis, "Drafting teams" includes teams that trade for a pick. Drafting teams are teams that a rookie plays for for the entire season. Therefore, teams that trade or receive picks midway through the season will not be counted in this analysis.

### Here are some of the plots and realizations from the 6 visual analysis questions (Analysis 1 is a DataFrame manipulation):

#### Analysis 2: Of the top 5 teams with the most top-10 picks play for them their rookie season, which typically chose the rookies with the most career win shares?

As we can see from this plot, we see that the Golden State Warriors and the Chicago Bulls typically chose the rookies with the most career win shares in the past 20 years. This could partly be attributed to the teams' player developmental and training staff, and/or their position in the drafts, being able to choose a clear star talent. However, these numbers may not always reflect well on these teams as certain players could have possibly gotten traded earlier on in their careers.
      
![barplot](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/barplot.png)
#### Analysis 3: Have guards had increasing 3PT% in years closer to 2020 than 2001 due to the transition to a distance shooting era?

This scatterplot shows no clear correlation at all between the draft year and the guards' rookie 3-point percentage. One would think that there would be a positive correlation between these two variables since that in recent years, the league has transitioned to an era dominated by the 3-point shot. Therefore, it follows that incoming point guards may have focused more on their outside jumper and thus had an overall better 3-point percentage than rookie guards several years before. 

However, as displayed here, this is not the case. Possibly, a more clear positive correlation could be between year and the number of attempts per game. This would better echo the transition to a 3-point era, as guards would be taking more shots, but not necessarily shooting a better percentage.
        
![jointplot](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/jointplot.png)
#### Analysis 4: Can we visualize clear groupings by position based on players' points, assists, and rebounding averages?

![plotly](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/3dscatterplot.png)
![lda](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/ldascatter.png)
#### Analysis 5: Is there a clear relationship between career box score plus minus or win shares with pick number?

![scatterplots](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/scatterplots.png)
![boxplots](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/boxplots.png)
#### Analysis 6: Are there differences in the rookie median minutes per game between positions among the top 6 drafting teams?

![barplot_grid](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/barplot_grid.png)


### Libraries Involved:
Requests, Beautiful Soup, NumPy, SciPy, Pandas, Matplotlib, Seaborn, Plotly, Scikit-learn
