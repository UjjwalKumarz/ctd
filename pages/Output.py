import streamlit as st
from streamlit_pills import pills
from prompts import PROMPTS
from weasyprint import HTML
from bs4 import BeautifulSoup


if "output" not in st.session_state:
    st.session_state.output = ""
if "final" not in st.session_state:
    st.session_state.final = {}

st.subheader("Convert generated data to PDF")
if "subparts" in st.session_state:
    selected_subpart = pills("Select the subpart:", list(st.session_state.subparts.keys()), index = None)
    if selected_subpart:
        selected_response = pills("Choose any one response among these:", st.session_state.subparts[selected_subpart], format_func=lambda x:x.get_text(), index = None) 
        if selected_response:
            st.session_state.final[selected_subpart] = selected_response

output_path = st.text_input("Provide the output path")
if output_path and st.button("Create pdf file"):
    with st.spinner('Preparing output data...'):
        for subpart in st.session_state.final:
            if st.session_state.final[subpart]:
                st.session_state.output += st.session_state.final[subpart].prettify() + "\n"

        title = PROMPTS[st.session_state["req_mod"]]['title']
        code = f'''<!DOCTYPE html>
            <html>
            <head>
                <title>Critical Features of Study Design</title>
            </head>
            <body>

            <h2>{title}</h2>

            {st.session_state.output}
            </body>
            </html>'''
    with st.spinner('Converting to html file...'):
        # Path to save the HTML file
        html_file_path = st.session_state.output_path + '.html'

        # Write HTML code to file
        with open(html_file_path, 'w') as html_file:
            html_file.write(code)
        pdf_output_path = st.session_state.output_path + '.pdf'
    with st.spinnner('Generating PDF...'):
        # Convert HTML to PDF
        HTML(html_file_path).write_pdf(pdf_output_path)
        st.success("Pdf file generated successfully")


