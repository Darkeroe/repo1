import tensorflow as tf ###TensorFlow를 사용하기 위한 import
from tensorflow.examples.tutorials.mnist import input_data

# Dataset loading
mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True)

# Set up model
x = tf.placeholder(tf.float32, [None, 784]) ###TensorFlow에게 계산을 하도록 명령할 때 입력할 값. 784는 각 이지미가 가로, 세로가 각 28픽셀이기 떄문에 28*28=784개의 숫자를 갖는 벡터로 단순화시킨 값입니다.
W = tf.Variable(tf.zeros([784, 10])) ###텐서 w를 0으로 채워서 초기화시킵니다.
b = tf.Variable(tf.zeros([10])) ###텐서 b를 0으로 채워서 초기화시킵니다.
y = tf.nn.softmax(tf.matmul(x, W) + b) ###우선 x와 W를 곱하는데 matmul(W, x)가 아니라 matmul(x, W)인 이유는 x가 여러 입력으로 구성된 2D텐서일 경우를 다루기 위함입니다. 그리고 그 값에 b를 더하고 tf.nn.softmax를 적용합니다.

y_ = tf.placeholder(tf.float32, [None, 10]) ###정답을 입력하기 위한 새 placeholder를 추가합니다.

cross_entropy = -tf.reduce_sum(y_*tf.log(y)) ###tf.log는 y의 각 원소의 로그값을 계산합니다. 그 다음, y_ 의 각 원소들에, 각각에 해당되는 tf.log(y)를 곱합니다. 마지막으로, tf.reduce_sum은 텐서의 모든 원소를 더합니다. 
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy) ###경사 하강법(gradient descent) 알고리즘을 이용하여 TensorFlow가 각각의 변수들의 비용을 줄이는 방향으로 약간씩 바꾸는 간단한 방법입니다.

# Session
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

# Learning
for i in range(1000): ###1000번 학습을 시키는 반복문
  batch_xs, batch_ys = mnist.train.next_batch(100) ###100개의 무작위 데이터들의 일괄처리(batch)들을 가져옵니다.
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys}) ###placeholders를 대체하기 위해 일괄처리데이터에 train_step 피딩을 실행합니다.

# Validation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1)) ###tr.grgmax(y,1)는 진짜 라벨이 tf.argmax(y_,1) 일때 우리 모델이 각 입력에 대해 가장 정확하다고 생각하는 라벨이다,tf.equal을 이용해 예측이 실제와 맞았는지를 확인합니다.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) ###정확도를 확인합니다.

# Result should be approximately 91%.
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})) ###정확도를 출력합니다.