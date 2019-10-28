
[![Build Status](https://travis-ci.com/AminKaram/FYP.svg?token=WUKwGEsuG3EUbwasy9R8&branch=master)](https://travis-ci.com/AminKaram/FYP)  
# ABA+G  
  
**Note:** Basic knowledge of argumentation theory is assumed throughout this documentation. If you are unfamiliar with this it's recommended that you read the material in the useful reading section before continuing.

  **Assumption Based Argumentation with goals and preferences(ABA+G)** is a newly proposed formalism for structured argumentation.
  
This project provides an interface which implements reasoning using the ABA+G formalism. There are algorithms for calculating extensions of these frameworks under various semantics, a problem which is of interest in fields such as AI, Law and Medicine. 

## CLI Usage

First install the relevant dependecies by running the command `make freeze && pip install -r requirements.txt`. Then install the CLI tool by running `pip install .` 

Users can specify the components of an ABA+G framework (i.e. Assumptions, Rules, Contraries, Preferences) in a file as follows: (Note that goals are as of now still unimplemented) 
-   **myAsm(a).**  specifies that  **a**  is an assumption;
-   **contrary(a**,  **x).**  specifies that  **x**  is the contrary of assumption  **a**;
-   **myRule(h**,  **[b1**]).**  specifies that  **h <- b1** is a rule;
-   **myPrefLT(b**, **a).** specifies that assumption **a** is strictly preferred over assumption **b**;
-   **myPrefLE(b**, **a).** specifies that assumption **a** is strictly or equally preferred over assumption **b**;

To get extensions of an ABA+ framework, `python src/cli.py --file "FILENAME"`

## Useful reading

The following papers provide a background on argumentation theory and this project. 

 - Francesca Toni: [A tutorial on assumption-based argumentation](https://www.tandfonline.com/doi/abs/10.1080/19462166.2013.869878). A great introductory tutorial to Assumption Based Argumentation (ABA).
 - Kristijonas Cyras, Claudia Schulz, and Francesca Toni: [Resolving Conflicts in Clinical Guidelines using Argumentation](https://arxiv.org/pdf/1902.07526.pdf). The paper which introduces the ABA+G formalism. 

## Developing  
  
The project comes with a set of commands you can use to run common operations for your stack:  
  
 - `make install`: Installs run time dependencies.  
 - `make install-dev`: Installs dev dependencies together with run time dependencies.  
 - `make freeze`: Freezes dependencies from `setup.py` to `requirements.txt` (including transitive ones).  
 - `make lint`: Runs static analysis.  
 - `make component`: Runs component tests.  
 - `make coverage`: Runs all tests collecting coverage.  
 - `make test`: Runs `lint` and `component`.  
  
### Updating dependencies  
  
Dependencies are managed from the `setup.py` file and then frozen in `requirements.txt` (including transitive dependencies) using `make freeze` (which uses `pip-compile`). If you want to change dependencies, you will have to do it in `setup.py` and then regenerate them using `make freeze`.  
  
Imagine your `setup.py` looks like  
  
```  
install_requires = [  
 'pytest~=3.3.0',]  
```  
  
if you want to update `pytest` to use version 3.4, you need to change it to  
  
```  
install_requires = [  
 'pytest~=3.4.0',]  
```  
  
If you execute `make freeze`, it will regenerate the `requirements.txt` file with the new dependencies according to what the new version of `pytest` needs.  
  
### Deployment to Heroku

The Flask API available in `src/app.py` can easily be deployed to Heroku. Please refer to the `Procfile` in the root folder and the official [Heroku documentation](https://devcenter.heroku.com/categories/reference) for more information on how to do this.   

## Contributing

If you would like to contribute to the project please follow these steps:

 - Clone the project locally.
 - Create a new feature branch.
 - Implement your feature while adhering to the development practices outlined above.
 - Once you are happy with your changes, make sure that the TravisCI checks are passing and create a pull request with a description of what you have changed.  
 
 Your pull request will be peer reviewed and merged into the master branch once ready.
