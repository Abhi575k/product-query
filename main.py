import warnings
warnings.filterwarnings("ignore")
from transformers import logging
logging.set_verbosity_error()

from api.utils.utilities import getQdrantClient
from api.utils.utilities import getRetriever
from api.utils.utilities import getReader

from api.models.data_preprocessing import preprocess

from api.models.qdrant_client_communication import createQdrantCollection
from api.models.qdrant_client_communication import upsertData

from api.api import get_answer

# initialize Qdraant client
qdrant_client = getQdrantClient()

# data
data = preprocess('./api/models/data.csv')

# create collection
collection_name = 'product-query'
collections = qdrant_client.get_collections()

retriever = getRetriever()

# only create collection if it doesn't exist
if collection_name not in [c.name for c in collections.collections]:
    createQdrantCollection(qdrant_client, collection_name)
    # upsert data
    upsertData(qdrant_client, collection_name, data, retriever)

reader = getReader()

# ask question
question = "Which is the best face cream?"
print(question)
answer = get_answer(question, retriever, reader, qdrant_client, collection_name)
print('Product: ', answer['product'], '\nAnswer: ', answer['answer'], ' ', '\nScore: ', answer['score'])

# ask question
question = "Suggest me a Diet food."
print(question)
answer = get_answer(question, retriever, reader, qdrant_client, collection_name)
print('Product: ', answer['product'], '\nAnswer: ', answer['answer'], ' ', '\nScore: ', answer['score'])

# ask question
question = "Which is the best moisturiser?"
print(question)
answer = get_answer(question, retriever, reader, qdrant_client, collection_name)
print('Product: ', answer['product'], '\nAnswer: ', answer['answer'], ' ', '\nScore: ', answer['score'])


