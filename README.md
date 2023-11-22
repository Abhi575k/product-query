# Large Language Model Using Qdrant

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

## Miscellaneous

1) The code assumes the product name(s) to be unique.
2) The input csv should be named "data.csv".

## TODO

1) Dissolve multiple colums to a single column - description
2) Learn how to use a Qdrant client over a Docker
3) Create Qdrant collection
4) Initialize retriever for embedding context and queries

```
# set device to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"

# load the retriever model from huggingface model hub
retriever = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1", device=device)
retriever
```

## References

1) https://www.youtube.com/watch?v=LRcZ9pbGnno&ab_channel=Qdrant
2) 