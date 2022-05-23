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
### 
sequential analysis
![model](images/sequ.png)
ml workflow
![model](data/pic.jpg)


## Conclusion
Accorfing to the classical A/B Test the ads that the advertising company runs did not result in a significant lift in brand awareness.



# Setup
## Docker

You can run the dashboard using docker:

```bash
docker pull abelblue/ad_image:1.0
docker run abelblue/ad_image:1.0
```

## Installation for linux

```bash
git clone https://github.com/Abel-Blue/smartAd-abTest
cd telecom-user-analytics
sudo python3 setup.py install

## Contributirs

![Contributors list](https://contrib.rocks/image?repo=nardoshood/smartAd-abTest)

Made with [contrib.rocks](https://contrib.rocks)