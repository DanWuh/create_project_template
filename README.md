# Create Template

This is a generic project template generator that prepares the following folder structure for your academic projects:

```
Project/
|-- writing/
|   |-- figures
|   |-- bib
|   |-- notes
|
|--literature
|   |-- papers
|   |-- notes
|
|-- statistics/
|   |-- data/
|   |   |-- data.csv
|   |-- figures/
|   |-- notes
|
|-- materials
|   |-- sounds/
|   |-- texts/
|   |-- analysis/
|   |-- notes
|
|-- scripts
|   |-- code
|   |-- notes
|
|-- README.md
```

## The hard way
To create this project structure put 'create_template.py' in the directory you want to create the project and run:

> python create_template.py



## The easy way
To avoid dealing with the location of the script, a better option is to create an alias in your .bash_profile that points to its location. To do this, you need to open .bash_profile using your favorite editor like emacs or vim but for most users it is easier with 'nano':

> nano ~/.bash_profile

Then write the following at the end of the file:

> alias ct="python ~/Documents/GTD/project_templates/code/create_template.py"

When you finish editing press
Ctrl + X and then "Yes" to save and exit.

Now, you can run the script simply by typing in all directories that you have sufficient privileges  

> ct

