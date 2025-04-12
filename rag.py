import pandas as pd
from openai import OpenAI
import numpy as np
import os

# Initialize OpenAI client (replace with your API key)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY', 'your-api-key-here'))

# Sample startup descriptions
data = pd.DataFrame({
    'startup_id': [201, 202],
    'name': ['Startup A', 'Startup B'],
    'description': [
        'A fintech platform for decentralized lending.',
        'AI-driven investment analytics for startups.'
    ]
})

def generate_embeddings(texts, model="text-embedding-ada-002"):
    """Generate embeddings for RAG pipeline using OpenAI."""
    embeddings = []
    for text in texts:
        response = client.embeddings.create(input=text, model=model)
        embedding = response.data[0].embedding
        embeddings.append(embedding)
    return np.array(embeddings)

def prepare_rag_data(df):
    """Prepare dataset for RAG with embeddings."""
    # Clean and preprocess descriptions
    df['description_clean'] = df['description'].str.lower().str.strip()
    
    # Generate embeddings
    embeddings = generate_embeddings(df['description_clean'].tolist())
    
    # Add embeddings to DataFrame
    df['embedding'] = list(embeddings)
    
    # Save to MySQL-compatible format (embeddings as JSON or serialized)
    df[['startup_id', 'name', 'description', 'embedding']].to_json('rag_data.json', orient='records')
    print("RAG data prepared and saved to rag_data.json")
    
    return df

# Run RAG prep
rag_data = prepare_rag_data(data)
print("Sample RAG Data:")
print(rag_data[['startup_id', 'name', 'description']])

# Example: Semantic search simulation
query = "fintech lending"
query_embedding = generate_embeddings([query])[0]
similarities = np.dot(rag_data['embedding'].tolist(), query_embedding)
top_match = rag_data.iloc[np.argmax(similarities)]
print(f"Top match for '{query}': {top_match['name']} - {top_match['description']}")