# Use official Python image as base
FROM theasp/novnc:latest

# Set working directory
WORKDIR /code

# Install system dependencies including X11 and Tkinter
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3 \
    python3-pip \
    python3-dev \
    python3-tk \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install \
    jupyter \
    notebook \
    jupyterlab \
    qutip \
    matplotlib \
    qiskit==0.45.2 \
    qiskit-aer==0.14.2
    
RUN pip install Pillow==11.1.0

# Create directory for notebooks
WORKDIR /code

# Copy all contents from the current directory
COPY . .

# Expose Jupyter port
EXPOSE 8888
# Expose VNC port
EXPOSE 8080

# Create entrypoint script
RUN echo '#!/bin/bash\n\
/app/entrypoint.sh &\n\
cd /code/Quantum_Cryptography_Notes && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=""\n' > /code/start.sh && \
chmod +x /code/start.sh

# Use custom entrypoint
ENTRYPOINT ["/code/start.sh"]