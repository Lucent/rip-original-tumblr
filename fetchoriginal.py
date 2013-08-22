import oauth2 as oauth
import time
import os
import sys

from tumblr import TumblrClient


def lister(client, count, params={}):
	client.get_blog_posts()

	total = 0
	while True:
		time.sleep(1)
		print "# REQUEST " + str(total)
		params['offset'] = total
		json_response = client.get_blog_posts(request_params=params)
		for post in json_response['response']['posts']:
			total += 1
			if total > count:
				raise StopIteration
			yield post


def main():
	subdomain = sys.argv[1]

	text = open('text.txt', 'w')
	photo = open('photo.txt', 'w')
	quote = open('quote.txt', 'w')
	link = open('link.txt', 'w')
	chat = open('chat.txt', 'w')
	audio = open('audio.txt', 'w')
	video = open('video.txt', 'w')
	answer = open('answer.txt', 'w')

	bigphoto = open('bigphotos.txt', 'w')

	hostname = subdomain + '.tumblr.com'

	consumer_key = 'Mri3sRuQiYcsM0PdemF92w4oJT6MY6MEhGxfoxADHvu8cXzJi8'
	consumer_secret = 'eDsK30RRKgP7gdbeGcwfIOe0v4sc7AgkKByITaKlThy85I9IjX'

	access_key = 'ACCESS_KEY'
	access_secret = 'ACCESS_KEY'

	consumer = oauth.Consumer(consumer_key, consumer_secret)
	token = oauth.Token(access_key, access_secret)

	params = {
#	   'type': 'photo',
	}

	client = TumblrClient(hostname, consumer, token)
	for post in lister(client, 27000, params):
		if (not 'source_title' in post) or (post['source_title'] == subdomain):
			eval(post['type']).write(post['post_url'] + '\n')
			print post['type'] + '\t' + post['post_url']
			if (post['type'] == 'photo'):
				bigphoto.write(post['photos'][0]['original_size']['url'] + '\n')


if __name__ == '__main__':
	main()
