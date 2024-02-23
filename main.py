import streamlit as st


def main():
    table_display_cols = st.columns([1, 3, 1])
    with table_display_cols[1]:
        with st.container(border=True):
            row_cols = st.columns(3)
            with row_cols[0]:
                # set a key so the text_inputs don't clash and
                # we can access them later if necessary
                user_number = st.number_input(
                    '', value=100.0, step=0.1,
                    label_visibility='collapsed')


if __name__ == '__main__':
    main()
