## 1. Title and Author

**Project Title:** IPL Score Prediction

Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

**Author Name:** Jaspreet Singh Bhatia

**GitHub:** https://github.com/jaspreet007singh

**LinkedIn:** https://www.linkedin.com/in/jsbhatia7/

**PowerPoint presentation file:**

**Link to your YouTube video:** 
    
## 2. Background

**What is the Project about?**

The IPL Score Prediction project is an exciting endeavor that harnesses the power of data analytics and machine learning to forecast the outcomes of cricket matches in the Indian Premier League (IPL). In a cricket-crazy nation like India, where the IPL is a sporting phenomenon, this project aims to provide cricket enthusiasts and sports enthusiasts with a valuable tool to anticipate the scores of upcoming matches. By analyzing historical data, team performance, player statistics, and various other factors, this project seeks to offer accurate and insightful predictions, enhancing the excitement and engagement surrounding IPL matches. It blends technology and sports passion to bring fans closer to the heart of the game.


**Why does it matter?**

The IPL Score Prediction project matters significantly for several reasons. Firstly, it adds an extra layer of excitement and engagement for cricket fans by allowing them to make informed predictions about match outcomes. This enhances the overall viewing experience and fosters a sense of participation.

Moreover, from a sports analysis perspective, it can provide valuable insights into team strategies, player performances, and the impact of various factors on match results. These insights can be used by cricket teams, coaches, and analysts to make data-driven decisions and improve their game.

Additionally, it showcases the practical applications of data analytics and machine learning in the world of sports, highlighting their relevance and potential in various industries beyond cricket. Overall, the IPL Score Prediction project matters as it enriches the fan experience, informs sports strategy, and demonstrates the power of data-driven decision-making.



**What are your research questions?**


I am going to build a machine learning model for predicting the score of the first innings in an IPL match . I am also checking if we can get correct observation if we include the powerplay overs in account.

## 3. Data 

**Describe the datasets you are using to answer your research questions:**

**Data sources:** - https://cricsheet.org/downloads/

**Data size (MB, GB, etc.):** - 9.2 Mb

**Data shape (# of rows and # columns) :** - (76014, 15) i.e. 76014 rows × 15 columns

**Time period:** - 2008-2017

**What does each row represent?** 

- Each row represents the values of 15 different columns in which 9 are numerical and 6 are categorical.

**Data dictionary:**

- **mid**
  - Data type: Numerical (Integer)
  - Definition: Each match is given a unique number.
  - Potential values: 1-617

- **date**
  - Data type: Categorical
  - Definition: When the match happened.
  - Potential values: Date

- **Venue**
  - Data type: Categorical
  - Definition: Stadium where match is being played.
  - Potential values: String values like "M Chinnaswamy Stadium" and so on.
 
- **bat_team**
  - Data type: Categorical
  - Definition: Batting team name.
  - Potential values: String values like "Mumbai Indians" and so on.

- **bowl_team**
  - Data type: Categorical
  - Definition: Bowling team name.
  - Potential values: String values like "Chennai Super Kings" and so on.

- **batsman**
  - Data type: Categorical
  - Definition: Batsman name who faced that ball.
  - Potential values: String values like "MS Dhoni" and so on.

- **bowler**
  - Data type: Categorical
  - Definition: Bowler who bowled that ball.
  - Potential values: String values like "Jasprit Bumrah" and so on

- **runs**
  - Data type: Numerical (Integer)
  - Definition: Total runs scored by team at that instance.
  - Potential values: 0-263

- **wickets**
  - Data type: Numerical (Integer)
  - Definition:  Total wickets fallen at that instance.
  - Potential values: 0-10

- **overs**
  - Data type: Numerical (Float)
  - Definition:  Total overs bowled at that instance.
  - Potential values: 0.0-19.6

- **runs_last_5**
  - Data type: Numerical (Integer)
  - Definition: Total runs scored in last 5 overs.
  - Potential values: 0-113

- **wickets_last_5**
  - Data type: Numerical (Integer)
  - Definition: Total wickets that fell in last 5 overs.
  - Potential values: 0-7

- **Striker**
  - Data type: Numerical (Integer)
  - Definition: max(runs scored by striker, runs scored by non-striker)
  - Potential values: 0-175

- **non-striker**
  - Data type: Numerical (Integer)
  - Definition: min(runs scored by striker, runs scored by non-striker).
  - Potential values: 0-109

- **Total**
  - Data type: Numerical (Integer)
  - Definition: Total runs scored by batting team after first innings.
  - Potential values: 67-263



**Which variable/column will be your target/label in your ML model?**
-	Total

**Which variables/columns may be selected as features/predictors for your ML models?**
 - runs
 - wickets
 - overs
 - striker
 - non-striker
