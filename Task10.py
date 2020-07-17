countries = {'Japan': 'Tokyo', 'Korea': 'Seoul', 'Greece': 'Athens', 'Italy': 'Rome', 'Australia': 'Canberra'}
print(countries)
print('In which city do you live?')
country = input()

if country in countries:
    print('This city of country', countries[country])




