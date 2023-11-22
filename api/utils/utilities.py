from qdrant_client import QdrantClient
import torch
from sentence_transformers import SentenceTransformer
from transformers import pipeline

qdrant_client_loaded = False
retriever_loaded = False
reader_loaded = False

qdrant_client = None
retriever = None
reader = None

def getQdrantClient():
    """
    Returns the Qdrant client
    """
    global qdrant_client_loaded
    global qdrant_client
    if qdrant_client_loaded:
        return qdrant_client
    # initialize Qdraant client
    qdrant_client = QdrantClient(host='localhost', port=6333)
    qdrant_client_loaded = True
    return qdrant_client

def getRetriever():
    """
    Returns the retriever model from huggingface model hub
    """
    global retriever_loaded
    global retriever
    if retriever_loaded:
        return retriever
    # set device to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # load the retriever model from huggingface model hub
    retriever = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1", device=device)
    retriever_loaded = True
    return retriever

def getReader():
    """
    Returns the reader model from huggingface model hub
    """
    global reader_loaded
    global reader
    # load the reader model into a question-answering pipeline
    if reader_loaded:
        return reader
    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
    reader = pipeline("question-answering", model=model_name, tokenizer=model_name)
    reader_loaded = True
    return reader