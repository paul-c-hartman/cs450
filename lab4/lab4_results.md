# Names: Paul Hartman
# Lab: Lab 4 (Retrieval Augmented Generation)
# Date: 10/27/2025

## Understanding embeddings
1. The embedding vectors are all the same length for the given text.
2. The vectors are different, although the two sentences with similar meanings have vectors that are kinda similar at a glance.

## Measure similarity
1. The texts that have similar semantic meanings are more similar.
2. It does.
3. I tried replacing the third with 'I like eating hats,' which had a lower similarity score than the given third one, which makes sense because the meaning is semantically different and the sentence structure is dissimilar as well, whereas the given third one has a similar sentence structure.

## Building a knowledge base
1. The top results are relevant to the query.
2. A relevant document has information and context relating to a query. Semantic similarity is part of this, but not all of it.

## RAG implementation
1. It does when it decides it has the answer.
2. It says "I don't know."
3. The retrieved sources are relevant.

## Compare with and without RAG
1. The RAG approach gives more accurate answers.
2. I would prefer it over direct LLM queries when the topic is not something the LLM is trained on--domain-specific knowledge, basically.

## RAG with large files
1. The structure does matter--if you ask a question in a semantically different way to how it's presented in documents, it won't always pick up that the documents have answering information.
2. See above.
3. The course name in the questions is "CS450" and in the syllabus is "CPTR 450". The course name isn't in the context, so I assume the LLM is "bridging the gap" a little and assuming they're the same. But this means the questions are a little bit more semantically different from the context it's given, which is why it doesn't always answer. This demonstrates how small semantic differences can add up and cause a RAG to freeze up, essentially.