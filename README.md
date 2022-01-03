# Github Pull Request Reporting
This repo is used to generate and send reports on pull requests in Github repositories. The reports are in html format and emailed to a list of recipients.

## Getting Started

### Prerequisites

1. The project needs a Github access token, so you will need to set that up.
2. Emails are sent via yagmail, so you will need to set up an app password in google.
    * see here: https://github.com/kootenpv/yagmail
3. Install python 3.8 or greater
4. Install dependencies with 
```
pip install -r requirements.txt
```
5. create a secrets.json file with the following format:
```
{
    "github" : {
        "access_token" :"<token>"
    },
    "gmail" :{
        "password" : "<password>"
    }
}
```
6. create a config.json file with the following format:
```
{
    "prior_weeks" : 1,
    "github" : {
        "repo" : "<repo_name>"
    },
    "addresses" :{
        "from" : "<sending address",
        "to" : [<list of recipients>]
    }
}
```

### Running the code
You can now run the code with:
``` 
python3 main.py --config-file=config.json --secrets-file=secrets.json
```
### Docker
You can also build using the provided Dockerfile and run that with:
```
docker run <image_name> --config-file=config.json --secrets-file=secrets.json
```

## Output
Running the above will result in the creation of "report.html" which is then emailed to the recipients. An example has been provided here with "example-report.html"

### Comment Total
The last column in the table is labeled "Comment Total" and contains the summation of comments from both the issue, and the review associated with the pull requests. This is the first step in providing useful insight into which pull request is most interesting, or should be viewed first.