# PREPARED Home Safety Advisor

## Table of Contents
1. [Project Overview](#project-overview)
    - [Context](#context)
    - [Goals](#goals)
2. [File Order](#file-order)
3. [Model Installation Instruction](#model-installation-instruction)
    - [Local App Installation](#local-app-installation-instructions)
    - [Remote App Installation](#remote-app-installation-instructions)
4. [Methodology](#methodology)
    - [Data Collection and Preprocessing](#data-collection-and-preprocessing)
    - [Model Development](#model-development)
5. [Findings and Challenges](#findings-and-challenges)
6. [Future Steps](#future-steps)

## Project Overview
The PREPARED Home Safety Advisor is a chatbot-driven platform designed to educate families about emergency and disaster planning, assess their current level of preparedness, and provide personalized safety recommendations and risk assessments. It facilitates easy ordering of essential products to bring families to their desired level of preparedness, with recommendations tailored to their household location and demographics.

### Context
Initially focused on California—specifically Los Angeles County—this project addresses the unique challenges posed by natural disasters such as wildfires, flooding, mudslides, earthquakes, and extreme heat. Los Angeles County is particularly vulnerable to these events, yet many families lack the knowledge or resources to prepare effectively.

While the project started with data specific to LA County, the integration of Ollama and large language models (LLMs) has enabled us to expand the chatbot’s capabilities to cover users nationwide. However, the chatbot remains most specific and accurate for LA County, as this region forms the core of our training dataset.

### Goals
- Educate families about the fundamentals of emergency and disaster planning.
- Determine levels of preparedness through assessments and risk evaluations.
- Provide personalized recommendations for products and practices to improve safety.

## File Order
1. [Clean_LA_Hazard_Dataset_&_Create_Text_Corpus.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/Clean_LA_Hazard_Dataset_%26_Create_Text_Corpus.ipynb)
2. [FEMA_Census_Tract_Cleaning.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/FEMA_Census_Tract_Cleaning.ipynb)
3. [FEMA_Data_Sentences_Merged_with_LA_County_Hazard_Data_Sentences.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/FEMA_Data_Sentences_Merged_with_LA_County_Hazard_Data_Sentences.ipynb)
4. [Localapp.py](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/Localapp.py)
5. [OllamaRemoteHost.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/OllamaRemoteHost.ipynb)
6. [requirements.txt](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/requirements.txt)
7. [Remoteapp.py](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/Remoteapp.py)
8. [app.py](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/app.py)

## Model Installation Instruction
### Local App Installation Instructions

1. **Download Required Files**  
Ensure the following files are downloaded to the same folder on your computer:  

- Localapp.py  
- Prepared_data.txt  
- amazon_link.csv  
- requirements.txt  

2. **Install Required Dependencies**  
Open a terminal in the folder containing the files and run the following command to install dependencies:  ```pip install -r requirements.txt``` 

3. **Run the App**  
Start the app by running the following command in the terminal:  ``` streamlit run Localapp.py  ```


### Remote App Installation Instructions

1. **Download Required Files**  
Ensure the following files are downloaded to the same folder on your computer:  

- Remoteapp.py  
- OllamaRemoteHost.ipynb  
- Prepared_data.txt  
- amazon_link.csv  
- requirements.txt  

2. **Set Up ngrok** (optional - recommended for security purposes)  

Create a free ngrok account at ngrok.com.  After creating your account, generate an authentication token.  Replace the existing authentication token in the OllamaRemoteHost.ipynb file with your own token.  

3. **Run the Ollama Host**  

Open the OllamaRemoteHost.ipynb file in Google Colab and run the cells step by step.  This will:  
- Download the Ollama model onto Google Colab’s host.  
- Launch Ollama with the Mistral model running.  
- Once the notebook runs successfully, ngrok will generate a public URL for the Ollama instance.  

4. **Update the Public URL**  

Copy the ngrok public URL generated in the previous step.  Open the Remoteapp.py file and replace the placeholder URL with the one you just copied.  

5. **Deploy on GitHub and Streamlit**  

Upload the following files to a GitHub repository:  

- Remoteapp.py  
- OllamaRemoteHost.ipynb   
- Prepared_data.txt  
- amazon_link.csv  
- requirements.txt  

Connect your GitHub repository to Streamlit's Community Cloud (streamlit.io).  Streamlit will automatically detect your changes and deploy the app.  

## Methodology
### Data Collection and Preprocessing
The data for this project was provided by challenge advisors and included:

- LA Hazard Data
- Amazon Product Recommendations
- FEMA Hazards Data (by Census Tract)

**Steps in Data Preprocessing**:
 1. Data Cleaning: Removed empty rows and columns, handled missing values, and filled null entries with appropriate replacements.
 2. Feature Engineering: Applied one-hot encoding, value mapping, and merged datasets from FEMA and LA Hazards.
 3. Text Data Preparation:
    - Transformed tabular data into descriptive sentences.
    - Combined generated sentences into a single text corpus.
    - Prepared the corpus for fine-tuning the LLM.
  
### Model Development
**Tool Used**: Ollama, a free-to-download, locally runnable LLM framework. <br>
**Training Approach**: Fine-tuned the model on custom text corpora derived from the datasets.

## Findings and Challenges

### Findings
- The model provides great general advice and personalized recommendations.
- It effectively integrates technical data to generate advice tailored to LA County.

### Challenges
- **Specificity of User Questions**: The chatbot's ability to meet user needs depends on how specific the questions are, which we are still evaluating.
- **Data Complexity**: While the model incorporates technical data, it's unclear how well this translates into actionable advice for end users.
- **Maintenance Requirements**: The model will require regular updates to ensure its information remains accurate and relevant over time.
- **Computing Power Limitations**: Deploying the model for public use is challenging due to limited access to computing resources.

## Future Steps
- **User Authentication Integration**: Add support for Amazon or Google sign-in systems to personalize user experiences.
- **Database Development**: Build a secure database to store customer information, enabling users to revisit their chat history.
- **Nationwide Model Accuracy**: Enhance the model’s accuracy to cover a wider range of regions effectively.
- **Offline Accessibility**: Develop an offline version of the chatbot to ensure users can access it without internet connectivity.

### Contributors: Yvette Roos, Keta Patel, Glenvelis Perez, Sukanya Iyer, Ula Nguyen <br>
**Challenge Advisors**: Billy Zimmer & Andre Fonseca <br>
**AI Studio TA**: Swathi Senthil <br>
Break Through Tech AI @ MIT <br>
Fall 2024
