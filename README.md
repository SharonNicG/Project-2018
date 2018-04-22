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


---
### Investigation
---
### Analysis
---
### Conclusions
---
**Bibliography**
