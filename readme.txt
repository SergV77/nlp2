mkdir my_project
 $ cd my_project
 $ virtualenv venv

source venv/bin/activate
 $ pip install flask


$ docker pull busybox
$ docker run busybox
$ docker ps -a
$ docker run -it busybox sh
$ docker rm 305297d7a235 ff0a5c3750b9
$ docker rm $(docker ps -a -q -f status=exited)

docker build -t my_flask_app:v0.1 my_flask_app/
$ docker duild -t my_test:v0.2 my_test/


git config --global core.autocrlf false