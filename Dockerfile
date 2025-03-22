# Use official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /code

# Install system dependencies including X11 and Tkinter
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
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
    qiskit-aer==0.14.2 \
    nbformat==5.10.4
    
RUN pip install Pillow==11.1.0

# Create directory for notebooks
WORKDIR /code

# Copy all contents from the current directory
COPY . .

# Expose Jupyter port
EXPOSE 8888

RUN ["python", "master_page_gen.py"]

# Use custom entrypoint
ENTRYPOINT ["/code/start.sh"]