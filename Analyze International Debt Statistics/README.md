Write SQL queries to answer the following:

- What is the number of distinct countries present in the database? The output should be single column aliased with the following name: `total_distinct_countries`.

- What are the distinct debt indicators? the output column should be aliased as `distinct_debt_indicators` and the outputs should be ordered by it.

- What is the total amount of debt owed by all the countries present in the table, in millions? The output should be single column aliased with the following name: `total_debt`.

- What country has the highest amount of debt?

- What is the average amount of debt across different debt indicators?

- What is the highest amount of principal repayments in the "DT.AMT.DLXF.CD" category?

Six SQL cells have been created for you in the Workspace. To access the database, you will need to select data using the syntax `FROM international_debt`.

Note: Please also ensure that you do not change the names of the DataFrames that the three query results will be saved as - creating new cells in the Workspace will rename the DataFrame. Make sure that your final solutions use the names provided: `num_distinct_countries`, `distinct_debt_indicators`, `total_debt`, `highest_debt_country`, `avg_debt_per_indicator`, and `highest_principal_repayment`.