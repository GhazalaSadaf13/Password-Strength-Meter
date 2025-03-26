import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    
    # Length Check
    if len(password) >= 8:
        strength += 1
    
    # Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1
    
    # Number Check
    if re.search(r"[0-9]", password):
        strength += 1
    
    # Special Character Check
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    
    # Determine Strength Level
    if strength == 1:
        remarks = "Very Weak"
    elif strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 5:
        remarks = "Very Strong"
    
    return strength, remarks

# Streamlit UI
st.title("Real-time Password Strength Indicator")
st.write("Enter a password to check its strength.")

password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks = check_password_strength(password)
    
    # Display strength level
    st.write(f"**Strength Level:** {remarks}")
    
    # Color Indicator
    if strength == 1:
        st.error("Very Weak Password")
    elif strength == 2:
        st.warning("Weak Password")
    elif strength == 3:
        st.info("Moderate Password")
    elif strength == 4:
        st.success("Strong Password")
    elif strength == 5:
        st.success("Very Strong Password")