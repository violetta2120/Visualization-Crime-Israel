# The Impact of Educational and Socioeconomic Factors on Crime Patterns in Israel

An interactive data-visualization dashboard that explores how education and socio-economic conditions relate to crime patterns across Israeli districts and settlements.

**🔗 Live dashboard:** https://visualization-crime-israel.streamlit.app/

---

## Motivation

Crime rates are rarely explained by a single cause. I wanted to look beyond the headline numbers and ask whether education and socio-economic conditions help explain *where* and *how much* crime happens in Israel. By bringing crime, education, and socio-economic data into one place, the goal was to make these relationships something you can actually explore and see, rather than just read about - for any district, crime type, or education indicator.

## What the dashboard does

The app integrates two datasets and presents them through five interactive views:

- **Overview** - summarizes both datasets: crime activity from 2020-2024 (crime types, districts, demographics for Israeli settlements) and 2023 education/socio-economic data, with headline statistics for each.
- **Crime Statistics** - crime rates by district over five years, with a line chart of trends and a bar chart of each district's average. Filter by crime type and district.
- **Education & Crime Analysis** - a side-by-side comparison of crime rates against a chosen education indicator (e.g. 5-Unit Mathematics, Bagrut eligibility) for each district.
- **Socio-Economic Impact** - a box plot showing the distribution of crime rates across the nine socio-economic clusters (1 = lowest, 9 = highest).
- **Integrated Data Visuals** - a scatter plot combining all three dimensions: crime rate vs. an education indicator, with points color-coded by socio-economic cluster, at the settlement level.

Each view includes interactive controls (crime-type, district, and education-metric selectors) and hover tooltips for detail.

## The data

- **Crime data (2020-2024):** crime counts and rates by type, district, and settlement, with demographic information. Total recorded crimes stayed broadly stable year to year (≈332k-350k), peaking in 2021.
- **Education & socio-economic data (2023):** settlement-level indicators including Bagrut eligibility, 5-Unit Mathematics, technological education, school dropout rate, excellent-Bagrut eligibility, and a socio-economic cluster (1-9).
- The two sources were cleaned, aligned to a common district/settlement level, and merged into a unified analytical dataset.

## Data Sources

The datasets used in this project was compiled from publicly available data published by:

- **Israel Police** - crime statistics and related public data.
- **Israel Ministry of Education** - educational, socio-economic and demographic data.

## Key findings

- **Crime is strongly district-dependent.** The Southern district has the highest crime rate throughout 2020–2024 (around 5–5.5%), while the Central district is consistently the lowest (around 3%). Jerusalem spiked in 2022 (~4.2%) before declining.
- **Higher educational attainment tracks with lower crime.** Districts with higher rates of 5-Unit Mathematics and Bagrut eligibility (Center, Tel Aviv) tend to show lower crime, whereas the South - with the lowest 5-Unit Math rate - has the highest crime.
- **A clear socio-economic gradient.** Crime rates tend to fall as the socio-economic cluster rises: the highest cluster (9) has the lowest median crime rate (~2.4%), while lower clusters sit higher (~4%), albeit with some high outliers.
- **The three factors reinforce each other.** At the settlement level, localities with higher education indicators *and* higher socio-economic status cluster together at lower crime rates.

> These are exploratory, correlational observations from the data - they describe patterns, not proven causation.

## Tech stack

- **Python**
- **Streamlit** - interactive multi-page app
- **Pandas / NumPy** - data cleaning and integration
- **Plotly** - interactive line, bar, box, and scatter charts


## Author

**Violetta Suhorukov** - B.Sc. Data Engineering, Ben-Gurion University
📧 violetta212067@gmail.com
