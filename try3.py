def coauthors_dict():
    coauthors = {}
    with open('CA-GrQc.csv', 'r') as file:
        counter = 0 
        for line in file:
            counter += 1
            if counter >= 5:
                authors = line.strip().split(',')
                if len(authors) == 2:
                    author1 = int(authors[0])
                    author2 = int(authors[1])
                            
                    if author1 == author2:
                        continue
                            
                    if author1 not in coauthors:
                        coauthors[author1] = []
                    if author2 not in coauthors[author1]:
                        coauthors[author1].append(author2)
                            
                    if author2 not in coauthors:
                        coauthors[author2] = []
                    if author1 not in coauthors[author2]:
                        coauthors[author2].append(author1)
    return coauthors[14]

print(coauthors_dict())