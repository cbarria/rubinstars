# Rubinstars 🌠

### What it does?

This Project counts the number of stars in 3 specific repositorys then it pushes<br>
a lovely Docker Image with Github Actions and you are set to go Stargazer! 

the repos are...

  * freeCodeCamp/freeCodeCamp
  * 996icu/996.ICU
  * EbookFoundation/free-programming-books
  
you will need Docker to eventually run this complete, 
but you can only run the Python if you have the following dependencies:
    * GyGithub
    * Pyyaml
    
 This was CentOS 7 made with python v3  

## Docker Image can be found here:  
   https://hub.docker.com/repository/docker/cbarria/rubinstars

## QUICK GUIDE:
* For running the stand-alone python code:
  python rubinstar.py

* For building the image run:
  sudo docker build -t rubinstars .

* For running the docker image:
  sudo docker run rubinstars

* For running unit testing:
  python -m unittest rubinstars_test 
