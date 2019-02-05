import argparse
#from tensorflow.example.tutorials.mnist import input_data


def parse_args():
	parser=argparse.ArgumentParser(description='CNN-SVM for image classification')
	gp=parser.add_argument_group('Argument')

	gp.add_argument('-m','--model',required=True,type=str,help='CNN-Softmax')
	gp.add_argument('-d','--dataset',required=True,type=str,help='path of mnist dataset')
	
	arguments=parser.parse_args()

	return arguments


if __name__=='__main__':
	args=parse_args()


