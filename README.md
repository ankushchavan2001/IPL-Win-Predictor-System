# IPL-Win-Predictor-System

Title: IPL Match Win Prediction System

Introduction:
The IPL Match Win Prediction System is a comprehensive data-driven project aimed at predicting the winner of Indian Premier League (IPL) matches. Leveraging machine learning techniques and data preprocessing, this project offers insights into the factors influencing match outcomes and provides accurate predictions for future matches. By merging ball-by-ball data with detailed match information, preprocessing the dataset, and developing a predictive model, the system serves as a valuable tool for cricket enthusiasts, analysts, and betting enthusiasts seeking to make informed predictions about IPL match results.

Goal:
The primary goal of the IPL Match Win Prediction System is to develop a predictive model capable of accurately forecasting the winner of IPL matches. By analyzing past match data and extracting relevant features, the project aims to identify patterns and trends that correlate with match outcomes. Ultimately, the predictive model will enable users to input match parameters and obtain the win probability of each team, facilitating strategic decision-making and enhancing the overall IPL match experience.

Data Collection and Preprocessing:
The project begins with the acquisition of two datasets from Kaggle: one containing ball-by-ball data of each IPL match and another containing detailed match information such as city, toss result, and match winner. The datasets are merged based on match ID to create a comprehensive dataset for analysis.

Data preprocessing plays a crucial role in preparing the dataset for modeling. Key preprocessing steps include:

Grouping the match ID and innings and aggregating total runs scored in each inning.
Filtering rows where the Duckworth-Lewis method is not applied.
Standardizing team names and removing teams that are not currently playing in the IPL.
Selecting relevant columns such as match ID, city, winner, and total runs for further analysis.
Merging the dataset with ball-by-ball data to extract information about the second innings, including total runs, wickets, current run rate, and required run rate.
Observations:
During the data preprocessing phase, several insights and observations are revealed:

The total runs scored by each team in a match vary significantly, indicating the dynamic nature of IPL matches.
Filtering out matches where the Duckworth-Lewis method is not applied ensures the integrity of the dataset and avoids potential discrepancies in analysis.
Standardizing team names helps maintain consistency and clarity in the dataset, enhancing the accuracy of predictions.
Model Development and Evaluation:
Following data preprocessing, the project proceeds to model development and evaluation. A pipeline is created using column transformers to one-hot encode team names and apply logistic regression for classification. The dataset is split into training and testing sets to train the model and evaluate its performance.

Model evaluation metrics such as accuracy, precision, recall, and F1-score are used to assess the predictive accuracy of the model. The classification report provides detailed insights into the model's performance, including metrics for each class (team).

Conclusion:
The IPL Match Win Prediction System demonstrates the effectiveness of leveraging machine learning techniques and data preprocessing to predict IPL match outcomes. By analyzing historical match data and extracting relevant features, the project achieves accurate predictions and provides valuable insights into factors influencing match results. The predictive model developed in this project can be utilized for making informed decisions, strategic planning, and enhancing the overall IPL match experience for stakeholders. The integration of Streamlit enables users to interact with the system through a user-friendly web interface, obtaining win probabilities for their desired match scenarios. Further refinement and exploration can enhance the system's predictive capabilities and provide additional value to users.
Link of Web app- http://localhost:8501/
