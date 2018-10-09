## Sam's review of the null and alternative hypotheses:

The null (H<sub>0</sub>) and alternative (H<sub>1</sub>) hypotheses statements are correct.

## Sam's review of the data processing:

The original dataframe was appropriately and efficiently narrowed for the purposes of this analysis. Rohun's decision to keep only the gender and start time columns (and then to keep only the hour from the start time) was the right choice for comparing differences in time of day when rides are taken by men and women.

The bar charts Rohun plotted, especially the chart overlaying the male and female ridership, were very effective at presenting the hourly trends in ridership. The normalized plot of the difference in ridership helps to highlight gender differences that could otherwise be overshadowed by a plot of absolute values only. 

But the normalized plot also must be viewed in the context of the plot of total rides in absolute values. By looking at only the normalized plot, one might conclude that there are vast differences in total rides late at night and early in the morning. The plot of total rides helps remind us that the difference between genders in late night/early morning rides, although large in terms of percentages, is still quite small in absolute terms when comparing the total to rides taken during rush hour and the middle of the day. An additional plot that incorporated the difference in ridership each hour both as a percentage and in absolute terms might have been beneficial to this analysis.

For this analysis, a Mann-Whitney U test should be performed because we have 2 groups of unpaired data (there is no overlap between the two samples of male and female CitiBike riders) and we do not know if the data is distributed normally (the data may be nonparametric).
