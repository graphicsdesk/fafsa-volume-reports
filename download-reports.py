from aiohttp import ClientSession
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import asyncio
import aiofiles
import os

ROOT = 'https://studentaid.gov'
OUTPUT_DIR = './raw-files/'
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensures OUTPUT_DIR exists


async def download_file(client, url):
    '''
    Downloads a file and stores it in OUTPUT_DIR.
    Returns the full filename.
    '''

    # Check if file already exists
    filename = OUTPUT_DIR + os.path.basename(url)
    if os.path.isfile(filename):
        return filename

    # Make the request
    async with client.get(url) as response:
        if response.status == 200:
            f = await aiofiles.open(filename, mode='wb')
            await f.write(await response.read())
            await f.close()
            return filename
        else:
            print('Failed:', response)


async def download_all_options(options):
    '''
    Downloads all files in the dropdown menu in parallel.
    Returns a dictionary that maps a time period (e.g. 2020-2021 Q1) to
    the filename.
    '''
    async with ClientSession() as client:
        tasks = []
        for option in options[:10]:
            url = ROOT + option['value']
            time_period = option.text.replace(',', '')  # Standardizes format
            tasks.append((time_period, download_file(client, url)))
        return [(time_period, await f) for time_period, f in tqdm(tasks)]


def download_reports():
    # Download and parse the page
    response = requests.get(
        ROOT + '/data-center/student/application-volume/fafsa-school-state')
    soup = BeautifulSoup(response.content, 'lxml')

    # Find the dropdown menu, send all options into our downloader
    dropdown = soup.find(id='gourl1')
    return dict(asyncio.run(download_all_options(dropdown.find_all('option'))))


if __name__ == '__main__':
    print('Downloaded files:', download_reports())
