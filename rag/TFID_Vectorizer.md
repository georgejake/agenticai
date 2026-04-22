### How TFID Vectorizer work ,as per Claude Desktop
### My question
docs = ["Office equipment policy","Office furniture guideline","Office travel policy"] to tfidvectorizer ,it transformed it into below array [[0.72033345 0.         0.         0.42544054 0.54783215 0.        ]
 [0.         0.65249088 0.65249088 0.38537163 0.         0.        ]
 [0.         0.         0.         0.42544054 0.54783215 0.72033345]]
 ,though office word is present in all 3 elements ,we don't see the same value being repeated in first and second rows in the 2d array
 ### Answer
 Great observation! This is IDF (Inverse Document Frequency) suppressing "office" — but actually, "office" is represented, just not in the column you might expect. Let me break it down:
### What's Happening
"office" appears in all 3 documents, so its IDF score becomes very low (close to 0), meaning it carries little discriminating power and gets a near-zero weight.
Words in all docs get IDF = 1 (minimum), words in fewer docs get higher IDF.

### Why "office" differs between rows (0.425 vs 0.385)
Even though "office" has the same IDF in all rows, the TF-IDF vectors are L2-normalized (each row's values are scaled so the row's magnitude = 1). Doc 2 has fewer words, so normalization distributes weight differently.

Doc 1: 3 unique words → office score = 0.4254
Doc 2: 3 unique words but no "policy" → office score = 0.3854  ← redistributed
Doc 3: 3 unique words → office score = 0.4254  (same as doc 1)

Bottom line: "office" is column index 3 — it's there in every row, just suppressed by low IDF and rescaled by L2 normalization.