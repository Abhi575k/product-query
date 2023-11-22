# LLM Using Qdrant

## Setup

The below code pulls the qdrant docker image and hosts the server on port 6333(default). This step can be skipped if you already have it hosted.
```
sudo docker pull qdrant/qdrant
sudo docker run -p 6333:6333 qdrant/qdrant
```

To install all the dependencies for the code:
```
pip3 install -r requirements.txt
```
This may be done using a virtual environment(recommended).
```
python3 -m venv venv
source venv/bin/activate
```

## API

The API has the following function calls:
```
def get_relevant_product(question, top_k, retriever, client, collection_name)
```
Given a question, this function encodes it using `multi-qa-MiniLM-L6-cos-v1` and queries it over our Qdrant client to retrieve relevant `top_k` product and it's context.

```
def extract_answer(question, context, reader)
```
From a given context, this function uses `bert-large-uncased-whole-word-masking-finetuned-squad` reader to generate answer for the query.

```
def get_answer(question, retriever, reader, qdrant_client, collection_name)
```
From the extracted `top_k` answers, this function returns the answer with the highest score.
The result is an object:
```
{'score': 0.8675349354743958, 'start': 79, 'end': 84, 'answer': '299.0', 'product': 'Sandal Skin Lightening Cream'}
```

### Example

For the below code snippet:
```
# ask question
question = "Suggest me a Diet food."
print(question)
answer = get_answer(question, retriever, reader, qdrant_client, collection_name)
print('Product: ', answer['product'], '\nAnswer: ', answer['answer'], ' ', '\nScore: ', answer['score'])
```

The output is:
```
Suggest me a Diet food.
Product:  Jaggery Spiced Cashews Trail Mix 
Answer:  Snacks, Dry Fruits, Nuts   
Score:  0.016895370557904243
```

More sample examples can be found in main.py in root directory.

## Similar Work

1) [Discord Chat Bot](https://github.com/Abhi575k/discord-chatbot)
2) [Mail Spam Detector](https://github.com/Abhi575k/mail-spam-detector)

## References

1) https://www.youtube.com/watch?v=LRcZ9pbGnno&ab_channel=Qdrant
2) https://colab.research.google.com/github/qdrant/examples/blob/master/extractive_qa/extractive-question-answering.ipynb#scrollTo=_4NRgV4mGWoj
3) https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1
4) https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad