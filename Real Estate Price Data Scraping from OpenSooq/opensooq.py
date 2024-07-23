
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time

import pandas as pd



# for x in tqdm(range(100)):
#     time.sleep(0.01)
    

    
def main():
    file_name = input('enter name file openSooq_links_? and change ? to number: ')
    with open(f"{file_name}.txt", 'r', encoding='utf-8-sig') as file:
        for line in tqdm(file):
            url = str(line)

            page = requests.get(url)
            src = page.content
            soup = BeautifulSoup(src, 'html.parser')
            
            bTable_list = []
            
            try:
                contaners = soup.find_all('div', class_= 'sc-23286f3d-0')[0].contents[1]
            except:
                print('page not found')
                continue
            len_con = len(contaners)
            
            # create for loop 
            for i in range(7):
                try:
                    features = contaners.contents[i].contents  # change the number 
                except:
                    print('page not found')
                    continue
                
                if i == 0:
                    try:
                        if 'City' == features[0].p.text.strip():
                            City = features[0].a.text.strip()
                        if 'Neighborhood' == features[1].p.text:
                            Neighborhood = features[1].a.text.strip()
                    except: 
                        City = ' '
                        Neighborhood = ' '
                elif i == 1:
                    try:
                        if 'Number of rooms' == features[0].p.text:
                            Number_of_rooms = features[0].a.text.strip()
                        if 'Number of bathrooms' == features[1].p.text:
                            Number_of_bathrooms = features[1].a.text.strip()
                    except:
                        Number_of_rooms = ' '
                        Number_of_bathrooms = ' '
                elif i == 2:
                    try:
                        if 'Surface Area' == features[0].p.text:
                            Surface_Area = features[0].a.text.strip()
                        if 'Floor' == features[1].p.text:
                            Floor = features[1].a.text.strip()
                    except: 
                        Surface_Area = ' '
                        Floor = ' '
                elif i == 3:
                    try:
                        if 'Building Age' == features[0].p.text:
                            Building_Age = features[0].a.text.strip()
                        if 'Furnished/Unfurnished' == features[1].p.text:
                            Furnished_Unfurnished = features[1].a.text.strip()
                    except:
                        Building_Age = ' '
                        Furnished_Unfurnished = ' '
                elif i == 4:
                    try:
                        if 'Lister Type' == features[0].p.text:
                            Lister_Type = features[0].a.text.strip()
                        if 'Property Status' == features[1].p.text:
                            Property_Status = features[1].a.text.strip()
                    except: 
                        Lister_Type = ' '
                        Property_Status = ' '
                elif i == 5:
                    try:
                        if 'Property Mortgaged?' == features[0].p.text:
                            Property_Mortgaged = features[0].a.text.strip()
                        if 'Payment Method' == features[1].p.text:
                            Payment_Method = features[1].a.text.strip()
                    except: 
                        Property_Mortgaged = ' '
                        Payment_Method = ' '
                elif i == 6:
                    try:
                        if 'Category' == features[0].p.text:
                            Category = features[0].a.text.strip()
                        if 'Subcategory' == features[1].p.text:
                            Subcategory = features[1].a.text.strip()
                    except:
                        Category = ' '
                        Subcategory = ' '
                else : print('error')
                
                # elif i == 7:
                #     if 'Amenities' == features[0].contents[0].text:
                #         Amenities = features[0].contents[1].text.strip()
                        
            # get price 
            try:             # if the price is exist
                price = soup.find('section', class_= 'sc-ed71d81b-2').find('span', class_= 'sc-1ccec9e8-6').text
            except:          # if the price is not exist
                price = soup.find('section', class_= 'sc-ed71d81b-2').find('span', class_= 'inline').text
                price = ' '  # Update the price to empity
            
            # get lat, long map feature
            try:
                location = str(soup.find_all('a', attrs={'class': 'sc-6c6e415d-0 cMYMdZ'}, href= True)).split(' ')[4].split('=')[3].split(',')
                latitude = location[0].strip()
                longitude = location[1].split('&')[0].strip()
                
            except: 
                latitude = ' '
                longitude = ' '
            
            def add_data_to_csv(filename, data):
            # Check if the file exists
                try:
                    with open(filename, 'r', encoding='utf-8-sig') as file:
                        reader = csv.reader(file)
                        header = next(reader)  # Read the header if it exists
                except FileNotFoundError:
                    header = None    # Indicate that the file does not exist

                # Append the data to the CSV file
                with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    if header is None:
                        writer.writerow(['price', 'City', 'Neighborhood','Number of rooms', 'Number of bathrooms',                                 
                                        'Surface Area', 'Floor', 'Building Age', 'Furnished/Unfurnished',
                                        'Lister Type', 'Property Status','latitude', 'longitude','Property Mortgaged', 
                                        'Payment Method','Category', 'Subcategory'])  # Write the header if it does not exist
                    for row in data:
                        writer.writerow(row)

            
            
            filename = f'{file_name}.csv'
            data = [
                [price, City, Neighborhood,Number_of_rooms, Number_of_bathrooms, Surface_Area,Floor, 
                Building_Age, Furnished_Unfurnished, Lister_Type, Property_Status, longitude, latitude, 
                Property_Mortgaged, Payment_Method, Category, Subcategory]
                ]
            add_data_to_csv(filename, data)

    
if __name__ == '__main__':
    main()
# with open(r'openSooq_links.txt', 'r', encoding="utf8") as f:
#     size = len(f.readlines())
#     print(f"the file size is: {size}")