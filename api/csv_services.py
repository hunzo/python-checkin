import csv
from datetime import datetime
from pprint import pprint


class CSV_SERVICES:
    def logging_csv(self, fname: str, lname: str, phoneNum: int, bld: str, floor: int, isCheckin: bool):
        filename = f'./outfile/access_bld_{bld}_floor_{floor}.csv'
        f = open(filename, 'a+', encoding='utf-8-sig')
        w = csv.DictWriter(f, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC, fieldnames=['fname', 'lname', 'phoneNum','building', 'floor', 'isCheckin', 'timestamp'])
        # w = csv.writer(f, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
        # w.writeheader()
        data = {
            "fname": fname,
            "lname": lname,
            "building": bld,
            "floor": floor,
            "isCheckin": 'checkin' if isCheckin else 'checkout',
            "phoneNum": phoneNum,
            "timestamp": datetime.now()
        }
        print(csv)
				
        print('Data Logging...')
        pprint(data)

        w.writerow(data)
        f.close()

        f_name = './outfile/all_access_list.csv'
        fa = open(f_name, 'a+', encoding='utf-8-sig')
        wa = csv.DictWriter(fa, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC, fieldnames=['fname', 'lname', 'phoneNum','building', 'floor', 'isCheckin', 'timestamp'])
        wa.writerow(data)
        fa.close()

