Whats NostraPredict? 
    "NostraPredict" Has been derived from two words, "Nostradamus" and "Predict",
      Nostradamus was a French astrologer, physician, and reputed seer. Whats a SEER? well thats basicall someone who can predict the future(Like the one in VIKINGS)
    (And trust me, I didn't use GPT for this)
   

This is my first ever actual project, and its a work in progress(So is my ML Knowledge) Housing data prediction is a classic ML problem and I felt that this would be a good start in my journey.

ABOUT THE PROJECT's CURRENT STATE:
  ~ Currently, I've successfully implemented Linear Regression and Polynomial Regression on my model, however, the R2_Score for both is low which is a clear indication that Linear Regression cannot suffice
    As Housing prices depend on multiple factors.

PREVIEW OF "housing.csv:
  ~Housing prices is the first column followed Area, Bathrooms...Furnishing status. 
   Apart from numerical values, we have Yes/No (Which can be converted to Binary) and for furnishing status,
    There are three values, Furnished, Semi-Furnished and Unfurnished.
    
WHAT NEEDS TO BE DONE:
  ~As I highlighted above, Linear regression alone isn't enough, the price depends on 12 Factors in total, 
   So multiple regression would be the way to go.
  ~For Furnishing Status, I'll implement both, a binary approach by assigning values to the three furnishing statuses
   and ONE-HOT matrix approach, as that would be used in models that are more complex in the future.
  ~After the Rough implementation, I will be using the Sklearn libraries more to proceed further.
  
