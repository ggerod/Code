#!/usr/bin/python3

#code1="525150535130034030405035055210105230021025505103305200455350155053255035203150411551020351514525455353452150512414502550005110535015505325511064775150146566703541156455116455127576256534377171475615763574476325"
code1="525150535130034030405035055210105230021025505103305200455350155053255035203150411551020351514525455353452150512414502550005110535015505325511052513150411551304520100352424232222510105150514015503005454151103522"
codes=[code1[i:i+2] for i in range(0,len(code1),2)]

polysquare=[
 ['F', 'G', 'H', 'I', 'J', 'K'],
 ['E', 'X', 'Y', 'Z', '0', 'L'],
 ['D', 'W', '7', '8', '1', 'M'],
 ['C', 'V', '6', '9', '2', 'N'],
 ['B', 'U', '5', '4', '3', 'O'],
 ['A', 'T', 'S', 'R', 'Q', 'P']]

for code in codes:
    print(polysquare[(int(code[0]))][(int(code[1]))], end="")

print("=========")

