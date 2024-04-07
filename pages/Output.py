import streamlit as st
from streamlit_pills import pills
from prompts import PROMPTS
# from weasyprint import HTML
from bs4 import BeautifulSoup
from xhtml2pdf import pisa

def generate_pdf():
    if 'output' in st.session_state:
        st.session_state.output = ''
    st.session_state.generate = True

def convert_html_to_pdf(code, pdf_file):

    # Open the HTML file and read its content
    # try:
    #     with open(html_file, 'r', encoding='utf-8') as html_file:
    #         html_content = html_file.read()
    # except FileNotFoundError:
    #     print("HTML file not found.")
    #     return

    # Create PDF output file
    try:
        with open(pdf_file, 'wb') as pdf_file:
            # Convert HTML to PDF with custom CSS styles
            pisa_status = pisa.CreatePDF(code, dest=pdf_file)
    except Exception as e:
        print(f"Error occurred during PDF generation: {e}")
        return

    # Check if PDF generation was successful
    if pisa_status and pisa_status.err:
        print(f"PDF generation failed: {pisa_status.err}")
    else:
        print("PDF generated successfully!")

if "output" not in st.session_state:
    st.session_state.output = ""
if "final" not in st.session_state:
    st.session_state.final = {}
if 'generate' not in st.session_state:
    st.session_state.generate = False

st.subheader("Convert generated data to PDF")
if "subparts" in st.session_state:
    selected_subpart = pills("Select the subpart:", list(st.session_state.subparts.keys()), index = None)
    if selected_subpart:
        selected_response = pills("Choose any one response among these:", st.session_state.subparts[selected_subpart], format_func=lambda x:x.get_text(), index = None) 
        if selected_response:
            st.session_state.final[selected_subpart] = selected_response

output_path = st.text_input("Provide the output path")
st.session_state.output_path = output_path
st.button("Create pdf file", on_click=generate_pdf)
if output_path and st.session_state.generate:
    with st.spinner('Preparing output data...'):
        for subpart in st.session_state.final:
            if st.session_state.final[subpart]:
                st.session_state.output += st.session_state.final[subpart].prettify() + "\n"

        title = PROMPTS[st.session_state["req_mod"]]['title']
        code = '''<!DOCTYPE html>
            <html>
            <head>
                <title>Critical Features of Study Design</title>
                <style>
                    @page {
                        size: A4; /* Specify page size (e.g., A4, Letter, etc.) */
                        margin-top: 2cm; /* Specify top margin */
                        margin-right: 2cm; /* Specify right margin */
                        margin-bottom: 2cm; /* Specify bottom margin */
                        margin-left: 2cm;
                    }
                    body {
                        font-family: Arial, sans-serif; /* Specify font family */
                        font-size: 14px; /* Specify font size */
                    }
                    h2 {
                        font-size: 24px; /* Specify font size for headings */
                        font-weight: bold; /* Specify font weight */
                    }
                    h3 {
                        font-size: 20px; /* Specify font size for headings */
                        font-weight: bold;
                    }
                    p {
                        font-size: 14px; /* Specify font size for paragraphs */
                    }
                </style>
            </head>
            ''' + f'''
            <body>

            <h2>{title}</h2>

            {st.session_state.output}

            </body>
            </html>'''
    # with st.spinner('Converting to html file...'):
    #     # Path to save the HTML file
    #     html_file_path = st.session_state.output_path + '.html'

    #     # Write HTML code to file
    #     with open(html_file_path, 'w') as html_file:
    #         html_file.write(code)
    pdf_output_path = st.session_state.output_path + '.pdf'
    with st.spinner('Generating PDF...'):
        # Convert HTML to PDF
        convert_html_to_pdf(code, pdf_output_path)

        # HTML(html_file_path).write_pdf(pdf_output_path)
    
    st.success("Pdf file generated successfully")
