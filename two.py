import random
import matplotlib.pyplot as plt
def linear_gradient (x,y,theta):
    m,b=theta
    predicted=m*x+b
    error=predicted-y
    grad=[2*error*x,2*error]
    return grad

def mean_gradient(data,theta):
    gradients=[linear_gradient(x,y,theta)for x,y in data]
    return [sum(gradient[i] for gradient in gradients)/len(gradients) for i in range(len(theta))]

def gradient_descent(data,theta,learning_rate,epochs):
    fig= plt.figure(figsize=(10,5))
    ax = fig.add_subplot(111)
    plt.ion()
    fig.show()
    fig.canvas.draw()
    for epoch in range(epochs):
        ax.clear()
        grad=mean_gradient(data,theta)
        theta=[theta[i]-learning_rate*grad[i] for i in range(len(theta))]
        x_values=[x for x,_ in data]
        y_values=[y for _,y in data]
        ax.scatter(x_values,y_values,label='Original Data')
        line_x=[min(x_values),max(x_values)]
        line_y=[theta[0]*x+theta[1] for x in line_x]
        ax.plot(line_x,line_y,color='red',label='Linear Regression Line')
        ax.quiver(theta[0],theta[1],-grad[0],-grad[1],angles='xy',scale_units='xy',scale=1,color='green',width=0.01)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Epoch {epoch+1}')
        plt.legend()
        fig.canvas.draw()
        plt.pause(0.1)
        
    return theta

data = [(1,3),(2,5),(3,7),(4,9)]
initial_theta = [random.uniform(-1,1), random.uniform(-1,1)]
learning_rate=0.1
num_epochs=20
final_theta=gradient_descent(data,initial_theta,learning_rate,num_epochs)
print("Final parameters: ",final_theta)
