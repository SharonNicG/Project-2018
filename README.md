## Project 2018
> Project for Programming and Scripting Module 52167
---
### Abstract
---
### Table of Contents

- [Fisher and the Iris data set](https://github.com/SharonNicG/Project-2018/tree/master/fishers_iris_data_set)

---
### Introduction

This project sets out to examine the well known Fisher's Iris data set<sup>[1](http://archive.ics.uci.edu/ml/datasets/Iris)</sup>, through a review of existing research on the data set and an analysis of the data set using Python from which conclusions will be drawn.

---
### Fisher and the Iris data set

As this project is inspired by Fisher's Iris data set let us first look at what the data set is and how it was compiled.

Ronald Fisher (17 February 1890 – 29 July 1962), is considered one of the most important statistician of the twentieth century<sup>[2](https://doi.org/10.1093/ref:odnb/33146)</sup>. During his lifetime Fisher developed much of the theory behind modern statistics and a range of statistical tests still used today - such as the analysis of variance, ANOVA for short. However, Fisher's work was not limited to the field of mathematics. A founding member of the Cambridge University Eugenics Society, Fisher published numerous papers in the field of genetics exploring the inheritance of continuous traits, (which lay the foundations for his later work on variance), and the basis for population genetics, which examines the genetic differences within and between populations as part of evolutionary biology (*Ibid.*). 

In 1936, as Head of the Department of Eugenics at University College, London, Fisher developed a statistical tool to establish if a set of observations is effective in predicting membership of a category<sup>[3](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x)</sup>.

The tool developed by Fisher (the linear discriminant function – generalised to linear discriminant analysis or LDA<sup>[5]( https://en.wikipedia.org/wiki/Linear_discriminant_analysis)</sup>, is a multivariable statistical analysis technique for determining whether an object can be assigned to a predefined class on the basis of measured values (Butterfield, A. et. al, 2016). That is it looks at a set of observations for a category and seeks to identify predictors, or indicators, of that category. Applying these predictors to other samples ought to help determine if the samples fall into that category.
  
To achieve this a number of techniques are employed.

Fisher’s linear discriminant, as a multivariate tool, analyses data derived from multiple variables. Unlike univariate tools, which consider one variable - and only allow for descriptive analysis - multivariate tools support descriptive analysis of variables and analysis and exploration of the relationship between the variables (*Ibid.*).

By examining all of the available information from multiple variables at the same time Fisher’s linear discriminant projects the mean of each set of variables (class). The distance between the means presents the maximum separation between classes (the further the distance between means the greater the difference between classes). In addition to identifying the maximum variance between classes Fisher’s model also determines the minimum variance within each class so the similarities of each class can be characterised<sup>[7]( https://en.wikipedia.org/wiki/Linear_discriminant_analysis)</sup>.

From this analysis, we see both the differences and commonalities of the provided variables and the relationships between them. Exploring the variables in this way recognises the characteristics of each class which can be used to predict the possibility of an object being classified within a given group or category.

Fisher's 1936 paper, illustrated the use of this statistical method with a data set compiled by botanist Edgar Anderson - the classic Iris data set <sup>[8](http://www.jstor.org/stable/2394164)</sup>. 

The Iris data set is a multivariate data set measuring the form and structure for related species of the flowering plant - Iris<sup>[9](http://archive.ics.uci.edu/ml/datasets/Iris)</sup>. The data set contains 150 records subdivided into 5 attributes: the species (class) of Iris plant with 50 samples drawn from each of 3 related species (Iris setosa, Iris versicolor and Iris virginica) and for each sample, a set of 4 measurements consisting of the length and width of the sepal and petal, in centimetres.

Sepals, the outermost layer of the flower are easily distinguished on the Iris as they fall downwards away from the flower's centre. The petals of an Iris plant are internal of the sepals and are more upright and rigid<sup>[10](https://www.independent.ie/regionals/sligochampion/lifestyle/irises-coming-into-flower-in-gardens-and-in-the-wild-31252322.html)</sup>.

Fisher applied the linear discriminant model to analyse the data set, using the length and width variables associated with the sepals and petals to classify and predict the class for each sample. He found that the Iris setosa class was linearly separable from the other classes. However, Iris versicolor and Iris virginica were not linearly separable from each other and that overlap between these two classes prevented full classification<sup>[11](https://doi.org/10.1093/ref:odnb/33146)</sup>.

The Iris data set and Fisher's paper are still extensively used. While there are many reasons for this a contributing factor is the accessibility of the data. It is easy to understand and explain while still providing a practical amount of information to work with - 150 records, across 3 classes with 4 attributes per record. Additionally, as Fisher's analysis shows the data set offers both a linearly separable class and two classes that are more challenging to separate allowing it to be used to illustrate a variety of studies. Furthermore, using a classic data set as a benchmark set of results facilitates performance comparison of new techniques and algorithms.

---
### Investigation

In this section, we will conduct a preliminary review of the Iris data set by accessing and reading the data set file, familiarising ourselves with its content and then conducting a summary review of the data.

#### Problem Definition

The problem presented here is how to accurately predict the class of an Iris plant. Utilizing the Iris data set<sup>[11](http://archive.ics.uci.edu/ml/datasets/Iris)</sup>, which provides data on 150 samples of 3 Iris plants (50 samples of each class of Iris) and the corresponding length and width measurements of the sepal and petals for each plant, this investigation aims to predict the class of Iris of Iris plant based on the provided measurements.

#### Preparation

##### Environment

Before proceeding considering how the data will be used to address the classification problem and what tools will be needed to help with this is necessary.Based on Fisher's work, it can be assumed that this investigation will require work on numerical data in tables and arrays and that a number of mathematical computations of the data (e.g. mean) will be required. Additionally, visualizing the data for review and presentation will be beneficial. 

In reviewing scientific computing packages for Python a few seem to meet the requirements of this investigation.
* NumPy (Numerical Python) is an indispensable library for scientific computing in Python. It is the library that the other tools we'll be using are built upon. NumPy allows us to work with arrays and data structures easily and quickly and crucially it performs calculations across entire arrays.

* Pandas (Python Data Analysis Library) is a library for the Python language, built on the numPy package, that facilitates the manipulation of data structures (e.g. tables) making data easier to work with and conduct an analysis of.

* SciPy is an expanded library for scientific computing, built on the NumPy package. It includes a module for linear algebra which based on Fisher's work ought to be useful in classifying the samples from the dataset.

* Matplotlib is an extension of NumPy that generated 2D graphs, such as plots, histograms and scatter plot that enables the visualization of data to identify and present analysis and result. 

Having identified the libraries that are needed an online search shows that the Python distribution Anaconda provides all of the required packages. Downloading version Python 3.6 from Anaconda.com, we are prompted at installation to install Microsoft's Visual Studio Code (a code editor that supports working with Python) Accepting this allows us to use Visual Studio code as the platform for developing code for this project.

After installation, we can check that the Python environment is operating as expected. To do this we will write a short script to test the Python environment by importing each library, confirming which version it is operating and addressing any errors that present when the code is run. Running the script here returns no errors and so we can proceed with investigating the data. 

##### Data

Ahead of conducting an analysis of the data set, it is important to ensure it is in a useful format and that everything that is needed is included. The data selected for use here is the Iris Data Set available from the UCI Machine Learning Repository<sup>[11](http://archive.ics.uci.edu/ml/datasets/Iris)</sup>. WThere are various versions of the data set available, however, the UCI repository is a popular site that offers a wide range of free datasets which have been shown to be interesting - providing a good baseline for comparison. 

###### Access dataset

To facilitate work on the data set without the requirement for internet access a copy of the dataset file was downloaded and stored in the working directory in csv format. A backup version was also stored in case the data is changed in an unintended way during the investigation.

At this point, we can look at the data file to familiarise ourselves with its content. To do that a short script is created starting with Python's built-in 'open()' function to access the file, check if it's content is readable, print the output of the file. Introducing the 'with' keyword means that we can repeat this instruction effectively as the file is opened, accessed and closed after the script has finished handling the object in fewer lines of code. A 'for' loop and split method (with parameters) is also applied to return the data in the file in an easier to read format.

We can see from the output of the file that there are 5 columns of data, the first 4 hold numeric data (floats) and the 5th contains text (string). we can also see that the data is sorted by categories indicated in the 5th column. There is no discernable secondary ordering and the rows and columns of the table have no headings.

###### Preprocess data

Thinking about how we are going to use the data we need to consider if any preprocessing is required. The dataset description from UCI advises that the data has already undergone same preprocessing: 3 errors in Fisher's original work have been corrected, the number of attributes and instances have been identified, the authors advise that there are no missing attribute variables and the dataset is provided as tabular data. Given the relatively small size of the dataset (150 instances), it should be manageable as a whole without the need for sampling. 

#### Summary Investigation

Following on from the preliminary review of the data file we can proceed to a summary analysis of the data using the identified libraries. 

###### Importing libraries

To include the libraries in our script we use the 'import' statement. The libraries are imported here using the abbreviation conventions adopted by the Python community - NumPy(np), ScPy(sc), pandas(pd) and Matplotlib(plt). While SciPy has been abbreviated here to 'sc' it should be noted that the SciPy documentation recommends importing the required functions from SciPy and calling these as needed. The SciPy namespace only contains the functions imported from NumPy so better practice is to import the required function from within the library e.g. from 'SciPy' import 'stats'. At this point, we are not sure what functions are required so we'll retain the current library and review this as we progress. 

###### Summary of dataset

While the UCI repository provides details of the number of instances and attributes, to ensure we haven't lost anything in transferring/copying the file we can check this also. using the pandas command 'df.shape()' we can see the number of columns and rows in the dataset. We can see more details on the data structure using the 'df.info()' method which provides index, datatype, and memory information - and confirms that we have 150 results recorded in each column (4 numeric/floats and 1 text/object). Using 'df.count()', we can identify the any NULL observations. 

###### Assigning headers

As identified earlier the csv file from UCI doesn't include headers. While we know what data has been collected for the dataset 9from our review of Fisher's work) we need to be able to link what is presented in the columns and rows to the correct measurement/variable. The first thing we need to do is load the csv file into Python using a 'with' function and then read it using the pandas function 'pd.read_csv'. Viewing the output of this shows separated columns of data with row numbers in the left margin. By creating a headers array and pass this new variable to the 'read-csv' function. To see a summary view of the column headers we can use the 'dataframe.head()' function which returns, de default, the first 5 rows of the dataset - allowing us to see the headers in place.


---
### Analysis
---
### Conclusions
---
**Bibliography**
