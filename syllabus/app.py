import streamlit as st

# List of subjects and corresponding file paths
subjects = {
    "Architecture": "architecture.md",
    "Data Structures": "DS.md",
    "Operating Systems": "os.md",
    "Mathematics": "maths.md",
    "C++": "cpluscplus.md"
}

# Sidebar for subject selection
st.sidebar.title("Syllabus")
subject = st.sidebar.selectbox("Choose a subject:", list(subjects.keys()))

# Read and display the selected subject's content
with open(subjects[subject], "r") as file:
    syllabus_content = file.read()

# Display the Markdown content in the sidebar
st.sidebar.markdown(syllabus_content, unsafe_allow_html=True)
