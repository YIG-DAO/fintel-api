# Using lightweight alpine image
FROM continuumio/anaconda3:2020.11

# Installing packages
RUN apk --no-cache update
RUN apk --no-cache add musl-dev linux-headers g++
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev
RUN apk install -y gcc cmake
#RUN pip3 install conda
#RUN conda env create -f spaghetti-science.yml

# Activate the environment, and make sure it's activated:
#RUN conda activate ynosis
#RUN conda create -n obb python=3.11 -y
#RUN conda activate obb
#RUN pip install openbb
#RUN pip install "openbb[optimization]"
#RUN pip install "openbb[prediction]"
# Set the working directory in the container
WORKDIR /app

#RUN conda activate /app
#RUN conda create -n obb -c conda-forge python=3.10.9 pip pybind11 cmake git cvxpy lightgbm poetry
# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application to the container
COPY . .

# Set the environment variables for Flask
ENV FLASK_APP=server.py
ENV FLASK_ENV=production
EXPOSE 5000

# Run the Flask application
CMD flask --debug run -h 0.0.0.0