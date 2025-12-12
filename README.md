# EDA Project - Data Science & AI Bootcamp - 2025/12

This is a project in exploratory data analysis (EDA) done at neue fische Academy in December 2025. The data set at stake is about house prices in King County in Washington State/ USA. 

Moreover, the project is divided into two parts: 

1. Three general hypotheses about the data set: tested and visualized by plots.
2. Recommendations to a fictional stakeholder active in the real estate market.

Part 1 is contained in notebook 'EDA', while Part 2 is contained in notebook 'Recommendations'. 

The project is written in Jupyter Lab and can be run via a virtual environment as described below. 

## Folder Structure

- **`src`** contains .py file to clean raw data
- **`plots`** contains all relevant plots as `.png` generated throughout the project
- **`presentation`** contains the final presentation as `.pdf`

## File Structure

- **`EDA.ipynb`** contains the notebook for Part 1 of the project
- **`stakeholder_recommendations.ipynb`** contains the notebook for Part 2 of the project
- **`requirements.txt`** contains all required software versions for this project
- **`column_names.md`** provides an explanation of column names in data set


## Setup

### **`MAC`**  

 Install the virtual environment and the required packages by following commands:

    ```
    pyenv local 3.11.3
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :


- `Step_1:` Update Chocolatey and install Node by following commands:
    ```sh
    choco upgrade chocolatey
    choco install nodejs
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
  
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
 

 **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

   ```Bash
   python.exe -m pip install --upgrade pip
   ```
