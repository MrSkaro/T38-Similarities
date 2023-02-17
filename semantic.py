import spacy
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


'''It's interesting that the similarity detector will find more similarity between a monkey and a banana than a cat and a banana
because of a monkey's diet, or the perception of a monkey's diet from media/pop culture.

A similar example might be 'gun', 'sword', 'bullet' where 'gun' is more similar to 'bullet' than 'sword' is because guns shoot
bullets.'''

word1 = nlp("gun")
word2 = nlp("sword")
word3 = nlp("bullet")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
     for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))




sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)


'''Changing the language model to en_core_web_sm in the example file causes the model to find lower similarity values.

Changing it in this file prints a warning stating that this model does not load word vectors but only determines similarities
based on context-sensitive tensors. Therefore any similarity test between individual words is going to be unreliable as the 
words being tested have no context.'''