# Module 20 Report Template

## Overview of the Analysis
- For this analysis various techniques are used to train and evaluate a model based on loan risk.
- The dataset id from the historical lending activity from a peer-to-peer lending services company 


- The values to be predited from model were the `0` (healthy loan) and `1` (high-risk loan) labels 
- Following steps were performed :
   - Read the file `lending_data.csv`
   - Create the labels set `y` from the “loan_status” column, and then create the features `X` DataFrame from the remaining columns.
   - Split the data into training and testing datasets by using `train_test_split`.
   - Fit a logistic regression model by using the training data (`X_train` and `y_train`).
   - Evaluate the model’s performance by calculating  the accuracy score of the model, generating a confusion matrix and printing the classification report.
   - Repeat same process using Logistic Regression Model with Resampled Training Data


## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
    - The model performs well with accuracy of 99% overall. If we compare , it does well in predicting healthy loans with good recall and f-1 score. For high risk loans there is a room for improvement as it predicts with 85% precision which is also reflected by recall and f-1 scores.
    



* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
  - In comparison the model fit with oversampled data does well in accuracy although the precision is 95% . The recall and f1-scores for prediction of healthy loans is still better than high risks loans prediction as high recall correlates to a more comprehensive output and a low false negative rate.

## Summary

 - Model with oversampled data fit has good overall accuracy than the model 1 for prediction of both labels
 - If we look at the performance for the high risk loans predictions, it has high recall and f1 scores which means it is able to identify correctly the high risk loans than the model 1.
- Based on the above arguments Model 2 with oversampled data is preferred over model 1.
