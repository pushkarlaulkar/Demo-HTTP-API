# HTTP-API-Demo

This is a demo of an HTTP API creation using Django Framework

The working demo can be found at this [link](https://demo-http-api.herokuapp.com/http_api/v1/books/all). Use Firefox browser to view the JSON outputs.

The demo has been on hosted on Heroku. Kindly wait for some time to load the API website since Heroku puts your website to sleep after 30 minutes of inactivity.

When the above link is opened the below output is expected. It shows a JSON output of details of 6 books which is a random data to showcase the implementation of API.

![Output](https://i.ibb.co/dMSkLCN/Capture.png)

If details of only a specific book is required we can replace the 'all' keyword in the link to a number between 0-5 which corresponds to the respective ID of the book.

For e.g. if the details of the book which has id 3 is required enter the link as [book-3](https://demo-http-api.herokuapp.com/http_api/v1/books/3). The below output will be shown

![Output](https://i.ibb.co/RgD8jVC/Capture.png)

If any number greater than 5 is put it will display a message "No such book, Please enter a value from 0-5 or 'all' to list all books".

![Output](https://i.ibb.co/wpdwx3W/Capture.png)

If a string is passed it will display a message "Please enter a numeric value from 0-5 or 'all' to list all books".

![Output](https://i.ibb.co/850DYX8/Capture.png)

########################################################################################
--**Docker Implementation**

The Dockerfile for this project is available.

The Docker image is available publicly at https://hub.docker.com/repository/docker/plaulkar/http-api

To run a container from this image, enter below command

docker run -d --name http-api -p 8000:8000 plaulkar/http-api:latest

Container name is http-api, port at which both the host and the container will listen to is 8000.

Once the container is deployed enter below link to view the API

http://[localhost or host ip]:8000/http_api/v1/books/all to view all books

To get details of books of id between 0-5 visit http://[localhost or host ip]:8000/http_api/v1/books/[id]

########################################################################################
--**Kubernetes Implementation**

Kubernetes deployment and service YAML file is also available.

The service has been deployed as node port service listening on port 30000.

To run a kubernetes deployment enter below command

kubectl create -f http-api-k8s-deployment.yml

This will create a deployment with 1 replica.

To create a service enter below command

kubectl create -f http-api-k8s-service.yml

This will create a service of type node port listening on port 30000.

Once the deployment and the service is deployed enter below link to view the API

http://[localhost or host ip]:30000/http_api/v1/books/all to view all books

To get details of books of id between 0-5 visit http://[localhost or host ip]:30000/http_api/v1/books/[id]
