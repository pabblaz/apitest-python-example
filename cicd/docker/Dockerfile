FROM python:3.11.8-slim
LABEL maintainer='pablso@hotmail.com'

# Install basic packages
RUN apt update && \
    apt install -y git

# Set working directory
WORKDIR /tests

# Create user and set ownership and permissions as required
RUN adduser --system automator --disabled-password --uid 1001 && \
    chown -R automator /tests && \
    chown -R automator /usr/local

USER automator

RUN pip install --upgrade --use-deprecated=legacy-resolver pip coverage

# Set Environment variables
ENV LANG C.UTF-8


# Copy repository files and install project dependencies
COPY --chown=automator . .

# Install dependencies
RUN pip install -r requirements.txt


RUN mkdir -p logs report