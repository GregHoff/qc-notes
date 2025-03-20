# Docker Setup Instructions for Jupyter Environment with GUI Support

## Prerequisites
Install Docker and Docker Compose on your system:
   - [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - [Docker for Linux](https://docs.docker.com/engine/install/)


## Setup Instructions


You can quickly run this environment without cloning the repository by pulling directly from DockerHub:
```bash
docker pull ksucyber/qc-notes:latest
```

**Run the container**

``` bash
docker run -p 8888:8888 -p 8080:8080 ksucyber/qc-notes:latest
```

Access Jupyter Lab at `http://localhost:8888` and noVNC at `http://localhost:8080/vnc.html` as described in the Usage Instructions section below.

**Note:** When running this way, any changes you make will be lost when the container stops. For persistent storage, use the volume mounting option:

``` bash
# Run with persistent storage
docker run -p 8888:8888 -p 8080:8080 -v ./notebooks:<any_path_in_host_to_save_data> ksucyber/qc-notes:latest
```

## Usage Instructions

1. Access Jupyter Lab:
   - Open your web browser and go to: `http://localhost:8888`
   - You'll see the Jupyter Lab interface with your notebooks

2. For viewing the simulation in Learning Object "22.4 The E91 Protocol":
   - Before running the simulation cells, open a new browser tab and go to: `http://localhost:8080/vnc.html`
   - Keep this tab open while running the simulation cells
   - The simulation will appear in this virtual desktop window
   - If you don't open this window before running the simulation, you won't be able to see the visualization

## How it Works
- The setup uses two containers:
  1. Jupyter container: Runs your notebooks and Tkinter applications
  2. noVNC container: Provides the virtual display server and web interface
- The simulation in LO 22.4 will display its GUI in the noVNC window

## Troubleshooting

1. If you can't see the simulation:
   - Make sure you opened `http://localhost:8080` before running the simulation cells
   - Keep the noVNC tab open while running the simulation
   - Try rerunning the notebook cells
   - If still not working, restart the Jupyter kernel and try again

2. If ports are already in use, modify the port mappings in docker-compose.yml:
```bash
   docker run -p 8889:8888 -p 8081:8080 ksucyber/qc-notes:latest
```
