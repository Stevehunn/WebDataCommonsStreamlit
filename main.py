import streamlit as st
from streamlit_option_menu import option_menu

from allDataDisplay import content_all_data_display
# Import Content Page
from comparison import content_comparison
from dataCount import data_count
from delete import content_delete_svg
from parse import get_plot_name, get_name_from_json
from welcome import content_welcome
from year2022 import content_2022
from year2023 import content_2023


def main():
    # Custom CSS
    custom_css = """
    <style>
        /* Your custom CSS goes here */
       [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
        }
        .st-emotion-cache-1y4p8pa {
            max-width: 95%
        }
    </style>
    """

    # Init data
    target_classes = []
    target_classes_available_after = []
    target_classes_available_before = []

    get_plot_name(target_classes)
    get_name_from_json(target_classes_available_after, "after")
    get_name_from_json(target_classes_available_before, "before")

    # Data before
    data_plotly_sunburst_before = data_count(False, "Before")
    data_plotly_treemap_before = data_count(True, "Before")

    # Data after
    data_plotly_sunburst_after = data_count(False, "After")
    data_plotly_treemap_after = data_count(True, "After")

    # Display custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    st.sidebar.title("Here you can navigate through the demo")
    with st.sidebar:
        selected_tab = option_menu(
            menu_title="Summary",
            options=["Welcome page", "Data from 2022", "New Data from 2023", "Comparison between the two dataset",
                     "Evolution of data per Type"],
        )
        if st.button("Delete previous Upsetplot", type="primary"):
            content_delete_svg()
            st.write("Previous Upsetplot remove")
    if selected_tab == "Welcome page":
        content_welcome()
    if selected_tab == "Data from 2022":
        content_2022(data_plotly_sunburst_before, data_plotly_treemap_before, target_classes_available_before)
    if selected_tab == "New Data from 2023":
        content_2023(data_plotly_sunburst_after, data_plotly_treemap_after, target_classes_available_after)
    if selected_tab == "Comparison between the two dataset":
        content_comparison(target_classes_available_before)
    if selected_tab == "Evolution of data per Type":
        content_all_data_display()


# Run the app
if __name__ == '__main__':
    main()
