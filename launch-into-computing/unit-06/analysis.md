SMS Spam Classification Analysis

This project developed a machine-learning model that classifies SMS messages as spam or normal. It used the publicly available SMS Spam Collection from the UCI Machine Learning Repository. The original dataset contains 5,574 labelled messages collected from several sources (Almeida and Hidalgo, 2011). After duplicate and incomplete records were removed, 5,169 messages remained. The data was divided into 80% training data and 20% testing data. This separation allowed the model to be evaluated using messages that it had not seen during training.

The model combined CountVectorizer with Multinomial Naive Bayes. CountVectorizer converted each message into numerical word counts, while Multinomial Naive Bayes estimated whether those word patterns were more closely associated with spam or normal messages. Scikit-learn identifies this classifier as suitable for discrete features such as word counts in text classification (Scikit-learn, 2024).

The model achieved 98.2% accuracy, 95.9% precision and 89.3% recall. Of 1,034 test messages, it correctly classified 898 normal messages and 117 spam messages. However, five normal messages were incorrectly marked as spam, while fourteen spam messages were missed. The high accuracy therefore does not mean that the system was error-free. The lower recall shows that detecting every spam message was more difficult than avoiding false spam warnings.

Both error types may have serious effects. If a legitimate work, banking or appointment message is placed in the spam folder, the user might miss important information or a deadline. If dangerous spam reaches the inbox, the user might open a malicious link or attachment. The dataset also has limitations because it was donated in 2012 and mainly contains English-language messages from particular groups and locations. Newer scams, other languages and different writing styles may therefore be classified less accurately. Privacy, informed consent and secure handling of message content must also be considered when developing a real-world spam filter.

References

Almeida, T. and Hidalgo, J. (2011) SMS Spam Collection [Dataset]. UCI Machine Learning Repository. Available at: https://doi.org/10.24432/C5CC84 (Accessed: 23 September 2026).

Scikit-learn (2024) MultinomialNB. Available at: https://scikit-learn.org/1.4/modules/generated/sklearn.naive_bayes.MultinomialNB.html (Accessed: 23 September 2026).