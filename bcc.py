#!/usr/bin/env python3
import os
import fmtr
import numpy as np
import tensorflow as tf

WDBC_TRAINING_SET = "./data/wdbc.train.fmtd"
WDBC_TEST_SET = "./data/wdbc.test.fmtd"

if not os.path.exists(WDBC_TRAINING_SET):
	if os.path.exists(WDBC_TRAINING_SET[:-5]):
		fmtr.fmt(WDBC_TRAINING_SET[:-5], 0, 30)
		print("Generated formatted data successfully: {}".format(WDBC_TRAINING_SET))
	else:
		print("Missing dataset: {}".format(WDBC_TRAINING_SET[:-5]))


if not os.path.exists(WDBC_TEST_SET):
	if os.path.exists(WDBC_TEST_SET[:-5]):
		fmtr.fmt(WDBC_TEST_SET[:-5], 0, 30)
		print("Generated formatted data successfully: {}".format(WDBC_TEST_SET))
	else:
		print("Missing dataset: {}".format(WDBC_TEST_SET[:-5]))

# load dataset
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
	filename=WDBC_TRAINING_SET,
	target_dtype=np.float32,
	features_dtype=np.float32,
	target_column=0)

test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
	   filename=WDBC_TEST_SET,
	   target_dtype=np.float32,
	   features_dtype=np.float32,
	   target_column=0)

features = [tf.feature_column.numeric_column('x', shape=[30])]
''' 10 features '''
# def calculate_hidden_nodes(nodes):
# 	return round((((2 * nodes)/3) + 2))

# build 3 layer DNN with 10,20,10 units
classifier = tf.estimator.DNNClassifier(feature_columns=features,
	   hidden_units=[30,22,32],
	   n_classes=2,
	   optimizer='Adam',
	   activation_fn=tf.nn.relu,
	   model_dir='./tmp/wdbc_model')

train_input_fn = tf.estimator.inputs.numpy_input_fn(
	   x={"x": np.array(training_set.data)},
	   y=np.array(training_set.target),
	   num_epochs=None,
	   shuffle=True)

# train
classifier.train(input_fn=train_input_fn, steps=2000)

# Define the test inputs
test_input_fn = tf.estimator.inputs.numpy_input_fn(
	   x={"x": np.array(test_set.data)},
	   y=np.array(test_set.target),
	   num_epochs=1,
	   shuffle=False)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(input_fn=test_input_fn)
print(accuracy_score)#.get_variable_value(classifier.get_variable_names()))
print("\nTest Accuracy: {0:f}\n".format(accuracy_score["accuracy"]))