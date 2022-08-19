# 

## Prerequisites
Before you can start performing Python 3 automation testing using pytest, you would need to:

Install the latest Python build from the official website. We recommend using the latest version.
Make sure pip is installed in your system. You can install pip from here.
Download the latest Selenium Client and its WebDriver bindings from the official website. Latest versions of Selenium Client and WebDriver are ideal for running your automation script on LambdaTest Selenium cloud grid.
Install virtualenv which is the recommended way to run your tests. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules.
```
pip install virtualenv
```
Installing Selenium Dependencies And Tutorial Repo
Step 1: Clone the LambdaTest’s pytest-selenium-sample repository and navigate to the code directory as shown below:

```
git clone https://github.com/LambdaTest/pytest-selenium-sample
cd pytest-selenium-sample
```
Step 2: Create a virtual environment in your project folder the environment name is arbitrary.

```
virtualenv venv
```

Step 3: Activate the environment.

```
source venv/bin/activate
```
Step 4: Install the required packages from the cloned project directory:

```
pip install -r requirements.txt
```
Setting Up Your Authentication
Make sure you have your LambdaTest credentials with you to run test automation scripts. You can get these credentials from the LambdaTest Automation Dashboard or by your LambdaTest Profile.

Step 5: Set LambdaTest Username and Access Key in environment variables.

For Linux
```
export LT_USERNAME="YOUR_USERNAME" 
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```
For Windows
```
set LT_USERNAME="YOUR_USERNAME" 
set LT_ACCESS_KEY="YOUR ACCESS KEY"

```



```

```



## Run your Test

Configuration Of Your Test Capabilities
Step 6: In the python script, you need to update your test capabilities. In this code, we are passing browser, browser version, and operating system information, along with LambdaTest Selenium grid capabilities via capabilities object.



Step 1: Clone the Java-TestNG-Selenium Repository.

```
git clone https://github.com/LambdaTest/Java-TestNG-Selenium.git
```

Step 2: Inside the Java-TestNG-Selenium folder, Check if you have all the necessary packages,and update them.

```
cd Java-TestNG-Selenium
mvn versions:display-dependency-updates
```

Step 3: Export the Lambda-test Credentials. You can get these from your automation dashboard.

<p align="center">
   <b>For Linux/macOS:</b>:
 
```
export LT_USERNAME="YOUR_USERNAME"
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```
<p align="center">
   <b>For Windows:</b>

```
set LT_USERNAME="YOUR_USERNAME"
set LT_ACCESS_KEY="YOUR ACCESS KEY"
```

### Executing Tests

1. To run single test.

```
pytest -s tests/lt_sample_todo.py
```

2. To run parallel tests.

```
pytest --workers 2 -s tests/lt_sample_todo.py
```

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.