import streamlit as st
from engine import FashionEngine
import os
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="StyleSense Pro | GenAI Fashion Platform",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# Initialize Engine
engine = FashionEngine()

# Sidebar - User Preferences
st.sidebar.title("🎨 Style Profile")
st.sidebar.markdown("---")

gender = st.sidebar.selectbox("Gender", ["Men", "Women", "Unisex", "Non-binary"])
age = st.sidebar.select_slider("Age Group", options=["Gen Z", "Millennial", "Gen X", "Classic"])
occasion = st.sidebar.selectbox("Occasion", ["Casual", "Formal", "Business", "Date Night", "Party", "Vacation"])
style = st.sidebar.multiselect("Preferred Styles", ["Minimalist", "Bohemian", "Streetwear", "Vintage", "Preppy", "Gothic"])
budget = st.sidebar.select_slider("Budget Level", options=["Budget", "Mid-Range", "Premium", "Luxury"])

st.sidebar.markdown("---")
st.sidebar.info("Upload your photo in the 'Style Analysis' tab for visual recommendations.")

# Main UI
st.title("✨ StyleSense Pro")
st.markdown("### Your Personal AI Fashion Stylist")

tabs = st.tabs(["🎯 Recommendations", "🔍 Style Analysis", "📈 Trend Insights"])

# Tab 1: Recommendations
with tabs[0]:
    st.header("Personalized Outfit Suggestions")
    if st.button("Generate My Outfits"):
        with st.spinner("Styling your perfect look..."):
            prefs = {
                "gender": gender,
                "age": age,
                "occasion": occasion,
                "style": ", ".join(style),
                "budget": budget
            }
            results = engine.get_recommendations(prefs)
            st.markdown(f'<div class="style-card">{results}</div>', unsafe_allow_html=True)

# Tab 2: Style Analysis
with tabs[1]:
    st.header("Visual Style Analysis")
    uploaded_file = st.file_uploader("Upload an outfit or item photo", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 1])
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Insight", use_container_width=True)
            
            # Save temp file for engine
            with open("temp_upload.png", "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        with col2:
            st.subheader("Stylist Analysis")
            if st.button("Analyze My Style"):
                with st.spinner("Analyzing visually..."):
                    analysis = engine.analyze_image("temp_upload.png")
                    st.markdown(f'<div class="style-card">{analysis}</div>', unsafe_allow_html=True)

# Tab 3: Trend Insights
with tabs[2]:
    st.header("Global Fashion Trends")
    if st.button("Fetch Latest Trends"):
        with st.spinner("Scouting the runways..."):
            trends = engine.get_trend_insights()
            st.markdown(f'<div class="style-card">{trends}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #a29bfe;">Created with ❤️ by StyleSense Pro AI</div>',
    unsafe_allow_html=True
)
