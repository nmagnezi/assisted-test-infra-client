import logging
import yaml
import requests

LOG = logging.getLogger(__name__)


def download_yaml(url):
    LOG.info('Download Starting...')
    r = requests.get(url)
    filename = url.split('/')[-1]  # this will take only -1 splitted part of the url
    with open(filename, 'wb') as output_file:
        output_file.write(r.content)

    LOG.info('Download Completed!!!')

def read_yaml(file):
    with open(file) as file:
        try:
            data = yaml.safe_load(file)
            # for key, value in data.items():
                # print(key, ":", value)
        except yaml.YAMLError as exception:
            print(exception)
    print(data['tests'][10])
    # for i in data['tests']:
    #     print(i['as'])
    return data
