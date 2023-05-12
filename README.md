# Udacity Universal Quotes Generator

This App generates a quote based on an emotion that you specify
and it can also translate into another language
of your choice.

Have fun playing!

I used [Streamlit](https://streamlit.io/) for my capstone project. Its a cool framework to build fast data apps!

# Project Components
1. Docker image - krithika1811/udacity-translator
2. Travis CI
3. Kubernetes for container orchestration

# Project setup - local

1. Clone git repo git@github.com:krithika1811/udacity-capstone-translator.git
2. ```code
    docker pull krithika1811/udacity-translator:latest
   ```
3. Copy base64 encoded `TOKEN` from `deploy/env-configmap.yaml`
4. ```code
    docker run -e TOKEN="<REPLACE TOKEN FROM STEP 3>" -p 8501:8501 krithika1811/udacity-translator:latest
   ```
5. Access `http://0.0.0.0:8501` to play udacity universal quotes translator

# Project - public access URL

Access URL - `http://a2b18c26745fc41c6a973ec4590aea11-130442488.us-east-1.elb.amazonaws.com:8501/`


# Screenshot Folder
It contains the screenshots of :
    1.Dockerhub
    2.Travis
    3.Front page of the app
    4.kubectl get pods and kubectl describe services
    5.kubectl logs


