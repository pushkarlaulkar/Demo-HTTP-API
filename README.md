# HTTP-API-Demo

This is a demo of an HTTP API creation using Django Framework

The working demo can be found at this [link](https://demo-http-api.herokuapp.com/http_api/v1/books/all)

When the above link is opened the below output is expected. It shows a JSON output of 6 books which is a random data to showcase the implementation of API.

![Output](https://i.ibb.co/dMSkLCN/Capture.png)

If details of only a specific book is required we can replace the 'all' keyword in the link to a number between 0-5 which corresponds to the respective ID of the book.

For e.g. if the details of the book which has id 3 is required enter the link as [book-3](https://demo-http-api.herokuapp.com/http_api/v1/books/3). The below output will be shown

![Output](https://i.ibb.co/RgD8jVC/Capture.png)
