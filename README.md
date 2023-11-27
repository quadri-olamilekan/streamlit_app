### Assuming that you have installed docker in your system, if not then please refer the link below to install docker 
https://docs.docker.com/get-docker/

### For running streamlit app locally first build docker file by running below command. Make sure you are in streamlit_app folder
docker build -t my_streamlit_app .

### Then check if the the docker image is created by running command below. If it is created then you will see my_streamlit_app image.
docker image ls

### Now to run streamlit app locally run the following command
docker run -p 8501:8501 my_streamlit_app

### After running docker file use localhost url to use streamlit app
http://localhost:8501/

![alt text](https://verified.sertifier.com/en/verify/35485319899531/?ref=email#:~:text=Certificate%20PDF-,Certificate,-PNG)
