

automobiliai = {}

automobiliai['1'] = {
    'marke': 'audi',
    'spalva': 'pilka',
    'variklis': 'benzinas',
    'metai': '1997'
}
automobiliai['2'] = {
    'marke': 'bmw',
    'spalva': 'juoda',
    'variklis': 'dyzelis',
    'metai': '2008'
}
automobiliai['3'] = {
    'marke': 'toyota',
    'spalva': 'sidabrine',
    'variklis': 'hybridas',
    'metai': '2015'
}
print(automobiliai['1'])
automobiliai['1']['variklis'] = 'dyzelis'
automobiliai['4'] = {
    'marke': 'mazda',
    'spalva': 'zalia',
    'variklis': 'dujos',
    'metai': '1998'
}
del automobiliai['2']
print(len(automobiliai))
print("Ar žodyne yra pilka audi?", 'audi pilka' in [
      automobiliai[auto]['marke'] + ' ' + automobiliai[auto]['spalva'] for auto in automobiliai])
