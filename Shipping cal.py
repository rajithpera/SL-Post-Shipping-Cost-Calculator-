A = ['india', 'maldives']
B = ['bangladesh', 'bhutan', 'cambodia', 'lao peo:dem:rep', 'malaysia', 'myanmar', 'nepal', 'oman', 'pakistan', 'singapore', 'thailand', 'vietnam']
C = ['afghanistan', 'azerbaijan', 'bahrain', 'brunei', 'comoros', 'djibouti', 'eritrea', 'ethiopia', 'hongkong', 'indonesia', 'iran', 'iraq', 'kazakhstan', 'kenya', 'kirghizstan', 'kuwait', 'macao', 'madagascar dem:rep', 'mauritius', 'philippines', 'qatar', 'reunion', 'saudi arabia', 'seychelles', 'somalia', 'taiwan', 'tajikistan', 'tanzania', 'turkmenistan', 'united arab emirates','uae','u.a.e', 'uzbekistan', 'yemen']
D = ['armenia', 'botswana', 'bulgaria', 'burundi', 'central african rep:', 'china peo:rep:', 'cyprus', 'east timor', 'egypt arab rep:', 'georgia', 'greece', 'israel', 'japan', 'jordan', 'lebanon', 'malawi', 'moldova', 'mongolia', 'mozambique', 'north korea', 'palau', 'romania', 'russian federation', 'rwanda', 'south africa', 'south korea', 'sudan', 'swaziland', 'syria', 'turkey', 'uganda', 'ukraine', 'zambia', 'zimbabwe']
E = ['albaria', 'angola', 'australia', 'austria', 'belarus', 'bosnia & herzegovina', 'cameroon', 'chad', 'congo peo:rep:', 'congo dem:rep:', 'croatia', 'czech republic', 'estonia', 'finland', 'gabon', 'guam', 'hungary', 'latvia', 'lesotho', 'libya', 'lithuania', 'macedonia', 'malta', 'montenegro', 'namibia', 'papua new guinea', 'poland', 'san marion', 'serbia', 'slovakia', 'slovenia', 'sweden', 'tunisia','tristan da cunha', 'vatican city state','virgin islands(gb)','virgin islands (gb)']
F = ['algeria', 'andorra', 'belgium', 'benin', 'burkina faso', 'cote d ivoire', 'denmark', 'equatorial guinea', 'france', 'germany', 'ghana', 'gibraltar', 'great britain', 'ireland', 'isle of man', 'italy', 'lichtenstein', 'luxembourg', 'mali rep: of', 'micronesia', 'monaco', 'morocco', 'nauru', 'netherlands', 'niger:rep:of', 'nigeria', 'northern ireland', 'norway', 'portugal', 'são tomé and príncipe', 'solomon islands', 'spain', 'switzerland', 'togo','tokelau']
G = ['cape verde', 'fiji', 'gambia', 'guinea bissau', 'guinea rep: of', 'iceland', 'liberia', 'marshall islands', 'mauritania', 'new zealand', 'samoa western', 'senegal', 'sierra leone','syrian arab rep','st.pierre & miquelon','st. pierre & miquelon', 'tuvalu', 'vanuatu','virgin islands(usa)','virgin islands (usa)','wallis and futuna islands']
H = ['anguilla', 'antigua & barbuda', 'antilles (netherlands)', 'argentina', 'aruba', 'bahamas', 'barbados', 'belize', 'bermuda', 'bolivia', 'brazil', 'canada', 'cayman island', 'chile', 'colombia', 'cook island', 'costa rica', 'cuba', 'dominica', 'dominican rep:', 'ecuador', 'el salvador', 'grenada','guadeloupe', 'guatemala', 'guyana','haiti', 'honduras', 'jamaica', 'kiribati', 'mexico', 'nicaragua', 'niue', 'panama', 'paraguay', 'peru', 'puerto rico', 'samoa', 'st christopher & nevis', 'st lucia', 'st. vincent & grenadines','st.vincent','st. vincent', 'suriname', 'tonga', 'trinidad & tobago', 'u.s.a','usa', 'uruguay', 'venezuela']

Ap = [160,325,600,1150]
Bp = [185,358,725,1400]
Cp = [205,445,845,1640]
Dp = [230,510,970,1895]
Ep = [255,570,1090,2135]
Fp = [280,630,1215,2380]
Gp = [310,700,1355,2665]
Hp = [425,995,1940,3835]

def country(name):
    if name.lower() in A:
        name = ('A')
    elif name.lower() in B:
        name = ('B')
    elif name.lower() in C:
        name = ('C')
    elif name.lower() in D:
        name = ('D')
    elif name.lower() in E:
        name = ('E')
    elif name.lower() in F:
        name = ('F')
    elif name.lower() in G:
        name = ('G')
    elif name.lower() in H:
        name = ('H')
    else:
        name = ('NOT FOUND')
    return name


# def weightcat(weight,):
c_name = str(input("enter the name: "))
weight = float(input("Please enter the weight: "))
x = (country(c_name))

def main (wei,group):
    
    if wei==100:
        y = int(0)
    elif 100 < wei <= 250:
        y = int(1)
    elif 251 <= wei <= 500:
        y = int(2)
    elif 501 <= wei <= 1000:
        y = int(3)

    p_group = group+'p'
    var = globals()[p_group]
        
    return (var[y])

print(main(weight,x))


input("Please enter to Exit")