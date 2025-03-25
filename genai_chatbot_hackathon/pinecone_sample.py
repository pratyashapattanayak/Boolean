import pinecone
import os
from dotenv import load_dotenv
import openai
import json

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

# Initialize Pinecone
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT"))
index = pinecone.Index('your-kb-index')

# Load KB articles
with open('kb_articles.json') as f:
    articles = json.load(f)

# Create embeddings and upload to Pinecone
for article in articles:
    embedding = openai.Embedding.create(input=article['content'], model="text-embedding-ada-002")['data'][0]['embedding']
    index.upsert([(article['id'], embedding, {"kb_article": article['content']})])

print("Pinecone Index Updated")
