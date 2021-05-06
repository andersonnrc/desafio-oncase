#!/bin/bash

python delete_documents.py

cd motoo

scrapy crawl motoo-crawler

cd ../mototour

scrapy crawl mototour-crawler

cd ../tudodemotos

scrapy crawl tudodemoto-crawler


