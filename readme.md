# life expectancy visualization

Downloaded:

 * Life table for Sweden, "Total (both sexes)" meaning both Females
   and Males, 5-year age interval (but birth to one year is still
   split out separately), 10-year year interval
     * Linked from: https://www.mortality.org/cgi-bin/hmd/country.php?level=1&cntr=SWE
     * Link: https://www.mortality.org/hmd/SWE/STATS/bltper_5x10.txt
     * Recommended citation: "Human Mortality Database. University of
       California, Berkeley (USA), and Max Planck Institute for
       Demographic Research (Germany). Available at www.mortality.org
       or www.humanmortality.de (data downloaded on 2020-08-06)."
     * Data sources of HMD for the Sweden data:
       https://www.mortality.org/hmd/SWE/DOCS/ref.pdf

My interpretation of the data fields is based largely on this
convenient summary from here:
https://www.ssa.gov/OACT/HistEst/CohLifeTables/LifeTableDefinitions.pdf

 * q_x: The probability that a person exact age x will die within one year.
 * l_x: The number of persons surviving to exact age x.
 * d_x: The number of deaths between exact ages x and x+1.
 * L_x: The number of person-years lived between exact ages x and x+1.
 * T_x: The number of person-years lived after exact age x.
 * e_x: The average number of years of life remaining at exact age x.

I care mostly about d_x, which always sums to 100,000 for a period.

Processing data in `process.py`...

```bash
python process.py
```

Working with the produced `data.csv` values in `visualization.xlsx`.

Ended up just taking a screenshot to make `lifetimes_in_sweden.png`.


---

Other notes:

 * The UK has nice data with real counts of for age of death by year,
   but it only goes back to 1963:
   https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/deathsregisteredinenglandandwalesseriesdrreferencetables
 * But, also in the UK: "The Births and Deaths Registration Act (1836)
   made it a legal requirement for all deaths to be registered from 1
   July 1837." So maybe I'm missing something? mortality.org has data
   from 1841, so it exists somewhere...
   https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/methodologies/mortalitystatisticsinenglandandwalesqmi
 * https://www.bbc.com/future/article/20181002-how-long-did-ancient-people-live-life-span-versus-longevity
 * of course https://en.wikipedia.org/wiki/Life_expectancy
