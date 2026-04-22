from rank_bm25 import BM25Okapi  # ← most commonly used variant

docs = ["Office equipment policy", "Office furniture guideline", "Office travel policy"]

# BM25 needs tokenized input (list of lists)
tokenized_docs = [doc.lower().split() for doc in docs]

bm25 = BM25Okapi(tokenized_docs)

# Query
query = "furniture"
tokenized_query = query.lower().split()

scores = bm25.get_scores(tokenized_query)
print(scores)  # [0.  0.93729472  0.]

# Best match
import numpy as np
best_idx = np.argmax(scores)
print(docs[best_idx])  # Office furniture guideline