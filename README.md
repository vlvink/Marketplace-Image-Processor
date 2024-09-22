# Marketplace-Image-Processor

The project is a solution to an e-commerce problem: developing a system for processing photos from
product cards on marketplaces, which performs the following actions:
 - Removing the background
 - Replacing the background
 - Description generation

## Installation
To run this project, you'll need to set up a Python environment and install the necessary dependencies.
### Prerequisites
Make sure you have Python 3.10 or higher installed.
1. Clone the repository:
```commandline
git clone https://github.com/vlvink/Marketplace-Image-Processor.git
cd marketplace-image-processor
```
2. Install the requirements
```commandline
poetry install
```

## Running the Code
To run the code, you need to configure Streamlit app
```commandline
streamlit run setup.py
```

## Project Organization


    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │   ├── params         <- Model's parameters in .pth files  
    │   └── predictions    <- Model's predictions: intermediate model responses
    │
    ├── notebooks          <- Jupyter notebooks. Test code, training code
    │
    ├── setup.py           <- Launches the Streamlit app to demonstrate how the models work
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
