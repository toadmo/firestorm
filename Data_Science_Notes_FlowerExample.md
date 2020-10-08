Data Science Notes:
 - For an array of lists, each list is an instance(sample or record), and each entry in the list is a feature(dimension or attribute).
 - The data for the first graph is not great because it is plotted in all the dimensions that there are variables, so it is difficult to determine where the points are in relation to the axes.
 - Newer graph gives the axes separately, so more clear comparisons can be drawn.
 - Can use the K Nearest Neighbor for each of the variables and compare it to species to see which one it should be.
 
 K Nearest Neighbor (KNN):
- Helpes to classify an unknown by analyzing the closest entities and then determining based off of proximity to other data points.
- The value K determines how many closest entities are found before judging the data point. 
    - Too low of k means a possibility of overfitting due to noise in the data.
    - Too high means that there is possibility of misclassification, misses close data points. 
    - Good value usually between 5 and 10.
- Eager Learner: Classifiers such as regression models, decision trees, rule-based, etc. 
    - Designed to learn a model that maps the input attribute as soon as the training data is available.
- Lazy Learner: k-NN
    - Delays process of modelling training data until it is needed to classify test examples.