# Docker Setup Instructions for Jupyter Environment with GUI Support

## Prerequisites
Install Docker and Docker Compose on your system:
   - [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - [Docker for Linux](https://docs.docker.com/engine/install/)


## Setup Instructions

![Docker Setup Demo](setupFiles/dockerSetup.gif)
<!-- <video src="setupFiles/dockerSetup.mp4" width="100%" controls muted></video> -->


You can quickly run this environment with just two commands in terminal (command prompt for windows):

1. **Pull the container image** (download the environment):

```bash
docker pull ksucyber/qc-notes:latest
```

**Run the container**

``` bash
docker run -p 8888:8888 -v ./notebooks:/code/Quantum_Cryptography_Notes ksucyber/qc-notes:latest
```

Follow Usage Instructions Below

## Usage Instructions

- Open your web browser and go to: `http://localhost:8888`
- You'll see the Jupyter Lab interface with your notebooks

## Stopping the Environment

When you're done using the environment:

1. Go to the terminal where you started the container
2. Press `CTRL+C` to stop the server

## How it Works
- The setup uses docker containers:
  1. Jupyter container: Runs your notebooks

- The `-v ./notebooks:/code/Quantum_Cryptography_Notes` part of the command creates a folder called notebooks on your computer that links to the environment. Any files you save in Jupyter will be stored there and won't be lost when you stop the container.
## Troubleshooting

1. If you see an error about ports already in use, try different port numbers:
```bash
   docker run -p 8889:8888 ksucyber/qc-notes:latest
```
