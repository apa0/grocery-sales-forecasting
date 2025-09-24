# This script is for cleaning our data for EDA, ideas listed below 


r""" Data Cleaning Checklist (your version + refinements)
	1.	Check for null values
	    •	Are there any? If so, impute or drop (document decision).
	2.	Exclude certain observations/time periods
	    •	For example: Do we drop returns (negative sales)? Or keep them since they’re real events?
	    •	Are there broken time periods (e.g., missing date ranges)?
	3.	Check column data types
	    •	Dates → convert to datetime.
	    •	Categorical columns (city, family, class) → should be categorical, not strings.
	    •	Numeric columns (sales, transactions, oil) → floats/ints.
	4.	Handle missing values
	    •	Oil prices sometimes missing? Fill by interpolation?
	    •	Holidays/events? Missing → “not a holiday.”
	5.	Parsing strings
	    •	Holidays/events description → you might want to categorize them (e.g., national holiday, religious holiday, transferred).
	6.	Grouping (if needed)
	    •	Aggregate to family/store/day, or keep item/store/day as-is (depends on project direction).
	7.	Rebuild calendar (important here)
	    •	Insert rows with unit_sales = 0 when no sales are recorded for (item, store, date). Otherwise, you’ll overestimate demand.
"""