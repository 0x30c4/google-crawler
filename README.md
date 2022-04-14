# Google Crawler
This api will parse and organizes the search results from google. In the backend the the API usage pyppeteer in a docker container to parse the google search result.<br>

## Here's the Swagger UI for the API EndPoint.
### The live demo version which is running on my server. And it has a limit 6 request per minute.
Live Demo -> [https://crawler.0x30c4/v1/docs](https://crawler.0x30c4.dev/v1/docs) <br>
[Live Demo Brach](https://github.com/0x30c4/google-crawler/tree/prod-version/demo-on-coco)


# Version.
* [Production](#prod_ver)
* [Development](#dev_ver) 

# The Application Architecture
<img src="https://raw.githubusercontent.com/0x30c4/google-crawler/main/images/Overview.png">

## Built With.
* [Docker](https://www.docker.com) - Platform and Software Deployment
* [FastApi](https://fastapi.tiangolo.com/) - Backend Frame-work.
* [Redis](https://fastapi.tiangolo.com/) - Caching DataBase.
* [Pyppeteer](https://github.com/pyppeteer/pyppeteer) -  Headless chrome/chromium automation library (unofficial port of puppeteer) 

### Prerequisites. 
* [Docker](https://www.docker.com) - Platform and Software Deployment
* [make](https://tldp.org/HOWTO/Software-Building-HOWTO-3.html) - As the Build System.
	
# Production Version.
<a name="prod_ver">
How to run the Production version.
</a>

To run the Production version first install [Docker](https://www.docker.com) and [make](https://tldp.org/HOWTO/Software-Building-HOWTO-3.html)
on you system and then clone the repo.

You can change the environment variables from the <code>env/.env.prod</code>
#### Change your user to root.

```bash

# Clone the repo
$ git clone https://github.com/0x30c4/google-crawler.git
$ cd google-crawler

# Run this command to build the production on image.
$ make build-prod

# Run this command to run the production version.
$ make run

# To stop it.
$ make stop-prod
```

# Development Version.
<a name="dev_ver">
How to run the Development version.
</a>
To run the Production version first install [Docker](https://www.docker.com) and [make](https://tldp.org/HOWTO/Software-Building-HOWTO-3.html)
on you system and then clone the repo.

You can change the environment variables from the <code>env/.env.dev</code>
#### Change your user to root.

```bash

# Clone the repo
$ git clone https://github.com/0x30c4/google-crawler.git
$ cd google-crawler

# Run this command to build the development image.
$ make build-dev

# Run this command to run the development version.
$ make run-dev

# To stop it run.
$ make stop-dev
```
