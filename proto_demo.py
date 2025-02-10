import streamlit as st

# Add the custom HTML banner with unsafe_allow_html
st.markdown("""
    <header>
      <div style="width:100vw; height:8vh; background-color:red; border-bottom:3px solid yellow; text-align:left; padding:4px;">
        <span style="color:white; font-size:30px;">Wells Fargo</span>
      </div>
    </header>
    """, unsafe_allow_html=True)

# Set the background color of the page to white
st.markdown("""
    <style>
    body {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Chatbot UI
st.title("Chatbot UI")
st.write("Hello! I'm your assistant. How can I help you today?")

# Create a simple input box for the user to type their message
user_input = st.text_input("Your message:")

# Display the user's message and a placeholder response
if user_input:
    st.write(f"**You:** {user_input}")
    st.write("**Chatbot:** I'm still learning to respond. Stay tuned!")
