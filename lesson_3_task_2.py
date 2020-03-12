def bio(**kwargs):
    result = ''
    for key, value in kwargs.items():
        result = result + ' ' + value
    return result


data = {
    'name' : 'Mohammed',
    'surname' : 'Jamale',
    'year_of_birth' : '1994',
    'city' : 'Abu-Dhabi',
    'email' : 'jamale1994@gmail.com',
    'phone_number' : '1854535353',
}

print(bio(**data))