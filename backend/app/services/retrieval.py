def retrieve(query, top_k=5):
    query_vector = embeddings.embed_query(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    docs = [match['metadata']['text'] for match in results['matches']]
    return docs