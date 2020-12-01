import csv

a = 'L-карнитин табл шип №20 Консумед;Малкут;Новосибирск, ул. Б.Богаткова, д.264;420.00'


def write_to_file(data):
    print('write to file.....')
    with open('test' + '.csv', 'w', newline='') as file:
        a_pen = csv.writer(file)
        # for d in data.split():
        # print(data)
        a_pen.writerow([data])
        # pizdfec vagno


write_to_file(a)
