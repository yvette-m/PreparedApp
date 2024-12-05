## PREPARED Home Safety Advisor

### Context
Los Angeles is particularly vulnerable to the destructive effects of wildfires, flooding, mudslides, earthquakes, and extreme heat, making emergency preparedness a critical need for families in the area .

### Project Overview
The PREPARED Home Safety Advisor educates families on the fundamentals of emergency and disaster planning, determines their current level of preparedness, provides personalized safety recommendations and risk assessments, and facilitates easy ordering of the products necessary to bring families to their desired level of preparedness. All recommendations are customized to their household location and basic demographics.

### File Order
1. [Clean_LA_Hazard_Dataset_&_Create_Text_Corpus.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/Clean_LA_Hazard_Dataset_%26_Create_Text_Corpus.ipynb)
2. [FEMA_Census_Tract_Cleaning.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/FEMA_Census_Tract_Cleaning.ipynb)
4. [FEMA_Data_Sentences_Merged_with_LA_County_Hazard_Data_Sentences.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/FEMA_Data_Sentences_Merged_with_LA_County_Hazard_Data_Sentences.ipynb)
5. [Localapp.py](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/Localapp.py)
6. [OllamaRemoteHost.ipynb](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/OllamaRemoteHost.ipynb)
7. [requirements.txt](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/requirements.txt)
8. [Remoteapp.py](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/Remoteapp.py)
9. [app.py](https://github.com/PREPARED-AI-Studio-Project/PREPARED-Project/blob/main/app.py)

### Model Installation Instruction
**Local App Installation Instructions**  

**Download Required Files**  
Ensure the following files are downloaded to the same folder on your computer:  

Localapp.py  
Prepared_data.txt  
amazon_link.csv  
requirements.txt  

**Install Required Dependencies**  
Open a terminal in the folder containing the files and run the following command to install dependencies:  
"pip install -r requirements.txt"  

**Run the App**  
Start the app by running the following command in the terminal:  
"streamlit run Localapp.py"  


**Remote App Installation Instructions**  

**Download Required Files**  
Ensure the following files are downloaded to the same folder on your computer:  

Remoteapp.py  
OllamaRemoteHost.ipynb  
Prepared_data.txt  
amazon_link.csv  
requirements.txt  

**Set Up ngrok** (optional - recommended for security purposes)  

Create a free ngrok account at ngrok.com.  
After creating your account, generate an authentication token.  
Replace the existing authentication token in the OllamaRemoteHost.ipynb file with your own token.  

**Run the Ollama Host**  

Open the OllamaRemoteHost.ipynb file in Google Colab and run the cells step by step.  
This will:  
Download the Ollama model onto Google Colab’s host.  
Launch Ollama with the Mistral model running.  
Once the notebook runs successfully, ngrok will generate a public URL for the Ollama instance.  

**Update the Public URL**  

Copy the ngrok public URL generated in the previous step.  
Open the Remoteapp.py file and replace the placeholder URL with the one you just copied.  

**Deploy on GitHub and Streamlit**  

Upload the following files to a GitHub repository:  

Remoteapp.py  
OllamaRemoteHost.ipynb   
Prepared_data.txt  
amazon_link.csv  
requirements.txt  
Connect your GitHub repository to Streamlit's Community Cloud (streamlit.io).  
Streamlit will automatically detect your changes and deploy the app.  

#### Contributors: Yvette Roos, Keta Patel, Glenvelis Perez, Sukanya Iyer, Ula Nguyen <br>
**Challenge Advisors**: Billy Zimmer & Andre Fonseca <br>
**AI Studio TA**: Swathi Senthil <br>
Break Through Tech AI @ MIT <br>
Fall 2024
