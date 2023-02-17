import spacy
nlp = spacy.load('en_core_web_md')

# Function takes a movie description as a parameter and compares it to a text file containing more descriptions
# to return a reccommendation based on similarity value
def movie_rec(description):
    movies = []
    reccommended = 0
    index = 0
    i = 0

    with open("movies.txt", "r") as f:
        for line in f:
            movies.append(line)

    # Loop through the list of descriptions and determine similarity to description parameter, updating instantiated
    # 'index' and 'reccommended' variables so we can store the highest value to compare against and the index of that 
    # value so we can return the result as our output.
    for token in movies:
        token = nlp(token)
        value = token.similarity(nlp(description))
        if value > reccommended:
            reccommended = value
            index = i
        i+=1

    result_arr = movies[index].split(" ")
    title = " ".join(result_arr[0:2]).strip(":")

    print(f"Based on your recently watched movies, you should watch {title}!")



description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

movie_rec(description)