import chardet
def find_encoding(name):
    file = open(name,'rb').read()
    result = chardet.detect(file)
    charenc = result['encoding']
    return charenc
file_name = 'scrapping\\Qdata\\index.txt'
my_encode = find_encoding(file_name)
with open(file_name, 'r', encoding=my_encode) as f:
    lines = f.readlines()
def preprocess(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms
vocab = {}
documents = []
for index, line in enumerate(lines):
    # read statement and add it to the line and then preprocess
    tokens = preprocess(line)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1
#reverse sorting vocab by value
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

# save the vocab in a text file
with open('scrapping/tf-idf/vocab.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save the idf values in a text file
with open('scrapping/tf-idf/idf-values.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

# save the documents in a text file
with open('scrapping/tf-idf/documents.txt', 'w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))

inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open('scrapping/tf-idf/inverted-index.txt', 'w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))
       