# PressAgent: AI-Generated Press Kit

PressAgent is a Streamlit web application that generates AI-powered press kits for companies. The application fetches supplementary data, generates a press release, and reviews the press kit for quality.

## Features

- Fetches supplementary data based on the company name
- Generates a press release based on the company name and press kit topic
- Reviews the generated press kit for quality
- Allows users to download the generated press kit as a PDF

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/PressAgent.git
    cd PressAgent
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the company name and press kit topic, then click "Generate Press Kit".

4. The app will fetch supplementary data, generate the press release, and review the press kit.

5. The generated press kit and quality review will be displayed on the page.

## File Structure

- [main.py](http://_vscodecontentref_/0): The main Streamlit app file.
- [data_fetch.py](http://_vscodecontentref_/1): Contains the [fetch_supplementary_data](http://_vscodecontentref_/2) function to fetch supplementary data.
- [content_gen.py](http://_vscodecontentref_/3): Contains the [generate_press_release](http://_vscodecontentref_/4) function to generate the press release.
- [review_agent.py](http://_vscodecontentref_/5): Contains the [review_press_kit](http://_vscodecontentref_/6) function to review the press kit.
- [backend/pdf_creator.py](http://_vscodecontentref_/7): Contains the `generate_pdf` function to create a PDF file and integrate it with Streamlit for download.

## Example

1. Enter the company name and press kit topic:
    - Company Name: `Example Company`
    - Press Kit Topic: `New Product Launch`

2. Click "Generate Press Kit".

3. The app will display the generated press kit and quality review.

## Dependencies

- [streamlit](http://_vscodecontentref_/8)
- `reportlab`
- `PyPDF2`

## License

This project is licensed under the MIT License.
