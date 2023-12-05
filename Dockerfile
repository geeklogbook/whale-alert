FROM apache/airflow:2.7.2
USER root

# Install required system packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user
USER airflow

# Set the working directory in the container
WORKDIR /usr/local/airflow

# Create and activate a virtual environment
RUN python3 -m venv venv
ENV PATH="/usr/local/airflow/venv/bin:$PATH"

# Install additional Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your DAG file
COPY dags/whale-alert.py /opt/airflow/dags/whale-alert.py