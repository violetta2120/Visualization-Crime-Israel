import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Set Streamlit to use wide mode
st.set_page_config(
    page_title="Crime Dashboard",  # Title of the dashboard
    page_icon="https://i.imgur.com/3613eIA.png",
    layout="centered")

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
            This dashboard analyzes the connections between crime rates and education and socioeconomic factors across Israel. By examining data from both crime and education sectors, it aims to uncover trends and correlations that help explain crime patterns in various settlements.

            ### Data Overview

            ##### Crime Data:
            The crime dataset covers criminal activity from 2020 to 2024, detailing crime types, district data, and demographic information for Israeli settlements.            """)
        # Add divider after title for visual separation
        add_divider()
        render_overview_crime(crimes)
        add_divider()


        st.markdown("""
            &nbsp;
            ##### Education Data:
            The education dataset provides information on the educational performance and socio-economic status of Israeli settlements for 2023.
            """)
        add_divider()
        render_min_max_general_rates(education_df)
        add_divider()

        st.markdown("""
            &nbsp;
            \n\n
            By combining these two data sources, the dashboard provides insights into the links between education, crime, and socio-economic factors in Israel. It allows users to explore trends and patterns, offering a clearer understanding of the complex relationship between education and crime.        """)

    elif page == "Crime Statistics":
        st.markdown("""
                ### What is the level of crime in different districts in Israel and the average crime rate in each district over the last 5 years?
                
                
                ##### Plot Overview:
                This plot displays crime rates across different Israeli districts over the years. The line graph on the right tracks crime trends by district and type, with the y-axis representing crime rates and the x-axis showing the years. 
                The mini-bar chart on the left highlights the average crime rate for each district in recent years, enabling easy comparisons between districts.

                ##### How to use?                                                     
                Select Crime Type: Choose the specific type of crime you wish to focus on.                                                                                                             
                Select Districts: Choose the districts you're interested in analyzing.                                                                              
                Hover over the line/bar to see district names and their corresponding crime percentage.                                                                                                    
            """)

        matala1(crimes)

    elif page == "Education & Crime Analysis":
        st.markdown("""
                ### What patterns and correlations can be uncovered between education indicators and crime rates across Israeli districts?


                ##### Plot Overview:
                This plot compares crime and education rates across Israeli districts, displaying two sets of bars: one for crime rates and one for education metrics. 
                It enables a clear comparison of how crime levels relate to education statistics in each district.
                        
                ##### How to use?
                Select Crime Type: Choose the specific type of crime you want to focus on.                                                                                    
                Select Districts: Choose the education indicator you'd like to explore. 
            """)

        matala2(crimes, education_df)

    elif page == "Socio-Economic Impact":
        st.markdown("""
                ### How does socio-economic status influence crime levels across different districts in Israel?


                ##### Plot Overview:
                This plot displays the distribution of crime rates across socio-economic groups in Israeli settlements. 
                The box plot shows the spread and outliers of crime rates within each group, with crime rates on the y-axis and socio-economic groups (1 to 9) on the x-axis for easy comparison.

                ##### How to use?                
                Select Crime Type: Choose the specific type of crime you want to analyze.                                                                               
                Hover over a point to see the socio-economic group number and its corresponding crime percentage.                                                                        
                In full screen of the plot, hover over the box to view details like the minimum and maximum values for each socio-economic group.
            """)

        matala3(crimes, education_df)

    elif page == "Integrated Data Visuals":
        st.markdown("""
                ### What are the differences between localities in Israel in the relationship between education levels, socioeconomic status, and crime rates?


                ##### Plot Overview:
                This scatter plot shows the relationship between crime rates and education rates across Israeli settlements, with socio-economic groups color-coded. 
                Each settlement is represented by a circle, where the position reflects the crime rate and selected education indicator, allowing for easy exploration of their correlation.

                ##### How to use?
                Select Crime Type: Choose the specific type of crime to focus on.                                                                                                         
                Select Education Rate: Choose an education metric to analyze its correlation with crime rates.                                                                                      
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
                font-size: 21px;
                font-weight: bold;
                text-align: center;
                padding-left: 1px;  /* Adjust padding-left to move the year slightly to the right */
            }
            .count-style {
                font-size: 17px;
                font-weight: bold;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Directly define the title using inline CSS to ensure it's applied
    st.markdown("""
        <h3 style="font-size: 18px; font-weight: bold; text-align: center; margin-bottom: 20px; font-family: 'Roboto', sans-serif;">
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
    features = list(education_translation.keys())

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
                font-size: 14px; /* Adjust font size for rates */
                text-align: center;
                margin-top: 5px;
                font-family: 'Arial', monospace; /* Change font family for rates */
                font-weight: bold; /* Optional: Make text normal weight */
            }
        </style>
    """, unsafe_allow_html=True)

    # Define the title using inline styles
    st.markdown(
        '<h3 style="font-size: 18px; font-weight: bold; text-align: center; margin-bottom: 20px; font-family: \'Roboto\', sans-serif;">Min, Max, and Average Rates for Education Features</h3>',
        unsafe_allow_html=True)

    # Create columns to display results
    cols = st.columns(len(features))

    for i, feature in enumerate(features):
        # Get the translated name
        translated_feature = education_translation[feature]

        # Calculate min, max, and average values
        min_value = min_max_avg_stats.loc[feature, 'min'] * 100
        max_value = min_max_avg_stats.loc[feature, 'max'] * 100
        avg_value = min_max_avg_stats.loc[feature, 'mean'] * 100

        # Display each feature's min, max, and average in its own column
        cols[i].markdown(
            f"<div class='feature-style'>{translated_feature}</div>"
            f"<div class='rate-style'>Min: {min_value:.1f}%</div>"
            f"<div class='rate-style'>Max: {max_value:.1f}%</div>"
            f"<div class='rate-style'>Avg: {avg_value:.1f}%</div>",
            unsafe_allow_html=True
        )



# Create the translation dictionaries
district_translation = {
    "מרכז": "Center",
    "תל אביב": "Tel Aviv",
    "חיפה": "Haifa",
    "דרום": "South",
    "ירושלים": "Jerusalem",
    "צפון": "North"
}

statistic_group_translation = {
    "כל העבירות": "All Crimes",
    "עבירות כלפי המוסר": "Moral Offenses",
    "עבירות כלפי הרכוש": "Property Offenses",
    "עבירות מרמה": "Fraud Offenses",
    "עבירות סדר ציבורי": "Public Order Offenses",
    "עבירות מנהליות": "Administrative Offenses",
    "עבירות מין": "Sex Offenses",
    "עבירות נגד גוף": "Offenses Against the Body",
    "עבירות בטחון": "Security Offenses"
}

education_translation = {
    "RateInTechEdu": "Technological education",
    "DropoutRate": "Dropout of School",
    "EligibleForBagrutRate": "Eligible For Bagrut",
    "5UnitsMathematicsRate": "5 Units Mathematics",
    "EligibleForExcellentBagrutRate": "Eligible For Excellent Bagrut"
}



def matala1(crimes):
    # Apply translations
    crimes["DistrictName"] = crimes["DistrictName"].replace(district_translation)
    crimes["StatisticGroup"] = crimes["StatisticGroup"].replace(statistic_group_translation)

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

    district_df = crimes.copy()
    # Define Hebrew crime categories to remove
    hebrew_crime_categories = [
        "עבירות נגד אדם", "עבירות רשוי", "עבירות תנועה",
        "עבירות כלכליות", "סעיפי הגדרה", "שאר עבירות"
    ]

    # Filter out rows with these crime names
    district_df = district_df[~district_df["StatisticGroup"].isin(hebrew_crime_categories)]
    district_df["CrimeRate"] = district_df["CrimeRate"].astype(str).str.rstrip('%').astype(float) / 100

    district_agg = district_df.groupby(["DistrictName", "Year", "StatisticGroup"], as_index=False)["CrimeRate"].mean()

    with st.container():
        filter_col1, filter_col2 = st.columns([1, 2])

        with filter_col1:
            crime_type = st.selectbox(
                "Select Type of Crime:",
                options=district_df["StatisticGroup"].unique(),
                index=list(district_df["StatisticGroup"].unique()).index("All Crimes")
            )

        with filter_col2:
            districts = st.multiselect(
                "Select Districts:",
                options=district_df["DistrictName"].unique(),
                default=["North", "Center", "South", "Jerusalem", "Tel Aviv", "Haifa"],
                key="district_filter"
            )

    filtered_data = district_agg[
        (district_agg["DistrictName"].isin(districts)) &
        (district_agg["StatisticGroup"] == crime_type)
    ]

    with st.container():
        col1, col2 = st.columns([1, 3])

        with col1:
            avg_crime_rate_by_district = district_agg[
                (district_agg["DistrictName"].isin(districts)) &
                (district_agg["StatisticGroup"] == crime_type)
            ].groupby("DistrictName")["CrimeRate"].mean().reset_index()

            avg_crime_rate_by_district = avg_crime_rate_by_district.sort_values("CrimeRate", ascending=True)

            unique_districts = district_df["DistrictName"].unique()
            color_mapping = {district: color for district, color in zip(unique_districts, px.colors.qualitative.Set2)}

            year_2024_data = district_agg[
                (district_agg["Year"] == 2024) & (district_agg["StatisticGroup"] == crime_type)]
            sorted_districts = year_2024_data.sort_values("CrimeRate", ascending=False)["DistrictName"].tolist()

            fig_mini = px.bar(
                avg_crime_rate_by_district,
                y="DistrictName",
                x="CrimeRate",
                color="DistrictName",
                color_discrete_map=color_mapping,
                labels={"CrimeRate": "Average Crime Rate", "DistrictName": "District Name"},
            )

            fig_mini.update_layout(
                xaxis=dict(
                    title="Average Crime Rate",
                    tickformat=".2%",
                    title_font=dict(size=13),
                    tickfont=dict(size=12),
                    tickangle=45,
                ),
                yaxis=dict(
                    title="District Name",
                    tickmode="linear",
                    dtick=1,
                    title_font=dict(size=13),
                    tickfont=dict(size=12)
                ),
                title={
                    'text': "Average Crime Rate",
                    'x': 0.5,
                    'y': 0.69,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font': {'size': 14}
                },
                margin=dict(l=40, r=40, t=170, b=20),
                height=400,
                showlegend=False,
            )

            st.plotly_chart(fig_mini, use_container_width=True)

        with col2:
            if not filtered_data.empty:
                fig = px.line(
                    filtered_data,
                    x="Year",
                    y="CrimeRate",
                    color="DistrictName",
                    color_discrete_map=color_mapping,
                    category_orders={"DistrictName": sorted_districts},
                    labels={"CrimeRate": "Crime Rate (%)", "Year": "Year"},
                    title="Crime Rate by Year for Selected Districts and Crime Type",
                )

                fig.update_traces(line=dict(width=4))

                fig.update_layout(
                    title={
                        'text': "Crime Rate by Year for Selected Districts and Crime Type",
                        'font': {'size': 18},
                        'x': 0.5,
                        'xanchor': 'center',
                    },
                    legend=dict(title="Districts", font=dict(size=14)),
                    xaxis=dict(
                        title="Year",
                        tickmode="linear",
                        dtick=1,
                        title_font=dict(size=18),
                        tickfont=dict(size=16)
                    ),
                    yaxis=dict(
                        title="Crime Rate",
                        tickformat=".2%",
                        title_font=dict(size=18),
                        tickfont=dict(size=13)
                    ),
                    font=dict(size=25),
                    margin=dict(l=40, r=40, t=50, b=0),
                    height=400
                )

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

    # Default values
    default_crime = "All Crimes"
    default_rate = '5UnitsMathematicsRate'

    # Crime type selection
    crime_options = list(statistic_group_translation.values())
    default_crime_index = crime_options.index(default_crime)
    col1, col2 = st.columns(2)
    with col1:
        selected_crime = st.selectbox("Select Type of Crime", crime_options, index=default_crime_index)
    with col2:
        selected_rate = st.selectbox("Select Education Metric", list(education_translation.values()), index=3)

    # Reverse mappings
    reverse_crime_mapping = {v: k for k, v in statistic_group_translation.items()}
    reverse_rate_mapping = {v: k for k, v in education_translation.items()}
    selected_crime_column = reverse_crime_mapping.get(selected_crime, 'כל העבירות')
    selected_rate_column = reverse_rate_mapping.get(selected_rate, default_rate)

    # Filter and combine data
    filtered_crime = crime_data[crime_data['StatisticGroup'] == selected_crime_column]
    crime_summary = filtered_crime.groupby('DistrictName')['CrimeRate'].mean().reset_index()
    education_summary = education_data.groupby('DistrictName')[selected_rate_column].mean().reset_index()
    combined_data = pd.merge(crime_summary, education_summary, on='DistrictName', how='inner')

    # Apply district name translations
    combined_data['DistrictName'] = combined_data['DistrictName'].map(district_translation).fillna(combined_data['DistrictName'])

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
        hovertemplate=(f'<b>%{{x}}</b><br>{selected_crime}:<br>%{{y:.2f}}%<extra></extra>')
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
        hovertemplate=(f'<b>%{{x}}</b><br>{selected_rate}:<br>%{{y:.2f}}%<extra></extra>')
    ))

    # Update layout with translated labels
    fig.update_layout(
        barmode='group',  # Grouped bars
        xaxis={'title': {'text': 'District Name', 'font': {'size': 18}}, 'tickfont': {'size': 16}},
        yaxis={'title': {'text': 'Percentage', 'font': {'size': 18}}, 'tickfont': {'size': 16}},
        height=550,
        width=1300,
        margin={'l': 50, 'r': 50, 't': 80, 'b': 100},
        legend={'font': {'family': 'Arial', 'size': 13}}
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

    # Apply translation to the crime types
    crimes["StatisticGroup"] = crimes["StatisticGroup"].replace(statistic_group_translation)

    # Define Hebrew crime categories to remove
    hebrew_crime_categories = [
        "עבירות נגד אדם", "עבירות רשוי", "עבירות תנועה",
        "עבירות כלכליות", "סעיפי הגדרה", "שאר עבירות"
    ]

    # Filter out rows with these crime categories
    crimes = crimes[~crimes["StatisticGroup"].isin(hebrew_crime_categories)]

    # Define available crime types
    crime_types = crimes['StatisticGroup'].unique().tolist()
    default_crime_type = statistic_group_translation["כל העבירות"]  # "All Crimes" in Hebrew

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
            title="Crime Rate",
            title_font=dict(
                size=17,
            ),
            tickfont=dict(
                size=15,
            ),
            tickformat=".0%"  # Add the percentage sign to the ticks
        ),
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 10)),
            ticktext=list(range(1, 10)),  # Explicitly set x-axis labels
            title="Socio-Economic Group (1 to 9)",
            title_font=dict(
                size=17,
            ),
            tickfont=dict(
                size=15,
            )
        ),
        # Legend customization
        legend=dict(
            font=dict(
                size=15
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

    # Reverse the rate mapping to get the column names
    reverse_rate_mapping = {v: k for k, v in education_translation.items()}

    # Default selected rate
    default_rate = 'EligibleForBagrutRate'

    # Default crime type
    default_crime_type = "כל העבירות"

    # Define Hebrew crime categories to remove
    hebrew_crime_categories = [
        "עבירות נגד אדם", "עבירות רשוי", "עבירות תנועה",
        "עבירות כלכליות", "סעיפי הגדרה", "שאר עבירות"
    ]

    # Filter out rows with these crime names
    crimes = crimes[~crimes["StatisticGroup"].isin(hebrew_crime_categories)]

    # Add filters in one line using st.columns
    col1, col2 = st.columns(2)

    with col1:
        rate_filter = st.selectbox(
            "Select Education Rate:",
            options=list(education_translation.values()),
            index=list(education_translation.values()).index(education_translation[default_rate])
        )

    with col2:
        crime_type_filter = st.selectbox(
            "Select Crime Type:",
            options=[statistic_group_translation[ct] for ct in crimes['StatisticGroup'].unique().tolist()],
            index=[statistic_group_translation[ct] for ct in crimes['StatisticGroup'].unique().tolist()].index(statistic_group_translation[default_crime_type])
        )

    # Get the corresponding field names for selected filters
    selected_rate = reverse_rate_mapping.get(rate_filter, default_rate)
    selected_crime_type = next(key for key, value in statistic_group_translation.items() if value == crime_type_filter)

    # Prepare the data
    df_scatter = pd.merge(crimes, education_df, on='Settlement')
    df_scatter['CrimeRate'] = df_scatter['CrimeRate'].str.rstrip('%').astype(float) / 100  # Correct scaling

    # Filter the data for the selected education rate and crime type
    df_scatter = df_scatter[
        (df_scatter['StatisticGroup'] == selected_crime_type) &
        (df_scatter['Year'] == 2023) &
        df_scatter[selected_rate].notna() &
        (df_scatter['SocioeconomicGroup'] < 10) 
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
        labels={selected_rate: education_translation[selected_rate], "CrimeRate": "Crime Rate (%)"},
    )

    # Update the layout to show percentages on both axes
    fig4.update_layout(
        xaxis=dict(
            title=education_translation[selected_rate],
            title_font=dict(size=18),
            tickfont=dict(size=14),
            tickformat=".1%"
        ),
        yaxis=dict(
            title="Crime Rate",
            title_font=dict(size=18),
            tickfont=dict(size=14),
            tickformat=".1%"
        ),
        legend=dict(
            title="Socio-Economic Group",
            title_font=dict(size=16, color="black"),
            font=dict(size=12, color="black"),
            tracegroupgap=9
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        width=1200,
        height=500
    )

    # Display the chart
    st.plotly_chart(fig4)








if __name__ == "__main__":
    main()
