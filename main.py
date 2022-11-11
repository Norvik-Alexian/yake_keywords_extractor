from yake import KeywordExtractor

doc = '''
Face the winds of fall and winter with our reflective striped jacket with a graphic lettering design.
A versatile layering piece, it can be worn with a matching tracksuit and sneakers for a sporty casual look,
or elevated with denim and combat boots for that coveted gopnik punk aesthetic. 
'''

model = KeywordExtractor()
keywords_extractor = model.extract_keywords(doc)

for keywords in keywords_extractor[:5]:
    print(keywords[0])