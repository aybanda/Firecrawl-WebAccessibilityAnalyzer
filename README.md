# Web Accessibility Analyzer

## Description

The Web Accessibility Analyzer is a Streamlit-based web application that helps developers and content creators assess the accessibility of their websites. It uses the Firecrawl API to fetch web content and analyzes it for common accessibility issues, providing visual feedback and references to relevant Web Content Accessibility Guidelines (WCAG).

## Features

- Analyzes websites for common accessibility issues:
  - Missing alt text for images
  - Potential low contrast issues
  - Missing lang attribute on the html tag
  - Empty links
  - Form inputs without labels
- Visualizes accessibility issues found
- Provides links to relevant WCAG guidelines
- Easy-to-use interface built with Streamlit

## Installation

1. Clone this repository:
   

2. Install the required dependencies:
   
   pip install -r requirements.txt
   ```

3. Set up your Firecrawl API key:
   - Create a .env` file in the project root
   - Add your Firecrawl API key to the `.env file:
     
     FIRECRAWL_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501`)

3. Enter a URL in the sidebar and click "Analyze Site"

4. View the accessibility analysis results, visualizations, and WCAG guidelines

## Dependencies

- streamlit
- pandas
- matplotlib
- seaborn
- firecrawl
- python-dotenv
- beautifulsoup4
- requests

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Firecrawl](https://firecrawl.com/) for providing the web scraping API
- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework
- [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/) for providing accessibility standards

## Disclaimer

This tool provides a basic accessibility analysis and should not be considered a comprehensive accessibility audit. For a thorough evaluation, please consult with accessibility experts and conduct manual testing.
