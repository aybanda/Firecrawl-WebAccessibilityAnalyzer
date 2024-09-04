import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# Load environment variables
load_dotenv()

# Initialize FirecrawlApp with the API key
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')
firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)

# Set up the Streamlit app
st.title('Web Accessibility Analyzer')

# Sidebar for user input
st.sidebar.header('User Input')
url = st.sidebar.text_input('Enter URL to analyze:')
analyze_button = st.sidebar.button('Analyze Site')

def analyze_accessibility(url):
    result = firecrawl_app.scrape_url(url, params={'formats': ['html']})
    html_content = result.get('html', '')
    soup = BeautifulSoup(html_content, 'html.parser')
    
    accessibility_issues = {
        'missing_alt_text': 0,
        'low_contrast': 0,
        'missing_lang': 0,
        'empty_links': 0,
        'missing_labels': 0
    }
    
    # Check for images without alt text
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            accessibility_issues['missing_alt_text'] += 1
    
    # Check for potential low contrast (simplified check)
    styles = soup.find_all('style')
    for style in styles:
        if 'color:' in style.text and 'background-color:' in style.text:
            accessibility_issues['low_contrast'] += 1
    
    # Check for missing lang attribute
    if not soup.html.get('lang'):
        accessibility_issues['missing_lang'] = 1
    
    # Check for empty links
    links = soup.find_all('a')
    for link in links:
        if not link.text.strip() and not link.find('img'):
            accessibility_issues['empty_links'] += 1
    
    # Check for form inputs without labels
    inputs = soup.find_all('input')
    for input_field in inputs:
        if not input_field.find_previous('label'):
            accessibility_issues['missing_labels'] += 1
    
    return accessibility_issues

def get_wcag_guidelines():
    url = "https://www.w3.org/WAI/WCAG21/quickref/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    guidelines = []
    for guideline in soup.select('.guideline'):
        title = guideline.select_one('.guideline-title').text.strip()
        link = urljoin(url, guideline.select_one('a')['href'])
        guidelines.append({'title': title, 'link': link})
    return guidelines

if analyze_button and url:
    with st.spinner('Analyzing site accessibility...'):
        try:
            results = analyze_accessibility(url)
            
            st.subheader('Accessibility Analysis Results')
            
            # Display results
            for issue, count in results.items():
                st.write(f"{issue.replace('_', ' ').title()}: {count}")
            
            # Visualize results
            fig, ax = plt.subplots()
            sns.barplot(x=list(results.keys()), y=list(results.values()), ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            ax.set_ylabel('Count')
            ax.set_title('Accessibility Issues')
            st.pyplot(fig)
            
            # Provide WCAG guidelines
            st.subheader('WCAG Guidelines for Reference')
            guidelines = get_wcag_guidelines()
            for guideline in guidelines[:5]:  # Display first 5 guidelines
                st.markdown(f"[{guideline['title']}]({guideline['link']})")
            
        except Exception as e:
            st.error(f"Error analyzing {url}: {str(e)}")

# Firecrawl API key status
st.sidebar.subheader('Firecrawl API Status')
if firecrawl_api_key:
    st.sidebar.success('Firecrawl API key is set')
else:
    st.sidebar.error('Firecrawl API key is not set')
