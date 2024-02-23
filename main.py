import streamlit as st


def main():
    table_display_cols = st.columns([1, 3, 1])
    with table_display_cols[1]:
        with st.container(border=True):
            user_number = st.number_input('This is a number input')


if __name__ == '__main__':
    main()
