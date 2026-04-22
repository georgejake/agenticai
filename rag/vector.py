from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

docs = ["Office equipment policy","Office furniture guideline","Office travel policy"]

analyzer = TfidfVectorizer()
word_scores = analyzer.fit_transform(docs)
print(word_scores.toarray())

# See the vocabulary mapping
print(analyzer.vocabulary_)
# {'office': 3, 'equipment': 0, 'policy': 4, 'furniture': 1, 'guideline': 2, 'travel': 5}

print(analyzer.idf_)
# IDF values for each word


df = pd.DataFrame(
    word_scores.toarray(),
    columns=analyzer.get_feature_names_out()
)
print(df)
'''
So far we have the TF-IDF scores for each word in each document. Now we can use these scores to
find the most relevant documents for a given query. For example, if we want to find documents related to "office policy", we can calculate the TF-IDF scores for the query and then compare them with the document scores.
'''
query = "furniture"
query_score = analyzer.transform([query])
print(query_score.toarray())    
# Now we can calculate the cosine similarity between the query and each document


similarity_scores = cosine_similarity(query_score, word_scores)
print(similarity_scores)



best_idx = np.argmax(similarity_scores)
print(f"Best match index : {best_idx}")
print(f"Best match doc   : {docs[best_idx]}")
print(f"Similarity score : {similarity_scores[0][best_idx]:.4f}")
