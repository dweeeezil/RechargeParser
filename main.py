from pypdf import PdfReader
import csv
import os

DIRECTORY = 'PDFs'
CSV = 'data.csv'


class paymentForm():
    def __init__(self, date, user, advisor, kfs, cost, time, type):
        self.date = date
        self.user = user
        self.advisor = advisor
        self.kfs = kfs
        self.cost = cost
        self.time = time
        self.type = type
    
    def export(self,file):
        row = [self.date, self.user, self.advisor, self.kfs, self.cost, self.time, self.type]
        
        if os.path.exists(file):
            with open(file, 'a') as file:
                writer = csv.writer(file)
                writer.writerow(row)
        else:
            createCSV(file)
            self.export(file)

def createCSV(file):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'user', 'advisor', 'kfs', 'cost', 'time', 'type'])

def getPDF(path):
    reader = PdfReader(str(path))
    try:
        fields = reader.get_form_text_fields()

        date = fields['Text1']
        user = fields['Text2']
        advisor = fields['Text40']
        kfs = fields['Text39']
        times = [(fields['Text5']),
                (fields['Text7']), 
                (fields['Text9']),
                (fields['Text13']), 
                (fields['Text17']), 
                (fields['Text21']),
                (fields['Text23']),
                (fields['Text25']),
                (fields['Text27']),
                (fields['Text29']),
                (fields['Text31']),
                (fields['Text35'])]
        cost = (fields['Text22'])
        type = 'none'
        time = 0

        return(paymentForm(date, user, advisor, kfs, cost, time, type))
    except:
        return(paymentForm(path, "READ ERROR", "READ ERROR", "READ ERROR", "READ ERROR", "READ ERROR", "READ ERROR"))


def main():
    files = os.listdir(DIRECTORY)
    for filename in files:
        filepath = (DIRECTORY + '/' + filename)
        pdf = getPDF(filepath)
        pdf.export(CSV)

    return

if __name__ == ("__main__"):
    main()