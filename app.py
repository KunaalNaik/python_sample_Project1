import pandas as pd
import streamlit as st

# AgGrid
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# Streamlit Configuration
st.set_page_config(layout="wide")

# Title and Heading
st.title('US Clinical Trials')
st.subheader('Extract and Compare Clinical trials information')

# Functions


@st.cache
def data_upload():
    df = pd.read_csv('input/input_nct_ids.csv')
    return df


# Side Bar Code
with st.sidebar:
    st.write("Analyse NCT Id's")
    uploaded_nct_ids = st.sidebar.file_uploader('Upload')

    input_nct_ids = data_upload()
    st.dataframe(data=input_nct_ids)




# Main Area Code

# Import the latest Tables to Display (input folder)
tbl_studies = pd.read_csv('data/studies.csv', infer_datetime_format=True)
tbl_countries = pd.read_csv('data/countries.csv')
tbl_interventions = pd.read_csv('data/interventions.csv')


# Display Tables
tab1, tab2, tab3 = st.tabs(["Studies", "Countries", "Interventions"])

with tab1:
    st.header("Studies")
    gd = GridOptionsBuilder.from_dataframe(tbl_studies)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=True, groupable=True)

    # sel_mode = st.radio('Selection Type', options=['single', 'multiple'])
    # gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
    gridOptions = gd.build()
    AgGrid(tbl_studies)

with tab2:
    st.header("Countries")
    AgGrid(tbl_countries)

with tab3:
    st.header("Interventions")
    AgGrid(tbl_interventions)

