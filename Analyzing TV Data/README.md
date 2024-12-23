## Task 1

Import `pandas` then load the data.

- Read the notebook on the right before the instructions here on the left.

- Import `pandas` under the alias `pd`.

Load the dataset's CSV files (`'datasets/super_bowls.csv'`, `'datasets/tv.csv'`, and `'datasets/halftime_musicians.csv'`) into DataFrames.

## Task 2

Display and inspect the summaries of the TV and halftime musician DataFrames for issues.

- Use the `.info()` method to inspect the DataFrame `tv`.

- Use the `.info()` method to inspect the DataFrame `halftime_musicians`.

## Task 3

Plot a histogram of combined points then display the rows with the most extreme combined point outcomes.

- From `matplotlib`, import the `pyplot` module under the alias `plt`.

- Create a histogram of the `combined_pts` column from the `super_bowls` DataFrame.

- Select the Super Bowl(s) where the combined score was less than 25.

## Task 4

Modify and display the histogram of point differences, then display the rows with the most extreme point difference outcomes.

- Add a y-label with `'Number of Super Bowls'`.

- Display the plot with `plt.show()`.

- Select the Super Bowl(s) where the point difference was equal to 1.

- Select the Super Bowl(s) where the point difference was greater than or equal to 35.

## Task 5

Import seaborn and plot household share vs. point difference.

- Import the `seaborn` module under the alias `sns`.

- Fill in the `x` argument of `sns.regplot()` with the point difference column

- Fill in the `y` argument of `sns.regplot()` with the household share column.

## Task 6

Create three line plots using the `tv` DataFrame to compare viewers, rating, and ad cost.

- For the first plot, plot `super_bowl` on the x-axis, `avg_us_viewers` on the y-axis, and set the line color to `'#648FFF'`.

- For the second plot, plot `super_bowl` on the x-axis, `rating_household` on the y-axis, and set the line color to `'#DC267F'`.

- For the third plot, plot `super_bowl` on the x-axis, `ad_cost` on the y-axis, and set the line color to `'#FFB000'`.

## Task 7

Filter and display the musicians for halftime shows up to and including Super Bowl XXVII.

- Using `halftime_musicians`, select the musicians that performed in halftime shows up to and including Super Bowl XXVII (27) (i.e. Michael Jackson's performance).

## Task 8

Select and display the musicians with more than one halftime show appearance.

- The new `halftime_appearances` DataFrame has two columns, `musician` and `super_bowl`, where `super_bowl` now contains the halftime show counts for each musician. Select the musicians that have appeared in more than one halftime show.

## Task 9

Modify the histogram of number of songs performed for non-band musicians.

- In the `plt.hist()` function, set the number of bins argument equal to `most_songs` (the most number of songs performed in a halftime show by a single musician).

- Add an x-label with `'Number of Songs Per Halftime Show Performance'`.

## Task 10

Who will win Super Bowl LIII?

- The `patriots` and `rams` are playing in Super Bowl LIII. Assign the variable of the team you think will win to the `super_bowl_LIII_winner` variable.