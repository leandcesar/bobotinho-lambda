[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Bobotinho Lambdas
Complementary Lambda functions to chatbot Bobotinho.

## ℹ️ Introduction
**reset-daily**: routinely invoked Lambda function to connect to AWS RDS Postgres and reset daily cookies.

### ‎💻 Technologies
- Serverless compute service with [**AWS Lambda**](https://aws.amazon.com/lambda/)
- Python Serverless Microframework for AWS with [**Chalice**](https://aws.github.io/chalice/)
- Python utilities for AWS Lambda with [**Lambda Powertools Python**](https://awslabs.github.io/aws-lambda-powertools-python)
- Relational Database with [**PostgreSQL**](https://www.postgresql.org/)
- PostgreSQL database adapter with [**Psycopg 2**](https://www.psycopg.org/)

### ‎🧰 Dev tools
- Code formatter with [**Black**](https://github.com/psf/black)
- Style guide with [**flake8**](https://flake8.pycqa.org/en/latest/)
- Tests with [**pytest**](https://docs.pytest.org/en/6.2.x/)
- Pre-commit hooks with [**pre-commit**](https://pre-commit.com/)


## 🏁 Getting Started
It is assumed that you have:
- [**AWS**](https://aws.amazon.com/) account.
- [**AWS CLI**](https://aws.amazon.com/cli/) installed and credentials configured on `~/.aws`.
- [**Python 3.8+**](https://www.python.org/) installed.
- [**Pip**](https://pip.pypa.io/en/stable/) installed.

```bash
$ aws --version
$ python3 --version
$ pip3 --version
```

### ⚙️ Configuring

After clone this repo, create `.env` file in your `/bobotinho-lambdas` directory. Add the database credentials after the `=`.

```
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASS=your-database-password
DB_HOST=your-database-host
DB_PORT=your-database-port
```

### ▶️ Run 

The standard library as of Python 3.3 comes with a concept called "Virtual Environment"s to keep libraries from polluting system installs or to help maintain a different version of libraries than the ones installed on the system.

Execute the following commands in your `/bobotinho-lambdas` directory:

```bash
$ python3.8 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements-dev.txt
$ chalice local
```

### 🧪 Test

Execute the following commands in your `/bobotinho-lambdas` directory:

```bash
$ pytest tests/ --cov
```

### 🚀 Deploy

Execute the following commands in your `/bobotinho-lambdas` directory:

```bash
$ chalice deploy --stage prod
```
