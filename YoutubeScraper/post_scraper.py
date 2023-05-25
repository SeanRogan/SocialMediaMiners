# RESEARCH PROCESS
# connect to api
# search for topic
# collect pages
# iterate through and collect specific video links
# save info
import json
import logging
# SCRAPER PROCESS
# connect to api
# search through saved info
# scrape page
# save raw results and send to analysis

# ANALYSIS PROCESS
# analyze video transcript and extract data

import os
from constants import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
api_service = 'youtube'
api_version = 'v3'
api_key = settings.YOUTUBE_API_KEY


def connect(service, version, key):
    logging.info(f'connecting to {api_service} api version {api_version}')
    return build(service, version, developerKey=key)


def search(query, pages=1):
    results = []
    try:
        assert isinstance(query, str)
    except AssertionError as err:
        logging.warning(str(err))
    finally:
        api = connect(api_service, api_version, api_key)
        logging.debug('api connected' + str(api))
        try:
            logging.debug('first api call')
            first_request = api.search().list(part='id,snippet',
                                              type='video',
                                              maxResults=50,
                                              order='relevance',
                                              q=query,
                                              fields='nextPageToken,items(id(videoId), snippet(publishedAt,channelId,channelTitle,title,description))')
            response = first_request.execute()
            next_page_token = response['nextPageToken']
            results.append(response)
            if pages > 1:
                for i in range(pages-1):
                    request = api.search().list(part='id,snippet',
                                                type='video',
                                                maxResults=50,
                                                q=query,
                                                order='relevance',
                                                fields='nextPageToken,items(id(videoId), snippet(publishedAt,channelId,channelTitle,title,description))',
                                                pageToken=next_page_token)
                    response = request.execute()
                    next_page_token = response['nextPageToken']
                    results.append(response)
        except HttpError as err:
            logging.warning(str(err))
            return 'an HttpError occurred'
        finally:
            return response_handler(results)


def response_handler(json_data):
    data = {}
    api = connect(api_service, api_version, api_key)
    for i in json_data:
        next_page_token = i['nextPageToken']
        items = i['items']
        for item in items:
            results = {}
            video_id = item['id']['videoId']
            results['video_id'] = video_id
            channel_title = item['snippet']['channelTitle']
            video_title = item['snippet']['title']
            results['published_at'] = item['snippet']['publishedAt']
            results['channel_id'] = item['snippet']['channelId']
            results['channel_title'] = channel_title
            results['video_title'] = video_title
            results['description'] = item['snippet']['description']
            req = api.videos().list(
                part='statistics, contentDetails',
                id=video_id,
                fields='items(statistics(viewCount, likeCount, commentCount), contentDetails(duration))')
            res = req.execute()
            results['duration'] = res['items'][0]['contentDetails']['duration']
            stats = res['items'][0]['statistics']
            if 'viewCount' in stats:
                results['views'] = stats['viewCount']
            if 'likeCount' in stats:
                results['likes'] = stats['likeCount']
            if 'commentCount' in stats:
                results['comments'] = stats['commentCount']
            data[f'{channel_title} presents: {video_title}'] = results

    return data


# analyze comment threads and extract sentiment
if __name__ == '__main__':
    print(search('ukraine war news', 2))
