Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# dictionary

# dictionary is not indexed
# dictionary ordered collection of data items
# instead of indexing, dict follows {key:value} as a paired items
# duplicate values are not followed
# popping allowed as usual

car = {} # create an empty dictionary
type(car)
<class 'dict'>
car['brand'] = 'VM'
car['model'] = 'polo'
car['price'] = '1500000'
car
{'brand': 'VM', 'model': 'polo', 'price': '1500000'}
car['brand']
'VM'
car['model']
'polo'
car['price']
'1500000'
car.keys()
dict_keys(['brand', 'model', 'price'])
>>> car.items()
dict_items([('brand', 'VM'), ('model', 'polo'), ('price', '1500000')])
>>> car.get('model')
'polo'
>>> car.pop('price')
'1500000'
>>> car
{'brand': 'VM', 'model': 'polo'}
>>> car.popitem()
('model', 'polo')
>>> car
{'brand': 'VM'}
>>> car.setdefault('model','polo')
'polo'
>>> car
{'brand': 'VM', 'model': 'polo'}
>>> value = car.fromkeys(car.keys())
>>> value
{'brand': None, 'model': None}
>>> vaue = car.setdefault('model','vento')
>>> value
{'brand': None, 'model': None}
