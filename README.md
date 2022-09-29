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


Endpoints:
look at api.http for exemples aplications. 
'/forecast_like_katana-ml': make a request using a needed size of horizon
'/newdata': add new data to archive .csv ...file that will be use on Prophet localy and don't need fit again.   
'/forecast_json': use only the json request and return another json as reponse.

If you want to see the original code as working from the original site look at 'prophetlikeKatana.py'. And make sure that you comment line 33 from Dokerfile an uncomment line 34. The endpont '/katana-ml/api/v1.0/forecast/ironsteel" will be up on the same port. I comented multiples lines where found 'plot' just becouse this don't work on Docker. Use the command "docker-compose up --build" after.

Create too a basic Flag with print() to make difference between from my code and the original code. 'FLASK ORING' and 'FLASK CHANGED'. First the original. 

If you have problem with Docker maybe a possible solution:
   1- Delete all containers: docker rm -vf $(docker ps -aq)
   and after that
   2- Delete all imagens: docker rmi -f $(docker images -aq)

Some times you need to try multiple times run docker-compose up --build,
yes maybe the server is down... have some problems and etc. This is common in
multiples stages of the instalation. This is a pain... 

