import os
import urllib2
import json

collection_name = 'ephemera'
collection_link = 'http://iiif.nli.org.il/collections/{}.json'.format(collection_name)
response = urllib2.urlopen(collection_link)
output = open("json_files/{}.json".format(collection_name),'wb')
output.write(response.read())
output.close()
maps = json.load(open('json_files/{}.json'.format(collection_name),'rb'))

image_num = 0
for member in maps['members']:
    link = member['@id']
    response = urllib2.urlopen(link)
    response_text = response.read()
    image_name = response_text[response_text.find('NNL_MAP') : response_text.find('/', response_text.find('NNL_MAP'))]
    html_dict = eval(response_text)
    if len(html_dict['sequences']) > 0:
        image_num += 1
        image_link = html_dict['sequences'][0]['canvases'][0]['images'][0]['resource']['@id']
        output = open("maps/{}.jpg".format(image_name),'wb')
        output.write(urllib2.urlopen(image_link).read())
        output.close()
        print image_name
