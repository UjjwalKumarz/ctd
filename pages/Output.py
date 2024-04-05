import streamlit as st
from streamlit_pills import pills
from prompts import PROMPTS
# from weasyprint import HTML
import pdfkit
import base64
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
        html_file_path = '__pycache__/'+ st.session_state.output_path + '.html'

        # Write HTML code to file
        with open(html_file_path, 'w') as html_file:
            html_file.write(code)
        pdf_output_path = st.session_state.output_path.strip() + '.pdf'
    with st.spinnner('Generating PDF...'):
        try:
            pdfkit.from_file(html_file_path, pdf_output_path, configuration=config)
            # Read the generated PDF file as bytes
            with open(pdf_output_path, "rb") as f:
                pdf_bytes = f.read()
            st.success("PDF file generated. Click on 'Download PDF' to save.")
            # Provide download link for the PDF file
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="{pdf_output_path}">Download PDF file</a>'
            st.markdown(href, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"PDF file generation failed. Error: {e}")
        
        # # Convert HTML to PDF
        # # HTML(html_file_path).write_pdf(pdf_output_path)
        # pdfkit.from_file(html_file_path, pdf_output_path, configuration=config)
        # # download the PDF file
        # if pdf_bytes is not None:
        #     st.success("PDF file Generated. Click on 'Download PDF' to save.")
        #     b64 = base64.b64encode(pdf_bytes).decode()
        #     href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF file</a>'
        #     st.markdown(href, unsafe_allow_html=True)
        #     # remove the success message and download link
        #     st.empty()
        # else:
        #     st.warning("PDF file generation failed. Please try again.")

        
        st.success("Pdf file downloaded successfully")


