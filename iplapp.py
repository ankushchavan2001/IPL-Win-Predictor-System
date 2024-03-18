import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Jaipur', 'Mumbai', 'Hyderabad', 'Centurion', 'Delhi', 'Nagpur',
       'Bangalore', 'Chennai', 'Chandigarh', 'Kolkata', 'Durban',
       'Johannesburg', 'Raipur', 'Cuttack', 'Ahmedabad', 'Dharamsala',
       'Cape Town', 'Visakhapatnam', 'Bengaluru', 'East London', 'Mohali',
       'Pune', 'Ranchi', 'Sharjah', 'Abu Dhabi', 'Indore',
       'Port Elizabeth', 'Kimberley', 'Bloemfontein']

pipe = pickle.load(open('iplpipe.pkl','rb'))

st.title('IPL Predictor')

# col1, col2 = st.beta_columns(2)
#
# with col1:
#     batting_team = st.selectbox('Select the batting team',sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select the bowling team',sorted(teams))

batting_team = st.selectbox('Select the batting team',sorted(teams))

bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

score = st.number_input('Score')

overs = st.number_input('Overs Completed')

wickets = st.number_input('Wickets fell')

if st.button('Predict Probability'):
    runs_left = target-score
    balls_left = 120- (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                             'city':[selected_city],'runs_left':[runs_left],
                             'balls_left':[balls_left],'wickets':[wickets],
                             'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + '-'+str(round(win*100))+'%')
    st.header(bowling_team + '-' + str(round(loss * 100)) + '%')