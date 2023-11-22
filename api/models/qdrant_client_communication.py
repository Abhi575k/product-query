from qdrant_client import QdrantClient
from qdrant_client.http import models
import numpy as np
from tqdm.auto import tqdm

def createQdrantCollection(client, collection_name):
    # create collection
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=384,
            distance=models.Distance.COSINE,
        ),
    )
    print(f'Collection {collection_name} created')

def upsertData(client, collection_name, df, retriever):
    batch_size = 512
    for index in tqdm(range(0, len(df), batch_size)):
        i_end = min(index + batch_size, len(df))  # find end of batch
        batch = df.iloc[index:i_end]  # extract batch
        emb = retriever.encode(batch["context"].tolist()).tolist()  # generate embeddings for batch
        meta = batch.to_dict(orient="records")  # get metadata
        ids = list(range(index, i_end))  # create unique IDs

        # upsert to qdrant
        client.upsert(
            collection_name=collection_name,
            points=models.Batch(ids=ids, vectors=emb, payloads=meta),
        )

    collection_vector_count = client.get_collection(collection_name=collection_name).vectors_count
    print(f"Vector count in collection: {collection_vector_count}")
    assert collection_vector_count == len(df)