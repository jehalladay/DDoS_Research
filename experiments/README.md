# Experiments

Here are the files for all the experiments conducted in this paper. To run and verify our results or to learn, users must have already downloaded the CICDDoS2019 dataset and must have run all the code in Dataset_generation.ipynb. Follow the instructions found [here](https://github.com/jehalladay/DDoS_Research/tree/main/data).

Our research has been constructed to show that Time-Based Features can be used to successfully detect and characterize DDoS attacks. This set of Time-Based Features has been show by [Lashkari et al.](https://www.researchgate.net/publication/314521450_Characterization_of_Tor_Traffic_using_Time_based_Features) to be effective at detecting web traffic that passes through the Onion Router (Tor) and characterizing that traffic by the type of application it originated from (p2p, streaming, chat, website, etc). Our goal was to show that this same set of features can be used in a different domain to detect and characterize DDoS traffic. We accomplish this through 4 scenarios of experiments conducted with the set of time-based features (25) and a control consisting of a baseline set of features (70). Futhermore, we show that this set of features is effective with a wide range of classifiers and its efficacy is not generally dependant on any single classification technique.

We conduct experiments using 9 different classifier:
  * Adaboost
  * Deep Neural Network
  * K Nearest Neighbors
  * LightGBM
  * Linear Discriminant Analysis
  * Naives Bayes
  * Random Forest
  * Support Vector Machines
  * XGBoost

We conducted experiments for 4 Scenarios:
  * A: Binary Classification of Benign vs. DDoS traffic flows "Benign vs. DDoS"
  * B: Multiclass Classification DDoS traffic as one of twelve different attack types
  * C: Binary Classification of one type of DDoS attack against benign traffic flows "Benign vs. attack"
  * D: Binary Classification of one type of DDoS attack against a basket of all other DDoS attacks "attack vs. DDoS"
  
The significance of the scenarios are as follows:
  * A: Shows how effective the classifier is at detecting DDoS attacks out of a 1:1 ratio of Benign traffic against a basket of all DDoS attack types
  * B: Shows how effective the classifier is at characterizing the type of DDoS attack out of a 1:11 ratio of each of 12 different DDoS attack types
  * C: Shows how effective the classifier is at detecting an individual DDoS attack out of a 1:1 ratio of Benign traffic against a single DDoS attack type
  * D: Shows how effective the classifier is at detecting an individual DDoS attack out of a 1:1 ratio of a single DDoS attack type against a basket of all other 11 DDoS attack types
