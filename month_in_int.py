def month_in_int(date):
    if date.split()[1] == 'октября':
        date = date.replace('октября','10')
    elif date.split()[1] == 'ноября':
        date = date.replace('ноября', '11')
    elif date.split()[1] == 'декабря':
        date = date.replace('декабря', '12')
    elif date.split()[1] == 'января':
        date = date.replace('января', '1')
    elif date.split()[1] == 'февраля':
        date = date.replace('февраля', '2')
    elif date.split()[1] == 'марта':
        date = date.replace('марта', '3')
    elif date.split()[1] == 'апреля':
        date = date.replace('апреля', '4')
    elif date.split()[1] == 'мая':
        date = date.replace('мая', '5')
    elif date.split()[1] == 'июня':
        date = date.replace('июня', '6')
    elif date.split()[1] == 'июля':
        date = date.replace('июля', '7')
    elif date.split()[1] == 'августа':
        date = date.replace('августа', '8')
    elif date.split()[1] == 'сентября':
        date = date.replace('сентября', '9')
    day = date.split()[0]
    if len(day) == 1:
        day = '0' + day
    mouth = date.split()[1]
    year = date.split()[2]
    date = f'{year}-{mouth}-{day}'
    return date