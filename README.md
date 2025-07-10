# ADvisor


ADvisor tool allows the exploration of different applicabilty domain (AD) strategies to find the most suitable for each use case. Once the user has identified the preferred AD methodology, this can be applied to any query dataset. This repository provides necessary Python scripts for AD search and application, using a predefined environment and dependencies. 

## Installation

To set up the required environment, use the provided YAML file:

```sh
conda env create -f env.yml
```

Then, activate the environment:

```sh
conda activate env
```

## Usage

### 1) AD search

Run the AD search script with Python, specifying the required inputs:

```sh
python Compare_AD_Strategies.py -train Train.csv -test Test.csv -repres RDKit-descriptors -mt regressor -test_tvc True -train_tvc True -test_pvc Pred -nj 4 -out Out1.csv
```
Please note that within ADvisor AD strategy the similarity formula used for regressors and classifiers is the one that performed best on average, respectively (we refer the user to the paper for further details). 

### 1) AD application

Run the calculate AD script with Python, specifying the required inputs:

```sh
python Calculate_AD.py -train Train.csv -test Test.csv -query Query.csv -repres RDKit-descriptors -ad ADvisor_AD_th-0.8_a-0.25_b-0.25_c-0.25_d-0.25 -mt regressor -test_tvc True -train_tvc True -test_pvc Pred -query_pvc Pred -nj 4 -out Out2.csv
```
Please note that the desired AD strategy to apply must be written in the same format returned by the AD search. 



### Input
- The input files must be in CSV format and contain a column named `SMILES`, which represents the molecular structures. This column is necessary in all input files.
- For the AD search, train and test set used to derive and validate the model must be used. For the AD application, both train and test set are necessary, together with the desired query set containing compounds to label as IN or OUT AD according to the selected strategy.
- The train set must contain a column storing the experimental value or class of compounds. The test set must contain a column storing the experimental value or class, and a column storing the predicted value or class. The query set must contain a column storing the predicted value or class.
- Three CSV files (Train.csv, Test.csv, Query.csv) are included in the repository for testing purposes.

### Output
- The AD search script will generate a CSV file with the evaluated AD methodologies ranked, together with their performance on IN and OUT subsets. 
- The AD application script will generate a CSV file containing the query smiles, the predictions for each query compound and a column storing the IN/OUT AD label according to the selected strategy.

## Dependencies

All necessary dependencies are included in `env.yml`.
