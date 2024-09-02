import streamlit as st 
st.title(" ")

st.sidebar.success("SELECT A PAGE ABOVE.")

with st.container():
    st.write("---")
    st.header("FEEDBACK😎")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/rahul.msc.mdu@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false"> 
     <input type="text" name="name" placeholder="Your Name " required>
     <input type="email" name="email" placeholder="Your Email " required>
     <textarea name="message" placeholder ="your message is here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

import streamlit as st

def load_local_css(file_path):
    """
    Load and apply local CSS styles to the Streamlit app.

    Args:
    - file_path (str): Path to the CSS file.

    Returns:
    - None
    """
    with open(file_path, "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

import streamlit as st

# Define CSS styles
st.markdown("""
    <style>
    /* Input fields and textarea */
    input[type=text], input[type=email], textarea {
        width: 100%; /* Full width */
        padding: 12px; /* Some padding */
        border: 1px solid #ccc; /* Gray border */
        border-radius: 4px; /* Rounded borders */
        box-sizing: border-box; /* Make sure that padding and width stay in place */
        margin-top: 6px; /* Add a top margin */
        margin-bottom: 16px; /* Bottom margin */
        resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
    }

    /* Style the submit button with a specific background color etc */
    input[type=submit] {
        background-color: #04AA6D;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    /* When moving the mouse over the submit button, add a darker green color */
    input[type=submit]:hover {
        background-color: #45a049;
    }

    /* Add a background color and some padding around the form */
    .container {
        border-radius: 5px;
        background-color: #f2f2f2;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.subheader("FEEL FREE TO CONTACT US")
    st.write("rahul.mdu@icloud.com")