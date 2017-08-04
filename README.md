# wacka-flacka
Small experiments with the IpinYou RTB dataset


### Introduction



### Data
The models are based on iPinYou dataset, a public real- world display ad dataset with each ad display information and corresponding user click feedback. The data logs are organised by different advertisers and in a row-per-record format. There are 19.50M data instances with 14.79K positive label (click) in total. The features for each data instance are all categorical. Feature examples in the ad log data are user agent, partially masked IP, region, city, ad exchange, domain, URL, ad slot ID, ad slot visibility, ad slot size, ad slot format, creative ID, user tags, etc. 

Used following make-file  https://github.com/wnzhang/make-ipinyou-data

During initial exploration a small dataframe is created with some features encoded with 23 columns. 

After one-hot encoding, the number of binary features is 937.67K in the whole dataset. We feed each compared model with these binary-feature data instances and the user click (1) and non-click (0) feedback as the ground-truth labels. In our experiments, we use training data from advertiser 1458, 2259, 2261, 2997, 3386 and the whole dataset, respectively.