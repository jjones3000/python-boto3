import json
from bson import json_util
import os
import sys
import csv
import datetime
import io
import re
import requests
import base64
import logging
import itertools, sys
import dateutil.parser
from pprint import pprint
import datetime
from json import JSONEncoder

arr_from_slack = ['dev-website-website-blue-20200515221620972100000004',
'production-drive-report-green-2018122023334785650000000b',
'production-drive-history-green-20181102173958557500000012',
'production-quickloc-blue-20181205234708657400000003',
'dev-consul.blue.20171025223236660900000002',
'production-async-cake-iap-blue-20191004003141579800000004',
'mysql-main-55.production20201006014315842500000001',
'production-nsq-kinesis-blue-20181116194837156700000008',
'mysql-main-04.production20191205001240599700000004',
'master-us-east-1c.masters.kube.dev.us-east-1.life360.com',
'production-metronome-blue-20181114221222458300000003',
'dev-nsq-kinesis-blue-20200204224219868600000007',
'production-rattail-http-green-20180913215903145900000003',
'nodes.kube.dev.us-east-1.life360.com',
'production-push360-gcm-green-2018102418140676090000000c',
'production-grafana-blue-20190816224619768800000004',
'eks-56b76412-3f5c-bf98-97b6-fa893fff4ef6',
'production-blackbox_exporter-blue-20190621220427752700000004',
'eks-f0b80e8a-e150-3694-3f16-eb2b1f545005',
'production-mydb-green-20190517010205708100000002',
'production-vernemq2-green-20190405164106264500000003',
'production-async-cake-device-deleted-blue-2018110118514426130000000f',
'production-nsqadmin-blue-20200505150122462400000004',
'mysql-main-25.production00c78d1ecfff5178f6046cd8e1',
'mysql-main-35.production20191205001240496000000003',
'production-tumbler-blue-20190625193057059500000003',
'production-nsq-kinesis-drives-green-2018111619483745940000000b',
'mysql-main-75.production20191205002553665500000003',
'production-eks1-asg',
'master-us-east-1d.masters.kube.dev.us-east-1.life360.com',
'production-appboy-blue-20181108000619662600000004',
'dev-eks2-asg',
'production-async-cake-pushuserlocation-green-20180917215043713800000004',
'production-geodecode-blue-20181108201329460000000004',
'production-nsq-kinesis-dwell-blue-20181116194837056200000007',
'production-consul-blue-20200317200756775100000004',
'cx-i3.blue.00c2d56cd52c7a6ccc1d089a2f',
'eks-98b76412-45ac-b143-ac3a-fa1deec4ea8b',
'mysql-main-43.production20200420013936233200000001',
'production-dvbrawdataforwarding-blue-20181119185142457900000003',
'production-nsqlookupd-blue-20181030234025661100000003',
'production-git2consul-blue-20190625193043554700000004',
'production-async-cake-sos-alert-green-20200506162200039700000004',
'production-platform-location-blue-2019111122020342940000000c',
'eks-f8b80e8a-e13c-6bb6-5610-8bc2a5e52f76',
'production-data-operations-blue-20191106003614095200000004',
'mysql-main-805.production20200324023228805500000001',
'master-us-east-1e.masters.kube.dev.us-east-1.life360.com',
'production-mydb-google-oauth-blue-20190914003205174800000001',
'prod-website-website-green-20200527224852946800000003',
'dev-mono-green-debug-158',
'dev-cx-qa-blue-20171120191230346000000004',
'eks-a8b80e8a-e13f-7e1d-cfdc-952c1b965c5d',
'production-cx-drive-report-blue-20181220233345962400000007',
'production-frontend-router-blue-20190507215201657500000004',
'production-george-read-green-20181102174000458700000016',
'eks-b6b76412-455a-4291-a994-30dee265d00e',
'production-drive-report-http-green-20181220233346955800000009',
'dev-dvbrawdataforwarding-blue-20210430011524223500000003',
'production-geonames-platform-blue-20190628195116904500000005',
'production-post-rgc-green-20181102173958556600000011']

arr_from_boto = ['cx-i3.blue.00c2d56cd52c7a6ccc1d089a2f',
'cx-i3.green.00c2d56cd52c7a6ccc1d089a2e',
'dev-appboy-blue-20191106201627830700000014',
'dev-appboy-green-20191106201626451500000010',
'dev-async-cake-battery-blue-20190712200005766900000004',
'dev-async-cake-battery-green-20190712200003858400000003',
'dev-async-cake-device-deleted-blue-20191106201627764100000013',
'dev-async-cake-device-deleted-green-20191106201629830400000018',
'dev-async-cake-handler-blue-20190502010555655900000003',
'dev-async-cake-handler-green-20190502010555857400000004',
'dev-async-cake-iap-blue-20191106201629828800000017',
'dev-async-cake-iap-green-20191106201629833100000019',
'dev-async-cake-location-heartbeat-blue-2019110620163150730000001b',
'dev-async-cake-location-heartbeat-green-2019110620163170180000001c',
'dev-async-cake-pushuserlocation-blue-2019110620162645150000000f',
'dev-async-cake-pushuserlocation-green-20191106201626453500000011',
'dev-async-cake-sos-alert-blue-20200430145528404100000003',
'dev-async-cake-sos-alert-green-20200430145528404200000004',
'dev-async-cake-violations-blue-20190430233443859800000003',
'dev-async-cake-violations-green-20190430233444271700000004',
'dev-async-fences-blue-20191125231801353800000003',
'dev-async-fences-green-20191125231805370400000004',
'dev-async-soa-blue-20191106235805712900000007',
'dev-async-soa-green-20191106235805476000000006',
'dev-bumblebee-service-blue-20201218094945260500000006',
'dev-bumblebee-service-green-20201218094944444200000005',
'dev-chatnado-blue-20191105192056850500000003',
'dev-chatnado-green-20191105192057445600000004',
'dev-consul-ui-blue-20200211230201252300000002',
'dev-consul-ui-green-20200211230201247100000001',
'dev-consul.blue.20171025223236660900000002',
'dev-consul.green.20171025223234686000000001',
'dev-cx-drive-report-blue-20181107191752263600000008',
'dev-cx-drive-report-green-20181107191752248200000007',
'dev-cx-qa-blue-20171120191230346000000004',
'dev-cx-qa-green-20171120191230134100000003',
'dev-drive-history-blue-20191106235805854900000008',
'dev-drive-history-green-20191106235805340700000005',
'dev-drive-report-blue-20181107191752064200000005',
'dev-drive-report-green-20181107191752098500000006',
'dev-drive-report-http-blue-20181211004820957900000003',
'dev-drive-report-http-green-20181211004821356000000004',
'dev-dvb-blue-20191106232246344700000003',
'dev-dvb-green-20191106232246532700000004',
'dev-dvbrawdataforwarding-blue-20210430011524223500000003',
'dev-dvbrawdataforwarding-green-20210430011524238100000004',
'dev-eks2-asg',
'dev-frontend-router-blue-20180306230617222000000004',
'dev-frontend-router-green-20180306230617222000000003',
'dev-geodecode-blue-20191106013739046900000001']


A=['a','c','g']
B=['a','b','c','d','e']

for arr in arr_from_boto:
    if arr in arr_from_slack:
	    print(arr)