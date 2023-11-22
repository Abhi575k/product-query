import warnings
warnings.filterwarnings("ignore")

def get_relevant_product(question, top_k, retriever, client, collection_name):
    """
    Get the relevant product for a given question
    """
    try:
        encoded_query = retriever.encode(question).tolist()  # generate embeddings for the question

        result = client.search(
            collection_name=collection_name,
            query_vector=encoded_query,
            limit=top_k,
        )  # search qdrant collection for context passage with the answer

        context = [
            [x.payload["product"], x.payload["context"]] for x in result
        ]  # extract title and payload from result
        return context

    except Exception as e:
        print({e})

def extract_answer(question, context, reader):
    """
    Extract the answer from the context for a given question
    """
    results = []
    for c in context:
        # feed the reader the question and contexts to extract answers
        answer = reader(question=question, context=c[1])

        # add the context to answer dict for printing both together, we print only first 500 characters of plot
        answer["product"] = c[0]
        results.append(answer)

    # sort the result based on the score from reader model
    sorted_result = sorted(results, key=lambda x: x["score"], reverse=True)
    return sorted_result

def get_answer(question, retriever, reader, qdrant_client, collection_name):
    # get relevant product
    context = get_relevant_product(question, 5, retriever, qdrant_client, collection_name)

    # extract answer
    return extract_answer(question, context, reader)[0]
