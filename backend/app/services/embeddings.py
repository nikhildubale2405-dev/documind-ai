from langchain_openai import OpenAIEmbeddings
import pinecone

embeddings = OpenAIEmbeddings()

pinecone.init(
    api_key="YOUR_API_KEY",
    environment="YOUR_ENV"
)

index = pinecone.Index("documind")

def store_embeddings(chunks):
    vectors = []

    for i, chunk in enumerate(chunks):
        vector = embeddings.embed_query(chunk)
        vectors.append((str(i), vector, {"text": chunk}))

    index.upsert(vectors)