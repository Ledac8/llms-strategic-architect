import streamlit as st

# Page configuration
st.set_page_config(page_title="LLM Strategic Architect", page_icon="🤖")

st.title("🤖 LLM Strategic Architect")
st.markdown("### Generate a GEO-optimized llms.txt file for your startup.")

# Input fields for the founder
company_name = st.text_input("Startup Name", placeholder="e.g. Acme AI")
site_url = st.text_input("Website URL", placeholder="https://acme.ai")
description = st.text_area("What does your startup do?", placeholder="Provide a brief, factual summary for AI agents.")

if st.button("Generate File"):
    if company_name and site_url and description:
        # Building the formatted text
        llms_text = f"# {company_name}\n\n"
        llms_text += f"> {description}\n\n"
        llms_text += "## Core Technical Specifications\n"
        llms_text += f"* Entity Type: Startup / Software Service\n"
        llms_text += f"* Primary Domain: {site_url}\n\n"
        llms_text += "## Answer First Documentation\n"
        llms_text += "### Feature: Core Value Proposition\n"
        llms_text += f"{description}\n"

        # Show the result in the UI
        st.success("Your llms.txt content is ready!")
        st.code(llms_text, language="markdown")

        # Download button
        st.download_button(
            label="Download llms.txt",
            data=llms_text,
            file_name="llms.txt",
            mime="text/plain"
        )
    else:
        st.error("Please fill in all fields to generate your file.")
