Articles: [Medium Article](https://medium.com/@Abel-Blue/a-b-test-using-machine-learning-a6dfbbb2d016)

---
# SmartAd Campaign - A/B Testing

![ab-test](https://blog.ida.cl/wp-content/uploads/sites/5/2014/07/ab-testing.jpg)

---
The main objective of this project is to evaluate if the ads that smartAd company runs resulted in a significant lift in brand awareness. 

We will cover:

    Setting up  classical & sequencial A/B tesing framework.
    Extracting statistically valid insights in relation to the business objective.
    Draw conclusion based on the satistical insights.

## Data & Background

- The BIO data for this project is a “Yes” and “No” response, of online users on the  question.
    Q: Do you know the brand Lux?

        O Yes
        O No

- Two types of user were using for the experiment, control & expose

    Control: users who have been shown a dummy ad

    Exposed: users who have been shown a creative (ad) that was designed by SmartAd for the client.

Control group engagment analysis
![model](images/control%20engagment.png)
Expose group engagment analysis
![model](images/exposed%20engagment.png)
P and t value for the groups
![model](images/p%20value.png)

## Conclusion

* Since the p-value is 0.5185 > alpha(0.05), We fail to reject the null hypothesis H0.
* So we came to the conclusion that there is no statistically significant difference between the two campaigns.

## A/B TESTING WITH MACHINE LEARNING

With A/B testing we compare between two, but with machine learning we can incorporate
the complexity and dynamic nature of data and draw insights.

Using k-fold cross validation we were able to train
three different models and determine their
accuracy in predicting our data.

### MEAN PERFORMANCE OF THE MODELS

accuracy score
![model](images/as.png)

#### Accuracy Scores

* Desicion Tree: 0.464
* Logistic Regression: 0.536
* XGBoost: 0.536
* Random Forest: 0.528
#### Best Models

* 1 - XGBoost
* 2 - Logistic Regression
* 3 - Random Forest

# Classical A/B test vs Machine learning

With classical A/B testing, we determined if there was a significant lift in brand awareness which is instrumental to smartAd in making the next move.

With Machine Learning, we discover that the other features like the hour of the day, and the dates, determine the conversion in brand awareness.

**There is a greater potential to have a significant lift in brand awareness.**


# Setup

## Installation

```bash
git clone https://github.com/Abel-Blue/smartAd-abTest
cd smartAd-abTest
sudo python3 setup.py install
```

---

## Contributirs

![Contributors list](https://contrib.rocks/image?repo=nardoshood/smartAd-abTest)

Made with [contrib.rocks](https://contrib.rocks)