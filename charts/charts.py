import matplotlib.pyplot as plt

def generate_chart():
    labels = ['A','B','C']
    values = [200,300,100]

    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('.pie.png')
    plt.close()