#!/bin/bash

#This is to clone the app
clone(){
        echo "Cloning the Django app..."
        if [ -d "flask-app" ]; then
                echo "The code directory already exists. Skipping clone."
        else
                git clone https://github.com/md-taha/flask-app.git || {
                        echo "Failed to clone the code."
                        return 1
                }
        fi
}

install_requirements(){
        apt-get update
        apt-get install -y docker.io
}

deploy(){
        docker login
        docker pull taha2606/test_repo:latest
        docker run -dp 8000:8000 taha2606/test_repo:latest
}

if ! clone; then
        cd flask-app || exit 1
fi

if ! install_requirements; then
        exit 1
fi

if ! deploy; then
        echo "deployment failed"
        exit 1
fi
