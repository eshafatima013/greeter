\# Greeter



A tiny Python web app (built-in `http.server`, no framework) that shows a greeting with my name and a quote of the day. It listens on port 8080.



\## Run with Docker



```bash

docker build -t greeter .

docker run -d -p 8080:8080 greeter

```



Then open http://localhost:8080



Or run the published image straight from Docker Hub:



```bash

docker run -d -p 8080:8080 eshafatima013/greeter:1.1

```

