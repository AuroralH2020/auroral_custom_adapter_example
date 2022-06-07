# 
FROM python:3.9-slim
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy project files
COPY ./app /app
# RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4444"]
