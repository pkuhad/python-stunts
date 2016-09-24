from sklearn import svm
import numpy as np

# Learn user choices 
USER_CHOICES = 20
CHOICE_LENGTH = 2

user_data_input = []
user_data_output = []

for i in range(USER_CHOICES):
    question_array = np.random.randint(10, size=CHOICE_LENGTH)
    user_data_input.append(question_array)
    user_input = np.array([int(raw_input('What do you think about %s' % question_array))])
    user_data_output.extend(user_input)

user_data_input = np.array(user_data_input)
user_data_output = np.array(user_data_output)


#for i in range(USER_CHOICES):
#    print user_data_input[i], '=', user_data_output[i]

print len(user_data_input)
print len(user_data_output)
# Train model

from sklearn.svm import SVC
clf = SVC()
clf.fit(user_data_input, user_data_output)


# Game output
user_game_input = []
user_game_output = []

for i in range(5):
    question_array = np.random.randint(10, size=CHOICE_LENGTH)
    user_game_input.append(question_array)

    user_input = np.array([int(raw_input('Now : What do you think about %s' % question_array))])

    machine_prediction = clf.predict(np.array([question_array]))
    if machine_prediction[0]==user_input:
        print 'Correct!!'
    else:
        print 'Well I think it is, ', machine_prediction


