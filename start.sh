#!/usr/bin/bash

sudo docker-compose up -d;

python3 ./Django_Project/manage.py runserver;
