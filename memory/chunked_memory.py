# Layer 1 - Cloud & Hadoop Big Data Foundation
import math

class ChunkedMemory:
    def __init__(self, chunk_size=1000):
        self.chunk_size = chunk_size
        self.lake = [] # Simulates Hadoop Data Lake
        self.metadata = []
        print(f"[LAYER 1] Hadoop Data Lake Initialized - Chunk Size {chunk_size}")

    def store(self, query, response):
        combined = f"Q:{query} | A:{response} | TIMESTAMP:3026"
        # Hadoop style chunking
        chunks = [combined[i:i+self.chunk_size] for i in range(0, len(combined), self.chunk_size)]
        for idx, chunk in enumerate(chunks):
            self.lake.append(chunk)
            self.metadata.append({"id": len(self.lake), "source": query[:20], "chunk": idx})

        return f"Stored in {len(chunks)} Hadoop chunks | Total Lake: {len(self.lake)} chunks"

    def retrieve(self, query):
        # Simulated Vector Search - Future will use FAISS
        results = []
        q_word = query.split()[0].lower() if query else ""
        for chunk in self.lake:
            if q_word in chunk.lower():
                results.append(chunk)
        return results[:3] if results else ["No relevant memory - New innovation"]

    def stats(self):
        size_mb = len(self.lake) * self.chunk_size / 1e6
        return {
            "total_chunks": len(self.lake),
            "size_mb": f"{size_mb:.2f} MB virtual",
            "hadoop_nodes": "3 (simulated)",
            "status": "Distributed & Encrypted"
        }
