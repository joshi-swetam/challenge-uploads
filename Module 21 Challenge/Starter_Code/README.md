# deep-learning-challenge
## Analysis
The purpose of this model is to help develop a tool for nonprofit foundation Alphabet Soup to select the applicants for funding with the best chance of success in their ventures.Dataset is provided by the organization to create a binary classifier that can predict whether applicants will be successful if funded by Alphabet Soup.
## Steps
To achieve the purpose following steps were followed:

- After reading in the file as ```application_df ```and displaying the data, columns were displayed as follows  ```['EIN', 'NAME', 'APPLICATION_TYPE','AFFILIATION','CLASSIFICATION','USE_CASE', 'ORGANIZATION', 'STATUS','INCOME_AMT','SPECIAL_CONSIDERATIONS', 'ASK_AMT', 'IS_SUCCESSFUL']```
- Feature columns and target column ```IS_SUCCESSFUL``` were identified.
- Columns such as ```'EIN', 'NAME' ``` were dropped considering they do not provide information needed for further steps
- Number of unique values for each column were determined .
- For columns that have more than 10 unique values``` 'APPLICATION_TYPE','CLASSIFICATION'```, the number of data points for each unique value were determined and these were used to pick a cutoff point to bin "rare" categorical variables together in a new value, Other .
- ```pd.get_dummies(application_df)``` to encode categorical variables.
- The preprocessed data was split into a features array, X, and a target array, y.
- These arrays were used to train_test_split function to split the data into training and testing datasets as follows ```X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42,stratify = y)```.
- Scaled the training and testing features datasets by creating a StandardScaler instance, fitting it to the training data, then using the transform function
~~~scaler = StandardScaler()
X_scaler = scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
print(len(X_train_scaled))
~~~
## Compilation,Training and evaluation
- Neural network layers were created with different combinations and summary was generated
- Different layers with different neurons and activation methods were tried.
- It was noticed that using more neurons or using different activation methods in each layer did not improve the accuracy.
 - Adding more hidden layers did not result in any improvement.
 - Considering these factors one input layers, and one hidden layer and output were used with units 80,30 and 1 respectively and activation functions being relu, relu and sigmoid were finalized.
- Compilation of the model was done.

nn.compile(loss="binary_crossentropy",optimizer="adam", metrics=["accuracy"])

  - Finally model was trained and evaluated and results were saved in ```AlphabetSoupCharity.h5.```
  - Increasing the number of epoch did not lead to any significant improvement and therefore 100 was chosen.
  ~~~
  fit_model = nn.fit(X_train_scaled, y_train, epochs= 100, callbacks=[checkpoint])
  model_loss, model_accuracy = nn.evaluate(X_test_scaled,y_test,verbose=2)
  nn.save('AlphabetSoupCharity.h5')
  ~~~
  ## Summary
  - In summary, with lots of combinations, hits and trials there was no improvement in the accuray.
  - The max it could reach was only 73.0% which is not good enough for using this model and making predictions.
  - Use of another classifiers such as random forest model could lead to better results.
  - Another approach would be creating bins for ask amount columns as well and perform the steps again.
- Exploratory data analysis could also add to the value if we want to improve accuracy using this model.