# forecastprophetdocker
Using forecast from Prophet on Docker. 
Just update this code from:
https://towardsdatascience.com/serving-prophet-model-with-flask-predicting-future-1896986da05f

Using this information:
https://pythontechworld.com/issue/facebook/prophet/2138

And finally using flask to expose a port and make a comunication http automatic from Dockerfile RUN. 

Note: using docker don't show results on your computer directy... but you can install all base that can run Prophet... but
this make no sense... just because we are using Docker.
Note: in the future I'll make a cleanup on the code... ^^

#Install
Make sure you have docker and docker-compose and run: docker-compose up --build
You can use api.http ou postman... test.

If you have problem with Docker maybe a possible solution:
   1- Delete all containers: docker rm -vf $(docker ps -aq)
   and after that
   2- Delete all imagens: docker rmi -f $(docker images -aq)

Some times you need to try multiple times run docker-compose up --build,
yes maybe the server is down... have some problems and etc. This is common in
multiples stages of the instalation. This is a pain... 

