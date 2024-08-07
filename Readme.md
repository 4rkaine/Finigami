# Sentiment Analysis for Financial News

Trained the DistilBERT model on the Financial Phrase Bank Data set for Sentiment Analysis. Exposed via a FLASK API. 

## File Structure:
    Root
      |
      |
      |- Readme.md                - You are here
      |- Sentences_xxxAgree.txt   - Dataset files
      |- LLM_Submission.ipynb     - Main Submission Nootebook, containing EDA, pre-processing, model training, Evaluation and API testing
      |- flaskapp.py              - Contains Flask API exposing model
      |- README.txt               - Readme for the data set
      |- License.txt              - Dataset license
      |- requirements.txt         - Required Python libraries to run file 
      |                                 (Note: If you only want to test the API, only ```pip install flask``` is needed)
      |
      |- model_save               - Contains weights and config for the tokenizer and pytorch model

## How to run:

### Complete Notebook including EDA, model training and evaluation:
    1. Open terminal at root folder
    2. Install dependencies ```pip install -r requirements.txt```
    3. Notebook should run smoothly

### Using the API
    1. Install dependencies ```pip install flask``` (Note: Not required if already completed section above)
    2. Run server ```python flaskapp.py```
    3. In the jupyter notebook, under Test API (at the bottom) you can see 10 examples using news excerpts from 6th Aug
    
    Feel free to use your own text to test out the API

## Model Performance Evaluation
    The model used here, achieves an accuracy of 95%. Precision and Recall hover around 85-99%, and the F1 score is between 90-98% for each sentiment.

    The most important metric here is the f1 score. While accuracy quantifies how many predictions were correct, the f1 score is a measure of precision and recall of the model. Here, the f1 score is very high for the neutral class, and fairly high for positves and negatives. This is to be expected as the training data is imbalanced.

        Precision measures how many predicted positives were true positives
        Recall measures how many true positives were correctly predicted

    These are the 2 metrics most important in classification problems, as they ensure the model will be truly accurate when faced with unseen data.