#-*- coding: utf-8 -*-
import os
from lxml import etree, objectify
from io import StringIO, BytesIO

import logging
import re
afs={"afs":"http://ref.antidot.net/v7/afs#"}
ns={"ns":"http://ref.antidot.net/srv/"}

stable = 1
rc = 2
beta = 3
alpha = 4


Logger = logging.getLogger("antidot.service.ymi")
Logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
Logger.addHandler(consoleHandler)

Path='/Users/ymfinidori/Desktop/dsrmlTest'

os.chdir(Path)

files=os.listdir(path=Path)
Logger.info('list all files : %s' % files)

def dsrmlParser(file):
    status_id = 0
    #Logger.info('Parsing %s' % file)
    root = etree.parse(file)
    service_id = root.xpath("@id")[0]
    #Logger.debug('service id : %s' % service_id)
    nom = root.xpath("@name")[0]
    #Logger.debug('service name : %s' % nom)
    if root.find('.//ns:meta/ns:framework', namespaces=ns) is None:
        type = 'Licence'
    else:
        type = root.xpath("ns:meta/ns:framework", namespaces=ns)[0].text
        #Logger.debug('type : %s' % type)       
    url_interne = root.xpath("ns:meta/ns:url_interne/@url", namespaces=ns)[0]
    #Logger.debug('type : %s' % url_interne)
    if root.find('ns:meta/ns:url_client', namespaces=ns) is None :
        url_externe = 'no url'
    else:
        if 'url' in root.find('ns:meta/ns:url_client', namespaces=ns).attrib:
            url_externe = root.xpath("ns:meta/ns:url_client/@url", namespaces=ns)[0]
            #Logger.debug('type : %s' % url_externe)
        else:
            url_externe = 'no url' 
            
            
    allStatus = root.xpath("ns:instances/ns:instance/@status", namespaces=ns)
       
    for status in allStatus:
        if status == 'stable':
            status_id = stable
        if status == 'rc':
            status_id = rc
        if status == 'beta':
            status_id = beta
        if status == 'alpha':
            status_id = alpha

        
            
        print("INSERT INTO blog_service (nom, service_id, url_interne, url_externe, status_id, type) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" %(nom, service_id, url_interne, url_externe, status_id, type))

    return (nom, service_id, url_interne, url_externe, type)
    
for file in files: 
    dsrmlParser(file)  










