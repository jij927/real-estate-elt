# Business Questions

Dataset: Dubai Land Department real estate transactions (open data).

## Scope and ground rules

- Price analysis uses **Sales** transactions only. Gifts, mortgages and other transaction groups can carry values that do not reflect market prices.
- Use the **median** price per sqm, not the average, because outliers distort averages.
- Only rank an area if it has a minimum number of sales (for example 30).
- Time analysis uses `instance_date`, not `load_timestamp` (which is when the file was loaded).

## Core questions (dashboard)

1. How have monthly transaction volume and total transaction value changed over time, split by transaction type?
2. Which areas have the highest and lowest median price per sqm for sales?
3. Which areas have grown fastest in price per sqm year over year?
4. How does off-plan property compare with ready property in volume and median price per sqm, and how has the off-plan share changed over time?
5. Which property types, sub-types and room counts dominate sales, and at what price points?

## Extended questions

6. Which master projects have the highest total sales value and volume?
7. What share of sales are first sales (pre-registration) versus resales, by area?
8. Does proximity to a metro station or mall relate to price per sqm? (Only if these columns are well populated; decide after profiling.)
9. Within the same property type, does parking availability relate to price per sqm?

## Data quality questions (feeds dbt tests and the README)

10. How many records have missing or suspicious values (zero value, missing area, extreme price per sqm)?
11. Is `transaction_id` unique, and what duplicates exist?
12. Which text fields have inconsistent spellings or casing (for example master project and building names)?

## Open items to confirm after profiling

- [ ] Date range actually covered by the data
- [ ] Transaction groups and registration types present, and their row counts
- [ ] How complete the metro, mall, landmark and rent columns are
- [ ] Units and definition of `meter_sale_price` (AED per sqm?)
- [ ] Whether question 8 and 9 stay in scope