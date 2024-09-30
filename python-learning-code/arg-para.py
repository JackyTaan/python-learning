#########
#written by tan lam ngan
########
#lesson of arguments and parameters
########

def sumoftwo(a, b):
    print('%d is sum of %d and %d', a+b,a,b)


def print_planet_info(name, radius, gravity):
    print('Name:', name)
    print('Radius: {} km'.format(radius))
    print('Gravity: {} g'.format(gravity))

planets = [
    ('Mecury', 240, 0.34),
    ('Venus', 223, 0.12),
    ('Mars', 252, 0.45),
    ('Earth', 243,0.23),
]


def average(*nums):
    return sum(nums)/len(nums)


def make_tag(elem, **attrs):
    html_attrs = []
    for key, val in attrs.items():
        attr = '{}="{}"'.format(key, val)
        html_attrs.append(attr)
        attrs = ' '.join(html_attrs)
    return '<{} {}>'.format(elem, attrs)

def get_empty_list():
    print('get empty list')
    return []

#def fun(seq=get_empty_list()):
#    print(id(seq))

def fun(val, seq=[]):
    seq.append(val)
    return seq


print('###########')
print('###########')

fun(3)
fun(4)

print('###########')

print('###########')
#fun()
print('###########')
print(make_tag('img', src='photo.png', font='vani'))
print('###########')
print(average(2,8))
mars = dict(name='Mars', radius=3390, gravity=0.3)
print_planet_info(**mars)
print('###########')
print(planets[-1])
print('###########')
print_planet_info(*planets[-1])
print('###########')
#sumoftwo(2,4)
print(sorted([-5,2,-4,8], key=None, reverse=True))

