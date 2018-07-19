from SPARQLWrapper import SPARQLWrapper2, JSON

sparql = SPARQLWrapper2('https://dbpedia.org/sparql')

with open('datasets/dbpedia/movies', mode='w', encoding='UTF-8') as f:

    for year in range(1919, 2001):
        query = """
            SELECT DISTINCT ?movie ?title ?year WHERE {
                ?movie rdf:type <http://dbpedia.org/ontology/Film>.
                ?movie rdfs:label ?title.
                ?movie dct:subject ?cat.
                ?cat rdfs:label ?year.
                FILTER langMatches(lang(?title), "EN").
                FILTER regex(?year, "^%d film", "i")
            }
            ORDER BY ?movie
        """ % (year)

        sparql.setQuery(query)

        for result in sparql.query().bindings:
            f.write('{:s}::{:s}::{:s}\n'.format(
                result['movie'].value, result['title'].value, result['year'].value))

    f.close()
