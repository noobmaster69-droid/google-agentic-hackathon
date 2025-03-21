from google.cloud import aiplatform
from vertexai.language_models import TextEmbeddingModel
from pinecone import Pinecone, ServerlessSpec
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ID = 'formal-loop-452705-h1'
REGION = 'us-central1'
PINECONE_API_KEY = 'pcsk_6XfUhD_URrTDuNDagfChu6YHGvqnxHCK9ajrBM9yNbX3Rp6ZNYoxdV5h9oLDXTdnCarF8i'
PINECONE_ENV = "us-east1"  # Or "us-west1-gcp" or your env
INDEX_NAME = "product-index"

try:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    logger.info("Successfully initialized Pinecone")
except Exception as e:
    logger.error("Failed to initialize Pinecone: %s", e)
    raise

try:
    index = pc.Index('product-index')
    logger.info("Successfully connected to Pinecone index")
except Exception as e:
    logger.error("Failed to connect to Pinecone index: %s", e)
    raise

def retrieve_product(product_id: str):
    try:
        fetch_response = index.fetch(ids=[product_id])
        if product_id in fetch_response.vectors:
            retrieved_vector = fetch_response.vectors[product_id]
            return retrieved_vector.metadata
        else:
            return None
    except Exception as e:
        print(f"Error retrieving product: {e}")
        return None


def retrieve_product_by_brand(brand: str):
    try:
        query_results = index.query(
            vector=[0.0] * 768,  # Dummy vector, as it's required but ignored when using a filter
            top_k=10,  # Adjust as needed to retrieve more results
            filter={
                "brand": {"$eq": brand}
            },
            include_metadata=True  # Ensure metadata is included in the results
        )

        if query_results.matches:
            # Return the metadata of the matched vectors
            products = [match.metadata for match in query_results.matches]
            return products
        else:
            return None
    except Exception as e:
        print(f"Error retrieving products by brand: {e}")
        return None

# Example usage
# product_id_to_retrieve = "Galaxy Z Fold5"
# retrieved_product = retrieve_product(product_id_to_retrieve)
# retrieved_product = retrieve_product_by_brand("Google")
#
# if retrieved_product:
#     print("Retrieved Product:")
#     print(retrieved_product)
# else:
#     print("Product not found.")
