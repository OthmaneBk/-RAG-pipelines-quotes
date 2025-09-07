from embedder import quote_texts, embedder, index



def find_similar_quotes(query, k=3):
    query_vec = embedder.encode([query])
    distances, indices = index.search(query_vec, k)
    results = []
    for i in indices[0]:
        results.append(quote_texts[i])
    return results


"""user_question = "You don’t forget the face of the person who?"
top_quotes = find_similar_quotes(user_question)
print("Citations les plus proches :")
for quote in top_quotes:
    print(quote)"""