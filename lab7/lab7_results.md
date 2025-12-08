# Names: Paul Hartman, Jenessy Lustre
# Lab: lab7 (RAG for Code with UniXcoder)
# Date: 12/8/2025

## 2.2
1. Look at the "discrimination" scores - what do they tell you?

UniXcoder differentiates between different pieces of code much better than a generic text embedding model. It's able to tell whether code snippets are more similar or different much more reliably than a generic model.

## 2.3
1. Does UniXcoder recognize functionally similar code despite variable name changes and type hints?

It does; adding type hints results in very little change, while changing variable names resulted in a larger (but still relatively small) change.

## 2.4
1. Does UniXcoder recognize increasingly numerous changes?

It does; adding more changes results in increasingly different embeddings. 

2. How does it handle the "cosmetic" changes? Does it think it's important, and if so, why?

It thinks it's pretty important since "cosmetic" changes often recontextualize the code, changing the model's understanding of how it works. The code with "cosmetic" changes still generates similar embeddings but not to the same extent as simply changing operators.

## 3.2
1. Do different phrasings of the same question retrieve the same functions?

Yes, although the format of the question changes the distance values. Natural language queries have consistently low values while keyword-only questions have higher ones. Essentially, less ambiguous queries have lower distance.

## 4.2
1. Which query types work best with UniXcoder?

Natural language queries can work best when they're well-formed, but on average, use-case-style queries have the lowest distance values to relevant pieces of code.

2. How does UniXcoder handle vague vs specific queries?

Vague queries tend to have larger distance values than specific ones, although keywords in the query will still lead to matches. Specific queries are better in nearly every case, though.