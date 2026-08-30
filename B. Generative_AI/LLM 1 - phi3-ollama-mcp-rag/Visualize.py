import chromadb

client = chromadb.PersistentClient(path="/app/.chroma")
collection = client.get_collection("docs")

data = collection.get()

print(len(data["documents"]))
print(data["documents"][:3])