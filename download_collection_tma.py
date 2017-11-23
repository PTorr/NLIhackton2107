import os
import urllib2
import json

collection_name = 'maps'
a = open('json_files/{}.json'.format(collection_name),'r')
maps = eval(a.read())
# bitmuna = json.loads('''{}'''.format(json_text))

img_list = []
date_list = []

image_num = 0
dates = []
for member in maps:
    if image_num == 1500:
        break
    link = member['@id']
    response = urllib2.urlopen(link)
    response_text = response.read()
    html_dict = eval(response_text)
    if len(html_dict['sequences']) > 0:
        image_num += 1
        image_link = html_dict['sequences'][0]['canvases'][0]['images'][0]['resource']['@id']
        image_name = response_text[response_text.find('NNL') : response_text.find('/', response_text.find('NNL'))]
        for record in html_dict['metadata']:
            if record['label'] == 'Creation Date':
                year = record['value']
                try:
                    float(year)
                    date_list.append(year)
                    output = open("maps/{}.jpg".format(image_name),'wb')
                    output.write(urllib2.urlopen(image_link).read())
                    output.close()
                    img_list.append(image_name)
                    print image_name, year
                except ValueError:
                    print "Not a number"                

pickle.dump(img_list, open('img_list_{}.pickle'.format(collection_name)))
pickle.dump(date_list, open('dates_list_{}.pickle'.format(collection_name)))
