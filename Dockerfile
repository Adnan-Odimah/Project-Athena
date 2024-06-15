# Use a Python base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file early in the build process
COPY requirements.txt .

# Install system dependencies for audio support and Python dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libsmpeg-dev \
    libsdl1.2-dev \
    pulseaudio \
    alsa-utils \
    alsa-oss \
    xvfb && \
    pip install -r requirements.txt && \
    python -m spacy download en_core_web_md && \
# Copy the source code after dependencies are installed
COPY src/main/ ./src/main/

# Set the environment variable for Pygame to use the virtual framebuffer
ENV DISPLAY=:99

# Start PulseAudio and run the application
CMD pulseaudio --start && Xvfb :99 -screen 0 1024x768x16 & python src/main/main.py