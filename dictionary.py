import streamlit as st

# ===============================
# Project Team (Group Members)
# ===============================
st.sidebar.title("Project Team")
st.sidebar.write("""
**English:** Seyi  
**Yoruba:** Aisha  
**French:** Daniel  
**Spanish:** Maria  
**German:** John  
""")

# ===============================
# Dictionary Data
# ===============================
translations = {
    "hello": {
        "English": "Hello",
        "Yoruba": "Bawo",
        "French": "Bonjour",
        "Spanish": "Hola",
        "German": "Hallo"
    },
    "thank you": {
        "English": "Thank you",
        "Yoruba": "E se",
        "French": "Merci",
        "Spanish": "Gracias",
        "German": "Danke"
    },
    "good morning": {
        "English": "Good morning",
        "Yoruba": "E kaaro",
        "French": "Bonjour",
        "Spanish": "Buenos días",
        "German": "Guten Morgen"
    },
    "please": {
        "English": "Please",
        "Yoruba": "Jowo",
        "French": "S'il vous plaît",
        "Spanish": "Por favor",
        "German": "Bitte"
    },
    "sorry": {
        "English": "Sorry",
        "Yoruba": "Ma binu",
        "French": "Désolé",
        "Spanish": "Lo siento",
        "German": "Entschuldigung"
    }
}

# ===============================
# App UI
# ===============================
st.title("🌍 Multi-Language Dictionary")

# Search bar
word = st.text_input("Enter a word to translate:")

# Dropdown menu
language = st.selectbox(
    "Choose language:",
    ["English", "Yoruba", "French", "Spanish", "German"]
)

# Action button
if st.button("Translate"):
    if word.lower() in translations:
        result = translations[word.lower()][language]
        st.success(f"Translation: **{result}**")
    else:
        st.error("Word not found in dictionary")

# Footer
st.caption("Group project — built with Python & Streamlit")
