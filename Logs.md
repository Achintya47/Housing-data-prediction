15-11-2024 1549 Hours
  Implemented Multiple regression on the housing prices. 4 Parameters have been used so far and the performance has increased. 
  The R2 Score for Linear Regression was around 0.2872931546811468 and for Polynomial Regression(degree 3) it was 0.32504534381488304

  For Multiple Regression, the R2 Score 0.5355960442835979 which shows that the multiple regression model is the most accurate so far

4-12-2024 2103 Hours
  Remapped the whole project using Pipeline feature from sklearn. Pipeline straeamlines the data so there is no need to individually Scale and Impute the data, Pipeline performs all the functions itself.
  The Mean_Absolute_Percentage_Error is 16% which is not that good. Further, now multiple regression techniques will be applied and I will be comparing the scores of each one individually to find the perfect model.

27-12-2024 1519 Hours
  I have started coding in Jupyter Notebook and have noticed its advantages. 
  The project has now been divided in two models, Linear Regression and KNearest Regressor, Initially I started with Linear Regression's further optimisation. First all the categorical data has now been encoded, 
  then using correlation matrix, I have further divided LR into two, one with all the independent variables and the other with the variables having highest correlation and the difference is minute.
  ![Correlation](https://github.com/user-attachments/assets/80043b08-86dc-4714-bb6b-3768ab4bff45)

  Then, I checked the skewness of the target variables "price" and it is skewed towards the left with a skew value of 1.2088998457878217.
  ![Skewness in Prices](https://github.com/user-attachments/assets/50d31c88-7adf-4e3b-8290-a10e2e03d329)

  To deal with this, I tool the log of the values and it drastically reduced my error but, what i didnt know that by taking log, the model's error's dimension is also reduced so the error was reduced due to that reason only.
  Now there's two more techniques left to be applied, PCA and 10-Fold Cross Validation.

  The second model is kNN regressor, for scaling and encoding, similar techniques were used. Since kNN is sensitive to data's scale, I scaled the independent variable's "Area" feature.
  Further I performed testing to find the best hyperparameter k that gives the lowest MAPE and the highest R2_SCORE and the value was around 5.  Scaling also helped in increasing the R2_SCORE significantly.
  
