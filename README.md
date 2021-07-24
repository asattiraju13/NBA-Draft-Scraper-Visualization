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

To view this interactive plot, please download the raw plot file [here](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/3dscatter.html) as an HTML file, which you can select to display in your browser.

The interactive plot (static version shown below) illustrates some of the differences between the the three main basketball position categories - guards, wings, and big-men - as it is it relatively easy to see three different groupings. The grouping of Big-Men has is located higher up on the trb_per_g axis than the others because they logically average more rebounds per game than other positions due to their height. The grouping of Guards is located farther out on the ast_per_g axis than the others because they are more responsible for distributing the ball to others, generating more assists than other positions. Notice that there is no clear grouping along the pts_per_g axis, as all three positions can score the ball depending on which position a certain team and offense emphasizes.
      
![plotly](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/3dscatterplot.png)
   
From the explained variance ratio, the X axis of the below plot explains 0.96% of the variance in the data; we could expect that the RPG and APG features are included in this axis as these features relatively clearly separated the position groupings on the interactive plot above.

This plot of Linear Discriminant Analysis with respect to the three position groupings listed on the graph attempt to plot the data points - which incorporated the features of PPG, RPG, and APG - along 2 axes to maximize separation between the position labels. As we can see, there are clear groupings of the Guard and Big Men categories and a less clear grouping of the Wing category, as it overlaps both of the others towards the edges.
    
![lda](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/ldascatter.png)
#### Analysis 5: Is there a clear relationship between career box score plus minus or win shares with pick number?
   
![scatterplots](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/scatterplots.png)

   
These two graphs above both show that there is a negative correlation both for average career win shares vs pick number and average career box plus minus vs pick number. The correlation coefficient for both graphs is roughly $\sqrt{0.55}$ = 0.74, which illustrates a moderate correlation as supported by the graphs. One would expect these relationships, as lower pick numbers are typically the better players and will have more success during their entire career. Let's look more closely at the ranges of win shares and Box Plus-Minus vs pick number below using boxplots in Seaborn.
   
![boxplots](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/boxplots.png)
    
These boxplot graphs show some support for the conclusion established from the scatterplot graphs, as the median win shares and box-plus minus of the top picks (smaller number picks) are on mostly higher than the median win shares and box-plus minus of the lower picks (higher number picks). However, these graphs best illustrate moderate correlation, since there are some aberrations in the trend. This is illustrated by median win shares and box-plus minus of the number two pick in particular, which are much lower than expected. Such an aberration with a top pick could possibly indicate a greater likelihood of number 2 picks not living up to star potential, becoming "busts" in their career.
    
#### Analysis 6: Are there differences in the rookie median minutes per game between positions among the top 6 drafting teams?

![barplot_grid](https://github.com/asattiraju13/NBA-Draft-Scraper-Visualization/blob/main/plots/barplot_grid.png)
  
This visualization is quite interesting, as it offers some insight into how different top-drafting teams value the players they drafted differently based on position. This could be due to a number of factors, such as the growth of another "veteran" player on the team, thus limiting a rookie's minutes, or the need to fill a void left by a star player's departure from the team, thus increasing a rookie's minutes. There are several reasons, each unique to the drafting team's circumstances. Of course, this could also depend upon the rookie's success throughout the season, which translates to the number of minutes played. 

From this barplot grid, we can see that Chicago, Cleveland, and Golden State have favored rookie guards and forwards in terms of minutes in the past 20 draft years. This makes sense, as Chicago drafted former MVP Derrick Rose, Cleveland drafted star Kyrie Irving, and Golden State drafted former MVP Stephen Curry. We also see that the minute distribution per position for Phoenix and Sacramento are fairly uniform, with rookie guards / forwards and centers having the most minutes in both cities. Minnesota seems to have favored centers more, drafting big-men such as star Karl Anthony-Towns. We could also propose explanations for the lack of minutes of some positions, making this visualization extremely versatile.


### Libraries Involved:
Requests, Beautiful Soup, NumPy, SciPy, Pandas, Matplotlib, Seaborn, Plotly, Scikit-learn
