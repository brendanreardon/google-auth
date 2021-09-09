# Template for google-auth
This is a template repository for projects that want to use Google Cloud application default credentials with Python. Specifically, code exists to support requests made to the [Terra API](https://api.firecloud.org/) as well as initialize BigQuery and Google Cloud storage clients.

## Installation
## System requirements
To use this repository, you must have the following set up on your system
- [Google Cloud SDK](https://cloud.google.com/sdk/)
- Python 3

Google Cloud and Terra use [Google Cloud SDK](https://cloud.google.com/sdk/) to manage authentication. The [application default credentials](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) will be used. **Please walk through Google's wonderful install and set up documentation if you have not**. To login and set an application default, make sure that you've run the following,
```bash
gcloud auth login
gcloud auth application-default login
```

You may need to export your google cloud auth token, add this to your bash profile:
```bash
export GCS_OAUTH_TOKEN=`gcloud auth application-default print-access-token`
```

### Download
This repository can be downloaded through GitHub by either using the website or terminal. To download on the website, navigate to the top of this page, click the green `Clone or download` button, and select `Download ZIP` to download this repository in a compressed format. To install using GitHub on terminal, type 

```bash
git clone https://github.com/brendanreardon/google-auth.git
cd google-auth
```

### Python dependencies
This template uses Python 3.9. We recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) and running Python with either [Anaconda](https://www.anaconda.com/download/) or  [Miniconda](https://conda.io/miniconda.html). 

Run the following from this repository's directory to create a virtual environment and install dependencies with Anaconda or Miniconda,
```bash
conda create -y -n template python=3.9
conda activate template
pip install -r requirements.txt
```

Or, if using base Python, 
```bash
virtualenv venv
source activate venv/bin/activate
pip install -r requirements.txt
```

To make the virtual environment available to jupyter notebooks, execute the following code while the virtual environment is activated,
```bash
ipython kernel install --user --name=template
```
Replace `template` with your preferred name of the virtual environment.
