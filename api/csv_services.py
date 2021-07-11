import csv
import model as m
from datetime import datetime


class CSV_SERVICES:
    def get_csv(self, res: m.UserReg):
        filename = f'./csv/access_bld_{res.Bld}_floor_{res.Floor}.csv'
        f = open(filename, 'a+', encoding='utf-8-sig')
        w = csv.DictWriter(f, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC, fieldnames=[
                            'fname', 'lname', 'building', 'floor', 'isCheckin', 'timestamp'])
        # w.writeheader()
        data = [
            res.Fname,
            res.Lname,
            res.Bld,
            res.Floor,
            res.isCheckin,
            datetime.now()
        ]
        d = {
            "fname": res.Fname,
            "lname": res.Lname,
            "building": res.Bld,
            "floor": res.Floor,
            "isCheckin": res.isCheckin,
            "timestamp": datetime.now()
        }
        print(d, data)

        w.writerow(d)
        f.close()
