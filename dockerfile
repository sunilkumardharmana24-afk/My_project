# 1️⃣ Use official Python base image
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency files first (for caching)
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest pytest-playwright allure-pytest

# 5️⃣ Install Playwright browsers
RUN playwright install --with-deps

# 6️⃣ Copy project files
COPY . .

# 7️⃣ Default command: run tests with Allure reporting
CMD ["pytest", "-n", "4", "--alluredir=allure-results", "--disable-warnings"]