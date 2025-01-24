import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Set Streamlit to use wide mode
st.set_page_config(
    page_title="Crime Dashboard",  # Title of the dashboard
    page_icon="https://i.imgur.com/3613eIA.png",
    layout="wide")

# Load the datasets
@st.cache_data
def load_data():
    education_df = pd.read_excel("DataEducation2023.xlsx")
    crimes = pd.read_csv("final_crimes_updated.csv")
    return education_df, crimes

# Add custom CSS to make the sidebar static
# Inject custom CSS for styling
st.markdown(
    """
    <style>
    /* Make sidebar static and control its width */
        [data-testid="stSidebar"] {
            width: 250px !important; /* Set the desired width */
            min-width: 250px !important;
            max-width: 250px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a custom visual break to separate sections
def add_divider():
    st.markdown("""
        <hr style="border:1px solid #e8e8e8; margin-top:20px; margin-bottom:20px;">
    """, unsafe_allow_html=True)

def main():
    # Load datasets
    education_df, crimes = load_data()

    # Sidebar navigation with logo and collapsible sections
    st.sidebar.image("https://i.imgur.com/3613eIA.png", width=150)
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Overview", "Crime Statistics", "Education & Crime Analysis", "Socio-Economic Impact", "Integrated Data Visuals"])

    if page == "Overview":
        st.title("The Impact of Educational and Socioeconomic Factors on Crime Patterns in Israel")

        st.markdown("""
            This project explores the intricate connections between crime patterns and educational and socioeconomic factors across different regions of Israel. Through the analysis of data from both the crime and education sectors, the goal is to uncover key trends, patterns, and correlations that may help identify the underlying causes of crime in various settlements.
            The project examines how differences in education—such as dropout rates, Bagrut eligibility, and participation in technological education—can impact crime rates. Simultaneously, it looks at how the socioeconomic conditions of a settlement, including income levels, employment rates, and poverty, may influence the frequency and nature of criminal activity.
            By combining insights from education, socioeconomic, and crime data, the project aims to better understand the interactions between these factors and determine whether improvements in education or socioeconomic conditions could help reduce crime in specific regions.

            The data is sourced from two governmental databases in Israel:
            - **Crime Data** - The Israel Police
            - **Education Data** - The Ministry of Education 

            ##### Central Question:
            What are the differences between localities in Israel in the relationship between education levels, socioeconomic status, and crime rates?

            ##### Sub-Questions:
            1. What is the level of crime in different districts in Israel and the average crime rate in each district over the last 5 years?
            2. What patterns and correlations can be uncovered between education indicators and crime rates across Israeli districts?
            3. How does socio-economic status influence crime levels across different districts in Israel?
            
            &nbsp;
            ### Data Description

            ##### Crime Data:
            The crime dataset covers criminal activity from 2020 to 2024, providing a comprehensive picture of crime patterns across Israeli settlements. It includes data on the number of reported crimes, categorized by crime type and district, along with key demographic information about each settlement. The primary columns/features in this dataset include:
            - **Year** - The year of the crime was recorded.
            - **DistrictName** - The geographical district in which the settlement is located.
            - **Settlement** - The name of city where the crime was reported.
            - **StatisticGroup** - The classification of crime.
            - **StatisticGroupKod** - The associated with the type of crime.
            - **Count** - The number of reported crimes of a particular type.
            - **NumResidents** - The population of the settlement.
            - **CrimeRate** - The calculated crime rate, derived from the number of crimes relative to the population size of the settlement.
            """)
        # Add divider after title for visual separation
        add_divider()
        render_overview_crime(crimes)
        add_divider()


        st.markdown("""
            &nbsp;
            ##### Education Data:
            The education dataset includes information on the educational performance and socio-economic status of Israeli settlements for the year 2023. This dataset is useful for analyzing the relationship between education indicators and crime rates. The primary columns/features in this dataset include:
            - **DistrictName** - The geographical district in which the settlement is located.
            - **Settlement** - The name of city where the crime was reported.
            - **SocioeconomicGroup** - The socioeconomic status classification of the settlement.
            - **NumResidents** - The population of the settlement.
            - **NumStudents** - The number of students in the settlement.
            - **RateInTechEdu** - The percentage of scholars enrolled in technological education programs.
            - **DropoutRate** - The percentage of students who drop out of school.
            - **EligibleForBagrutRate** - he percentage of students eligible for the Bagrut.
            - **EligibleForExcellentBagrutRate** - The percentage of students eligible for a high-level Bagrut.
            - **5UnitsMathematicsRate** - The percentage of students who pass the high-level 5-unit mathematics Bagrut.
         """)


        # # Add divider after title for visual separation
        # add_divider()
        # render_overview_education(education_df)
        # add_divider()

        add_divider()
        render_min_max_general_rates(education_df)
        add_divider()

        st.markdown("""
            &nbsp;
            \n\n
            Combining these two data sources allows for a deeper understanding of the potential relationships between educational features and crime patterns, while also considering geographic and socioeconomic factors. The visualizations developed in this project will enable users to explore and identify trends and patterns in the data, facilitating a better understanding of the complex relationship between education and crime in Israeli society.
        """)

    elif page == "Crime Statistics":
        st.markdown("""
                ### What is the level of crime in different districts in Israel and the average crime rate in each district over the last 5 years?
                
                
                ##### Plot Overview:
                This plot visualizes crime rates over the years across different districts in Israel, highlighting trends in crime for various districts.
                The line graph on the right shows crime trends over the last few years for the selected districts and crime types. It plots the crime rate on the y-axis and the years on the x-axis, making it easy to visualize how crime rates have evolved over time in different areas.
                The mini-bar chart on the left shows the average crime rate for each selected district over the last few years, allowing you to quickly compare crime levels across districts.

                ##### How to use?
                Use the interactive features below to filter by crime type and district, helping you analyze crime trends at the district level.                                                         
                Select Crime Type: Choose the specific type of crime you wish to focus on.                                                                                                             
                Select Districts: Choose the districts you're interested in analyzing.                                                                                                     
            """)

        matala1(crimes)

    elif page == "Education & Crime Analysis":
        st.markdown("""
                ### What patterns and correlations can be uncovered between education indicators and crime rates across Israeli districts?


                ##### Plot Overview:
                This plot compares crime rates and education rates across different districts in Israel. It displays two sets of bars: one representing the crime rate for the selected type of crime and the other representing the education rate for the chosen educational metric. 
                By showing both sets of data side by side, it allows for a clear comparison of how crime levels relate to various education statistics in each district.
                        
                ##### How to use?
                Use the interactive features below to filter by crime type and education indicators, helping you explore the relationship between crime rates and education levels at the district level.
                Select Crime Type: Choose the specific type of crime you want to focus on.                                                                                    
                Select Districts: Choose the education indicator you'd like to explore. 
            """)

        matala2(crimes, education_df)

    elif page == "Socio-Economic Impact":
        st.markdown("""
                ### How does socio-economic status influence crime levels across different districts in Israel?


                ##### Plot Overview:
                This plot shows the distribution of crime rates across different socio-economic groups in Israeli settlements for the selected crime type. The box plot displays how crime rates vary within each group, highlighting the spread and outliers. 
                The y-axis represents crime rates as percentages, and the x-axis shows socio-economic groups (1 to 9), allowing for easy comparison across groups.

                ##### How to use?
                Use the interactive features below to filter by crime type and analyze crime distribution across different socio-economic groups in Israeli settlements.                  
                Select Crime Type: Choose the specific type of crime you want to analyze.
            """)

        matala3(crimes, education_df)

    elif page == "Integrated Data Visuals":
        st.markdown("""
                ### What are the differences between localities in Israel in the relationship between education levels, socioeconomic status, and crime rates?


                ##### Plot Overview:
                This scatter plot shows the relationship between crime rates and education rates across Israeli settlements, highlighting socio-economic groups. It allows you to explore how education indicators, correlate with crime rates.
                Socio-economic groups are color-coded, and each settlement is represented by a circle, with position reflecting the crime rate and selected education indicator.

                ##### How to use?
                Use the interactive features below to filter by crime type and education rate, and explore the relationship between crime rates and education indicators across different socio-economic groups in Israeli settlements.         
                Select Crime Type: Choose the specific type of crime you want to focus on. This will filter the data to show crime rates for the selected crime category.                                                                
                Select Education Rate: Choose one of the available education metrics to analyze its correlation with crime rates.                                                                                                        
                Hover Over Points: Hover over each settlement to view details like its name, crime rate, and the selected education rate.                                     
            """)

        matala4(crimes, education_df)




def render_overview_crime(crimes):
    # Filter the crimes dataset for StatisticGroupKod == -2 and group by year
    filtered_crimes = crimes[crimes['StatisticGroupKod'] == -2]

    # Sum the 'Count' for each year where StatisticGroupKod == -2
    year_counts = filtered_crimes.groupby('Year')['Count'].sum()

    # Define custom HTML and CSS styles
    st.markdown("""
        <style>
            .year-style {
                font-size: 25px;
                font-weight: bold;
                text-align: center;
                padding-left: 1px;  /* Adjust padding-left to move the year slightly to the right */
            }
            .count-style {
                font-size: 21px;
                font-weight: bold;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Directly define the title using inline CSS to ensure it's applied
    st.markdown("""
        <h3 style="font-size: 17px; font-weight: bold; text-align: center; margin-bottom: 20px; font-family: 'Roboto', sans-serif;">
            Crime Statistics Over the Years
        </h3>
    """, unsafe_allow_html=True)

    # Create columns for each year and its count
    col1, col2, col3, col4, col5 = st.columns(5)

    # Populate the columns with year and crime count data
    for i, (year, count) in enumerate(year_counts.items()):
        year_str = int(year)
        count_str = int(count)

        if i == 0:
            col1.markdown(
                f"<div class='year-style'>{year_str}</div><div class='count-style'>{count_str} Crimes</div>",
                unsafe_allow_html=True)
        elif i == 1:
            col2.markdown(
                f"<div class='year-style'>{year_str}</div><div class='count-style'>{count_str} Crimes</div>",
                unsafe_allow_html=True)
        elif i == 2:
            col3.markdown(
                f"<div class='year-style'>{year_str}</div><div class='count-style'>{count_str} Crimes</div>",
                unsafe_allow_html=True)
        elif i == 3:
            col4.markdown(
                f"<div class='year-style'>{year_str}</div><div class='count-style'>{count_str} Crimes</div>",
                unsafe_allow_html=True)
        elif i == 4:
            col5.markdown(
                f"<div class='year-style'>{year_str}</div><div class='count-style'>{count_str} Crimes</div>",
                unsafe_allow_html=True)

def render_overview_education(education_df):
    # Group by SocioeconomicGroup (1-9) and count the number of unique settlements
    socioecon_group_counts = education_df.groupby('SocioeconomicGroup')['Settlement'].nunique()

    st.markdown("""
        <style>
            .group-style {
                font-size: 18px;
                font-weight: bold;
                text-align: center;
            }
            .count-style {
                font-size: 16px;
                font-weight: bold;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Define the title using inline styles
    st.markdown(
        '<h3 style="font-size: 17px; font-weight: bold; text-align: center; margin-bottom: 20px; font-family: \'Roboto\', sans-serif;">Number of Settlements by Socioeconomic Group</h3>',
        unsafe_allow_html=True)

    # Create columns for each group count (up to 9 groups)
    cols = st.columns(9)

    # Populate the columns with SocioeconomicGroup and settlement count data for groups 1-9
    for i, group in enumerate(range(1, 10)):
        count = socioecon_group_counts.get(group, 0)  # Get the count for the group, default to 0 if not present
        group_str = str(group)
        count_str = int(count)

        # Use the appropriate column for each group
        cols[i].markdown(
            f"<div class='group-style'>{group_str}</div>"
            f"<div class='count-style'>{count_str} Settlements</div>",
            unsafe_allow_html=True)

def render_min_max_general_rates(education_df):
    # Features to calculate min, max, and average rates
    features = ['EligibleForBagrutRate', 'EligibleForExcellentBagrutRate', 'DropoutRate',
                '5UnitsMathematicsRate', 'RateInTechEdu']

    # Calculate min, max, and mean for each feature
    min_max_avg_stats = education_df[features].agg(['min', 'max', 'mean']).transpose()

    st.markdown("""
        <style>
            .feature-style {
                font-size: 16px; /* Adjust font size */
                text-align: center;
                margin-bottom: 5px;
                font-family: 'Arial', sans-serif; /* Change font family */
                font-weight: bold; /* Make text bold */
            }
            .rate-style {
                font-size: 15px; /* Adjust font size for rates */
                text-align: center;
                margin-top: 5px;
                font-family: 'Arial', monospace; /* Change font family for rates */
                font-weight: bold; /* Optional: Make text normal weight */
            }
        </style>
    """, unsafe_allow_html=True)

    # Define the title using inline styles
    st.markdown(
        '<h3 style="font-size: 17px; font-weight: bold; text-align: center; margin-bottom: 20px; font-family: \'Roboto\', sans-serif;">Min, Max, and Average Rates for Education Features</h3>',
        unsafe_allow_html=True)

    # Create columns to display results
    cols = st.columns(len(features))

    for i, feature in enumerate(features):
        min_value = min_max_avg_stats.loc[feature, 'min'] * 100
        max_value = min_max_avg_stats.loc[feature, 'max'] * 100
        avg_value = min_max_avg_stats.loc[feature, 'mean'] * 100

        # Display each feature's min, max, and average in its own column
        cols[i].markdown(
            f"<div class='feature-style'>{feature}</div>"
            f"<div class='rate-style'>Min: {min_value:.1f}%</div>"
            f"<div class='rate-style'>Max: {max_value:.1f}%</div>"
            f"<div class='rate-style'>Avg: {avg_value:.1f}%</div>",
            unsafe_allow_html=True
        )




def matala1(crimes):
    ## Section 1: Crime Rate by Year for Districts
    st.markdown("""
                <style>
                    .custom-title {
                        font-size: 30px;  /* Font size */
                        font-weight: bold;  /* Font weight */
                    }
                </style>
                <div class="custom-title">
                    Crime Rate by Year for Different Districts
                </div>
            """, unsafe_allow_html=True)

    # Data preparation for both the main graph and the mini graph
    district_df = crimes.copy()

    # Convert CrimeRate to numeric and normalize
    district_df["CrimeRate"] = district_df["CrimeRate"].astype(str).str.rstrip('%').astype(float) / 100

    # Aggregate by District, Year, and StatisticGroup for the main graph and the mini graph
    district_agg = district_df.groupby(
        ["DistrictName", "Year", "StatisticGroup"], as_index=False
    )["CrimeRate"].mean()

    # Create a container for the entire layout
    with st.container():
        # Create a single column for the filters that span the full width
        #st.markdown("### Select Filters for Crime Rate Visualization")

        # Create two columns for the filters (crime type and districts) side by side
        filter_col1, filter_col2 = st.columns([1, 2])  # Adjust these proportions to your needs

        with filter_col1:
            # Crime type filter
            crime_type = st.selectbox(
                "Select Type of Crime:",
                options=crimes["StatisticGroup"].unique(),
                index=list(crimes["StatisticGroup"].unique()).index("כל העבירות")  # Set default to "כל העבירות"
            )

        with filter_col2:
            # District filter
            districts = st.multiselect(
                "Select Districts:",
                options=crimes["DistrictName"].unique(),
                default=["צפון", "מרכז", "דרום", "ירושלים", "תל אביב", "חיפה"],
                key="district_filter"
            )

            # Dynamically adjust filter width based on number of districts selected
            district_count = len(districts)
            filter_col2.width = 300 + (district_count * 20)  # Adjust width based on selection length

    # Filter the aggregated data based on selections for the main graph
    filtered_data = district_agg[
        (district_agg["DistrictName"].isin(districts)) &
        (district_agg["StatisticGroup"] == crime_type)
    ]

    # Plot Section: Create columns for main plot and mini plot
    with st.container():
        # Create two columns for the plots (main plot and mini plot)
        col1, col2 = st.columns([1, 3])  # The first column is smaller, the second is bigger (adjust proportions)

        # Mini plot (average crime rate by district)
        with col1:
            # Calculate the average crime rate by district
            avg_crime_rate_by_district = district_agg[
                (district_agg["DistrictName"].isin(districts)) &
                (district_agg["StatisticGroup"] == crime_type)
            ].groupby("DistrictName")["CrimeRate"].mean().reset_index()

            # Sort the DataFrame by CrimeRate in ascending order
            avg_crime_rate_by_district = avg_crime_rate_by_district.sort_values("CrimeRate", ascending=True)

            # Create a consistent color mapping for DistrictName
            unique_districts = crimes["DistrictName"].unique()
            color_mapping = {district: color for district, color in zip(unique_districts, px.colors.qualitative.Set2)}

            # Filter data for the year 2024 and crime type
            year_2024_data = district_agg[
                (district_agg["Year"] == 2024) & (district_agg["StatisticGroup"] == crime_type)]
            sorted_districts = year_2024_data.sort_values("CrimeRate", ascending=False)["DistrictName"].tolist()

            # Mini plot: Average crime rate by district
            fig_mini = px.bar(
                avg_crime_rate_by_district,
                y="DistrictName",
                x="CrimeRate",
                color="DistrictName",
                color_discrete_map=color_mapping,  # Use the shared color mapping
                labels={"CrimeRate": "Average Crime Rate", "DistrictName": "District Name"},
            )

            # Customize layout for the mini graph
            fig_mini.update_layout(
                xaxis=dict(
                    title="Average Crime Rate (%)",
                    tickformat=".2%",  # Format x-axis as a percentage
                    title_font=dict(size=15),  # Font size for x-axis title
                    tickfont=dict(size=15),  # Font size for x-axis values
                    tickangle=25,  # Fix the angle of the x-axis labels
                ),
                yaxis=dict(
                    title="District Name",
                    tickmode="linear",
                    dtick=1,  # Adjust y-axis ticks
                    title_font=dict(size=15),  # Font size for y-axis title
                    tickfont=dict(size=15)  # Font size for y-axis values
                ),
                title={
                    'text': "Average Crime Rate by District",
                    'x': 0.5,  # Center the title
                    'y': 0.77,  # Move the title down
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {'size': 17}  # Title font size
                },
                margin=dict(l=40, r=40, t=170, b=20),  # Adjust margins
                height=400,  # Set height
                showlegend=False,  # No legend for this plot
            )

            # Display the mini graph
            st.plotly_chart(fig_mini, use_container_width=True)

        # Main plot (Crime Rate by Year for Selected Districts)
        with col2:
            #st.markdown("### Crime Rate by Year for Selected Districts")

            if not filtered_data.empty:
                # Main plot: Crime Rate by Year for Selected Districts and Crime Type
                fig = px.line(
                    filtered_data,
                    x="Year",
                    y="CrimeRate",
                    color="DistrictName",
                    color_discrete_map=color_mapping,  # Use the shared color mapping
                    category_orders={"DistrictName": sorted_districts},  # Order districts based on 2024 data
                    labels={"CrimeRate": "Crime Rate (%)", "Year": "Year"},
                    title="Crime Rate by Year for Selected Districts and Crime Type",
                )

                fig.update_traces(line=dict(width=4))

                # Customize layout for the main graph
                fig.update_layout(
                    title={
                        'text': "Crime Rate by Year for Selected Districts and Crime Type",  # Title text
                        'font': {
                            'size': 22,  # Font size
                        },
                        'x': 0.5,  # Center the title
                        'xanchor': 'center',
                    },
                    legend=dict(
                        title="Districts",
                        font=dict(size=16)  # Font size for legend labels
                    ),
                    xaxis=dict(
                        title="Year",
                        tickmode="linear",
                        dtick=1,
                        title_font=dict(size=20),  # Font size for x-axis title
                        tickfont=dict(size=17)  # Font size for x-axis values
                    ),
                    yaxis=dict(
                        title="Crime Rate (%)",
                        tickformat=".2%",
                        title_font=dict(size=20),  # Font size for y-axis title
                        tickfont=dict(size=15)  # Font size for x-axis values
                    ),
                    font=dict(size=25),  # General font size for labels and other text
                    margin=dict(l=40, r=40, t=50, b=0),  # Margins
                    height=400  # Graph height
                )

                # Display the chart in Streamlit
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data available for the selected filters.")

def matala2(crimes, education_df):
    # Custom title
    st.markdown("""
                <style>
                    .custom-title {
                        font-size: 30px;  /* Font size */
                        font-weight: bold;  /* Font weight */
                    }
                </style>
                <div class="custom-title">
                    Crime Rate vs Education Rate in Different Districts
                </div>
            """, unsafe_allow_html=True)

    # Function to preprocess data (handle percentage columns)
    def preprocess_data(df, percentage_columns):
        for col in percentage_columns:
            df[col] = df[col].astype(str).str.replace('%', '').replace('nan', '0').astype(float)
        return df

    # Preprocess crime and education data
    crime_data = preprocess_data(crimes.copy(), ['CrimeRate'])
    education_df_copy = education_df.copy()
    education_df_copy[['RateInTechEdu', 'DropoutRate', 'EligibleForBagrutRate',
                       '5UnitsMathematicsRate', 'EligibleForExcellentBagrutRate']] *= 100
    education_data = preprocess_data(education_df_copy, [
        'RateInTechEdu', 'DropoutRate', 'EligibleForBagrutRate',
        '5UnitsMathematicsRate', 'EligibleForExcellentBagrutRate'
    ])

    # Filter for the year 2023
    crime_data = crime_data[crime_data['Year'] == 2023]

    # Mappings for crime types and education rates
    statistic_group_mapping = {
        'עבירות בטחון': 'עבירות בטחון',
        'עבירות כלפי המוסר': 'עבירות כלפי המוסר',
        'עבירות כלפי הרכוש': 'עבירות כלפי הרכוש',
        'עבירות מין': 'עבירות מין',
        'עבירות מרמה': 'עבירות מרמה',
        'עבירות נגד אדם': 'עבירות נגד אדם',
        'עבירות נגד גוף': 'עבירות נגד גוף',
        'עבירות סדר ציבורי': 'עבירות סדר ציבורי',
        'עבירות רשוי': 'עבירות רשוי',
        'עבירות תנועה': 'עבירות תנועה',
        'כל העבירות': 'כל העבירות'
    }

    rate_mapping = {
        'RateInTechEdu': "תלמידים בחינוך טכנולוגי",
        'DropoutRate': "נשירה מלימודים",
        'EligibleForBagrutRate': "זכאים לבגרות",
        '5UnitsMathematicsRate': "זכאים 5 יחידות מתמטיקה",
        'EligibleForExcellentBagrutRate': "זכאים לבגרות מצטיינת"
    }
    default_rate = '5UnitsMathematicsRate'

    # Crime type selection
    crime_options = list(statistic_group_mapping.values())
    default_crime_index = min(11, len(crime_options) - 1)
    col1, col2 = st.columns(2)
    with col1:
        selected_crime = st.selectbox("Select Type of Crime", crime_options, index=default_crime_index)
    with col2:
        selected_rate = st.selectbox("Select Education Rate", list(rate_mapping.values()), index=4)

    # Reverse mappings
    reverse_rate_mapping = {v: k for k, v in rate_mapping.items()}
    selected_rate_column = reverse_rate_mapping.get(selected_rate, default_rate)

    # Filter and combine data
    filtered_crime = crime_data[crime_data['StatisticGroup'] == selected_crime]
    crime_summary = filtered_crime.groupby('DistrictName')['CrimeRate'].mean().reset_index()
    education_summary = education_data.groupby('DistrictName')[selected_rate_column].mean().reset_index()
    combined_data = pd.merge(crime_summary, education_summary, on='DistrictName', how='inner')

    # Bar plot with ColorBrewer palette
    fig = go.Figure()

    # Add crime rate bar
    fig.add_trace(go.Bar(
        x=combined_data['DistrictName'],
        y=combined_data['CrimeRate'],
        name=selected_crime,
        marker_color=px.colors.qualitative.Set2[0],  # Color from Set2
        text=combined_data['CrimeRate'].apply(lambda x: f"{x:.2f}"),  # Text for outside position
        textposition='outside',
        textfont={'size': 16},
        hovertemplate=(
            '<b>%{x}</b><br>'
            f'{selected_crime}:<br>'
            '%{y:.2f}%<extra></extra>'
        )
    ))

    # Add education rate bar
    fig.add_trace(go.Bar(
        x=combined_data['DistrictName'],
        y=combined_data[selected_rate_column],
        name=selected_rate,
        marker_color=px.colors.qualitative.Set2[1],  # Another color from Set2
        text=combined_data[selected_rate_column].apply(lambda x: f"{x:.2f}"),  # Text for outside position
        textposition='outside',
        textfont={'size': 16},
        hovertemplate=(
            '<b>%{x}</b><br>'
            f'{selected_rate}:<br>'
            '%{y:.2f}%<extra></extra>'
        )
    ))

    # Update layout
    fig.update_layout(
        barmode='group',  # Grouped bars
        xaxis={'title': 'District Name', 'titlefont': {'size': 20}, 'tickfont': {'size': 18}},
        yaxis={'title': 'Percentage', 'titlefont': {'size': 20}, 'tickfont': {'size': 18}},
        height=550,
        width=1300,
        margin={'l': 50, 'r': 50, 't': 80, 'b': 100},
        legend={'font': {'family': 'Arial', 'size': 18}}
    )

    # Display the plot
    st.plotly_chart(fig)

def matala3(crimes, education_df):
    # Custom CSS to move the selectbox more precisely and ensure centering
    st.markdown("""
        <style>
            /* Target the outer container of the selectbox widget to move it */
            div[role="listbox"] {
                position: relative !important;
                left: 0 !important;  /* Keep the selectbox in center */
                transform: translateX(-50%) !important;  /* Move the selectbox horizontally to center */
                width: auto !important;  /* Let the width auto-adjust */
            }
            .css-1d391kg {  /* Adjust the spacing of the main container */
                padding: 0 1rem;  /* Adjust top and side padding */
            }
            .css-18e3th9 {  /* Adjust the spacing of the sidebar (filters) */
                padding: 0 0 0px 0;  /* Top, right, bottom, left */
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("""
        <style>
            .custom-title {
                font-size: 30px;  /* Font size */
                font-weight: bold;  /* Font weight */
            }
        </style>
        <div class="custom-title">
            Distribution of Crime Percentage by Socio-Economic Group
        </div>
    """, unsafe_allow_html=True)

    # Define available crime types
    crime_types = crimes['StatisticGroup'].unique().tolist()
    default_crime_type = "כל העבירות"  # "All Crimes" in Hebrew

    # Create a column layout with equal width
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the numbers to control the proportions

    with col2:
        # Add a filter for crime type
        crime_type_filter = st.selectbox(
            "Select Crime Type:",
            options=crime_types,
            index=crime_types.index(default_crime_type)
        )

    # Merge crimes with education data to include socio-economic group
    df_boxplot = pd.merge(crimes, education_df, on="Settlement")
    df_boxplot['CrimeRate'] = df_boxplot['CrimeRate'].str.rstrip('%').astype(float)
    # Scale the CrimeRate values by dividing by 100 to get them between 0 and 1
    df_boxplot['CrimeRate'] = df_boxplot['CrimeRate'] / 100

    # Filter the data for the selected crime type and year, and remove group 10
    df_boxplot = df_boxplot[
        (df_boxplot['StatisticGroup'] == crime_type_filter) &
        (df_boxplot['Year'] == 2023) &
        (df_boxplot['SocioeconomicGroup'] < 10)  # Exclude group 10
    ]

    # Use plotly.graph_objects for more control
    import plotly.graph_objects as go

    # Define a colorblind-friendly color palette (Set2 from ColorBrewer)
    color_palette = [
        "#66c2a5", "#fc8d62", "#8da0cb",
        "#e78ac3", "#a6d854", "#ffd92f",
        "#e5c494", "#b3b3b3", "#1f78b4"
    ]

    fig = go.Figure()

    # Add traces for each socio-economic group (1-9)
    for group in range(1, 10):
        filtered = df_boxplot[df_boxplot['SocioeconomicGroup'] == group]
        fig.add_trace(
            go.Box(
                y=filtered['CrimeRate'],
                name=str(group),  # Group as category
                boxpoints="all",  # Show all points
                jitter=0.3,  # Add some jitter to points for better visibility
                pointpos=0,  # Align points directly on the group
                marker=dict(size=6, color=color_palette[group - 1]),  # Apply colorblind-friendly color
                line=dict(color=color_palette[group - 1]),  # Apply line color
                width=0.6  # Box width
            )
        )

    fig.update_layout(
        # Y-axis customization
        yaxis=dict(
            title="Crime Rate (%)",
            title_font=dict(
                size=19,
            ),
            tickfont=dict(
                size=16,
            ),
            tickformat=".0%"  # Add the percentage sign to the ticks
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 10)),
            ticktext=list(range(1, 10)),  # Explicitly set x-axis labels
            title="Socio-Economic Group (1 to 9)",
            title_font=dict(
                size=19,
            ),
            tickfont=dict(
                size=16,
            )
        ),
        # Legend customization
        legend=dict(
            font=dict(
                size=17
            ),
            orientation="v",
            yanchor="top",
            xanchor="right",
            x=1.15,
            y=0.7
        ),
        margin=dict(l=20, r=20, t=20, b=20),  # Tight margins
        width=1400,
        height=600,
    )

    # Display the chart
    st.plotly_chart(fig)

def matala4(crimes, education_df):
    st.markdown("""
            <style>
                /* Adjust width of selectboxes */
                .stSelectbox select {
                    width: 200px;  /* Set the width of the selectbox */
                }
                /* Title customization */
                .custom-title {
                    font-size: 30px;
                    font-weight: bold;
                }
            </style>
        """, unsafe_allow_html=True)

    st.markdown("""
            <div class="custom-title">
                Distribution of Settlements Based on Crime and Education Rate, with Socio-Economic Grouping
            </div>
        """, unsafe_allow_html=True)

    # Define rate mapping
    rate_mapping = {
        'RateInTechEdu': "תלמידים בחינוך טכנולוגי",
        'DropoutRate': "נשירה מלימודים",
        'EligibleForBagrutRate': "זכאים לבגרות",
        '5UnitsMathematicsRate': "זכאים 5 יחידות מתמטיקה",
        'EligibleForExcellentBagrutRate': "זכאים לבגרות מצטיינת"
    }

    # Default selected rate
    default_rate = 'EligibleForBagrutRate'

    # Define available crime types
    crime_types = crimes['StatisticGroup'].unique().tolist()
    default_crime_type = "כל העבירות"

    # Add filters in one line using st.columns
    col1, col2 = st.columns(2)

    with col1:
        rate_filter = st.selectbox(
            "Select Education Rate:",
            options=list(rate_mapping.values()),
            index=list(rate_mapping.values()).index(rate_mapping[default_rate])
        )

    with col2:
        crime_type_filter = st.selectbox(
            "Select Crime Type:",
            options=crime_types,
            index=crime_types.index(default_crime_type)
        )

    # Reverse the rate mapping to get the column names
    reverse_rate_mapping = {v: k for k, v in rate_mapping.items()}
    selected_rate = reverse_rate_mapping.get(rate_filter, default_rate)

    # Prepare the data
    df_scatter = pd.merge(crimes, education_df, on='Settlement')
    df_scatter['CrimeRate'] = df_scatter['CrimeRate'].str.rstrip('%').astype(float) / 100  # Correct scaling

    # Filter the data for the selected education rate and crime type
    df_scatter = df_scatter[
        (df_scatter['StatisticGroup'] == crime_type_filter) &
        (df_scatter['Year'] == 2023) &
        df_scatter[selected_rate].notna()
    ]

    # Create the scatter plot with customized hovertemplate
    fig4 = px.scatter(
        df_scatter,
        x=selected_rate,
        y="CrimeRate",
        size_max=12,  # Set the maximum size of the circles
        size=[10] * len(df_scatter),  # Set all sizes to be identical
        color="SocioeconomicGroup",
        hover_name="Settlement",
        labels={selected_rate: rate_mapping[selected_rate], "CrimeRate": "Crime Rate (%)"},
    )

    # Update the layout to show percentages on both axes
    fig4.update_layout(
        xaxis=dict(
            title=rate_mapping[selected_rate],
            title_font=dict(size=20),
            tickfont=dict(size=16),
            tickformat=".0%"
        ),
        yaxis=dict(
            title="Crime Rate (%)",
            title_font=dict(size=20),
            tickfont=dict(size=16),
            tickformat=".0%"
        ),
        legend=dict(
            title="Socio-Economic Group",
            title_font=dict(size=18, color="black"),
            font=dict(size=14, color="black"),
            tracegroupgap=10
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        width=1000,
        height=500
    )

    # Display the chart
    st.plotly_chart(fig4)







if __name__ == "__main__":
    main()