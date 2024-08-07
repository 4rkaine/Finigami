from flask import Flask, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

app = Flask(__name__)

model_dir = './model_save/'
tokenizer = DistilBertTokenizer.from_pretrained(model_dir)
model = DistilBertForSequenceClassification.from_pretrained(model_dir)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    text = data['text']
    # print(text)
    
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    sentiment_map = {0: 'negative', 1: 'neutral', 2: 'positive'}
    predicted_sentiment = sentiment_map[predicted_class]
    
    return jsonify({'sentiment': predicted_sentiment})

if __name__ == '__main__':
    app.run(debug=True)