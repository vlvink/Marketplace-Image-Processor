# Marketplace-Image-Processor

The project is a solution to an e-commerce problem: developing a system for processing photos from
product cards on marketplaces.

It performs the following actions:
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
cd Marketplace-Image-Processor
```
2. Install the requirements
```commandline
poetry install
```
3. Setting the poetry environment
```commandline
poetry shell
```

## Running the Code
**Before running** code [download](https://drive.google.com/file/d/1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ/view) file `u2net.pth` and put it into `models/params/u2net/`

To run the code, you need to configure Streamlit app
```commandline
streamlit run src/start_page.py
```
For stopping session press the keyboard shortcut **Ctrl+C** in the terminal.

## Demos
#### Web app UI interface
<image src="data/outsourceimg/uidemo.jpg" alt="UI interface">

#### Intermediate results
<image src="data/outsourceimg/intermres.jpg" alt="UI interface intermediate">

#### Final output
<image src="data/outsourceimg/FinalDemo.png" alt="Final output image">

## Project Organization


    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project
    ├── data
    │   └── bg_themes      <- Background image styles.
    │   │   ├── dark_bg_theme.JPG      <- Dark background image file
    │   │   └── light_bg_theme.JPG     <- Light background image file
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │   ├── params         <- Model's parameters in .pth files
    │   │   ├── blip       <- Pretrain configuration for BLIP model
    │   │   ├── u2net      <- Directory for u2net parameters
    │   │   
    │   └── predictions    <- Model's predictions: intermediate model responses
    │
    ├── notebooks          <- Jupyter notebooks. Test code, training code
    │
    ├── src                <- Source code for use in this project
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── applications   <- Code with applications for Streamlit app
    │   │   └── apply_bg.py
    │   │
    │   ├── start_page.py  <- Launches the Streamlit app to demonstrate how the models work
    │   │
    │   ├── data           <- Scripts to modify data
    │   │   └── image_processing.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │              predictions
    │   │   ├── blip       <- Code for initializing and using BLIP model (Image2Text)
    │   │   │   ├── blip_init.py
    │   │   │   └── blip_model_utils.py
    │   │   │
    │   │   ├── u2net      <- Code for initializing and using U2-Net model (Semantic segmentation)
    │   │   │   ├── u2net_init.py
    │   │   │   ├── u2net_model_utils.py
    │   │   │   ├── u2net_model.py
    │   │   │   └── u2net_processor.py
    │   │   │
    │   │   ├── madlad400  <- Code for initializing and using MADLAD400 model (Translating)
    │   │   │   ├── madlad400_init.py
    │   │   │   └── translate.py
    │
    └── tox.ini            <- tox file with settings for running tox
