import matplotlib.pyplot as plt
import numpy as np


def Sigmoid(x):
    y = np.exp(x) / (np.exp(x) + 1)
    return y


def Sigmoid_gradient(x):
    y = (np.exp(x) / (np.exp(x) + 1)) * (1 - (np.exp(x) / (np.exp(x) + 1)))
    return y


def Tanh(x):
    y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    # y = np.tanh(x)
    return y


def Tanh_gradient(x):
    y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    g = 1 - np.power(y, 2)
    return g


def ReLU(x):
    y = np.where(x < 0, 0, x)
    return y

def Relu_gradient(x):
    y= np.where(x >=0,1,0)
    return y


def LeakyReLU(x, a):
    # LeakyReLU的a参数不可训练，人为指定。
    y = np.where(x < 0, a * x, x)
    return y

def LeakyReLU_gradient(x, a):
    # LeakyReLU的a参数不可训练，人为指定。
    y = np.where(x >= 0, 1, a)
    return y


def PReLU(x, a):
    # PReLU的a参数可训练
    y = np.where(x < 0, a * x, x)
    return y


def ReLU6(x):
    y = np.minimum(np.maximum(x, 0), 6)
    return y


def Swish(x, b):
    y = x * (np.exp(b * x) / (np.exp(b * x) + 1))
    return y

def Swish(x, b):
    y = x * (np.exp(b * x) / (np.exp(b * x) + 1))
    return y


def Mish(x):
    # 这里的Mish已经经过e和ln的约运算
    temp = 1 + np.exp(x)
    y = x * ((temp * temp - 1) / (temp * temp + 1))
    return y


def Grad_Swish(x, b):
    y_grad = np.exp(b * x) / (1 + np.exp(b * x)) + x * (b * np.exp(b * x) / ((1 + np.exp(b * x)) * (1 + np.exp(b * x))))
    return y_grad


def Grad_Mish(x):
    temp = 1 + np.exp(x)
    y_grad = (temp * temp - 1) / (temp * temp + 1) + x * (4 * temp * (temp - 1)) / (
            (temp * temp + 1) * (temp * temp + 1))
    return y_grad

def SiLU(x):
    y = x*(np.exp(x) / (np.exp(x) + 1))
    return y
def SiLU_gradient(x):
    y = x*np.exp(x) / (np.exp(x) + 1)
    g = y+(np.exp(x) / (np.exp(x) + 1)*(1-y))
    return g

if __name__ == '__main__':
    x = np.arange(-10, 10, 0.01)

    plt.plot(x, Sigmoid(x),color='c')
    plt.title("Sigmoid")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig("Sigmoid.png", dpi=600)
    plt.show()
    #
    plt.plot(x, Sigmoid_gradient(x),color='c')
    plt.title("Gradient of Sigmoid")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('Sigmoid_gradient.png', dpi=600)
    plt.show()

    plt.plot(x, Tanh(x),color='c')
    plt.title("Tanh")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('Tanh.png', dpi=600)
    plt.show()

    plt.plot(x, Tanh_gradient(x),color='c')
    plt.title("Gradient of Tanh")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('Gradient of Tanh.png', dpi=600)
    plt.show()


    plt.plot(x, ReLU(x),color='c')
    plt.title("ReLU")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('ReLU.png', dpi=600)
    plt.show()

    plt.plot(x, Relu_gradient(x),color='c')
    plt.title("Gradient of ReLU")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('Gradient of ReLU.png', dpi=600)
    plt.show()


    plt.plot(x, LeakyReLU(x, 0.1),color='c')
    plt.title("LeakyReLU")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('LeakyReLU.png', dpi=600)
    plt.show()

    plt.plot(x, LeakyReLU_gradient(x, 0.1),color='c')
    plt.title("LeakyReLU")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('LeakyReLU_gradient.png', dpi=600)
    plt.show()

    # plt.plot(x, PReLU(x, 0.25))
    # plt.title("PReLU")
    # plt.grid()
    # plt.show()
    #
    plt.plot(x,SiLU(x),color='c')
    plt.title('SiLU')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('SiLU.png',dpi=600)
    plt.show()

    plt.plot(x, SiLU_gradient(x),color='c')
    plt.title('Gradient of SiLU')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig('SiLU_gradient.png', dpi=600)
    plt.show()

    # plt.plot(x, ReLU6(x))
    # plt.title("ReLU6")
    # plt.grid()
    # plt.show()
    #
    # plt.plot(x, Swish(x, 1))
    # plt.title("Swish")
    # plt.grid()
    # plt.show()
    #
    # plt.plot(x, Mish(x))
    # plt.title("Mish")
    # plt.grid()
    # plt.show()
    #
    # plt.plot(x, Grad_Mish(x))
    # plt.plot(x, Grad_Swish(x, 1))
    # plt.title("Gradient of Mish and Swish")
    # plt.legend(['Mish', 'Swish'])
    # plt.grid()
    # plt.show()
