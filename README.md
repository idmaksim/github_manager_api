# GitHub Management API

## Project Description

This project is an API for managing your GitHub repositories. It allows you to perform various actions such as creating, updating, deleting repositories and more, all through a convenient RESTful interface. The API is built using FastAPI, making it fast, reliable, and easy to use. 

## Features
- **Repository Management**: Create, update, and delete repositories.
- **Branch Management**: Create, delete, and manage branches. 
- **Commit History**: View commit history and details.
- **User Management**: Get user information and manage collaborators.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- GitHub account
- Personal Access Token from GitHub with the necessary permissions

## Running project

### to run this project you need:
 - install requirements from requirements.txt
 - dev or release mode: fastapi [dev or run] src/app.py --reload --port 8090
### or
- install docker
- cmd: docker build -t [name of your image] .
- cmd: docker run -p [port:port] -d [optional if you dont need to see logs] --name [name of your container] [name of image]
