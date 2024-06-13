import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import matplotlib.animation as animation

#comment test
#Path to data
filePath = "c:/Users/Bruin/Downloads/SampleData/"

#Path to ffmpeg writer
plt.rcParams["animation.ffmpeg_path"] = "c:/Users/Bruin/Downloads/ffmpeg/ffmpeg/bin/ffmpeg.exe"

metadata = dict(title = "Movie", artist = "bruin")
writer = FFMpegWriter(fps = 60, metadata = metadata)

#Arrays to hold data
xData = []
yData = []
zData = []

#TODO: Add a writer to save my files


def getInput():
    #Asking user what parts of their data they'd like to use
    inputType = int(input("Would you like to use a set number, range or manually enter your inputs (Respond with 1,2,or 3)"))
    inputNums = [] #Holding the users data preferences
    def switch(inputType):
        if inputType == 1:
            inputNums.append(int(input("How many inputs would you like to enter?")))
            xfileInp = str(input("What is your x file name?\n"))
            for N in range(inputNums[0]):
                xFilePath = filePath + xfileInp + str(N + 1)
                x = []
                with open(xFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        x.append(number)
                xData.append(x)

            yfileInp = str(input("What is your y file name?\n"))
            for N in range(inputNums[0]):
                yFilePath = filePath + yfileInp + str(N + 1)
                y = []
                with open(yFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        y.append(number)
                yData.append(y)

            zfileInp = str(input("What is your z file name?\n"))
            for N in range(inputNums[0]):
                zFilePath = filePath + zfileInp + str(N + 1)
                z = []
                with open(zFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        z.append(number)
                zData.append(z)

            return inputNums[0]
            
        elif inputType == 2:
            inputNums.append(int(input("Please enter your lower bound: ")))
            inputNums.append(int(input("Please enter your upper bounds: ")))

            xfileInp = str(input("What is your x file name?\n"))
            for N in range(inputNums[0],(inputNums[1] + 1)):
                xFilePath = filePath + xfileInp + str(N + 1)
                x = []
                with open(xFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        x.append(number)
                xData.append(x)

            yfileInp = str(input("What is your y file name?\n"))
            for N in range(inputNums[0],(inputNums[1] + 1)):
                yFilePath = filePath + yfileInp + str(N + 1)
                y = []
                with open(yFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        y.append(number)
                yData.append(y)

            zfileInp = str(input("What is your z file name?\n"))
            for N in range(inputNums[0],(inputNums[1] + 1)):
                zFilePath = filePath + zfileInp + str(N + 1)
                z = []
                with open(zFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        z.append(number)
                zData.append(z)
            
            return (inputNums[1] - inputNums[0]) + 1
            
        

        elif inputType == 3:
            i = int(input("How many inputs would you like to enter?"))
            x = 0;


            while x < i:
                inputNums.append(int(input("Please enter input: ")))
                x = x + 1

            xfileInp = str(input("What is your x file name?\n"))
            for N in range(i):
                xFilePath = filePath + xfileInp + str(inputNums[N] + 1)
                x = []
                with open(xFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        x.append(number)
                xData.append(x)

            yfileInp = str(input("What is your y file name?\n"))
            for N in range(i):
                yFilePath = filePath + yfileInp + str(inputNums[N] + 1)
                y = []
                with open(yFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        y.append(number)
                yData.append(y)

            zfileInp = str(input("What is your z file name?\n"))
            for N in range(i):
                zFilePath = filePath + zfileInp + str(inputNums[N] + 1)
                z = []
                with open(zFilePath, "r") as file:
                    for line in file:
                        number = float(line.strip())
                        z.append(number)
                zData.append(z)

            return i

    return switch(inputType)


def getGraphicalInput():
    graphicalInput = []
    graphicalInput.append(int(input("How many dimensions would you like to plot?(Please enter 2 or 3)\n")))#TODO add options for input like which dimensions would you like?
    graphicalInput.append(int(input("What type of plot would you like?(1: Scatter, 2: Line plot)\n")))#TODO add more customizations
    graphicalInput.append(int(input("Would you like to save your plot?(0: No, 1: Yes)\n")))
    return graphicalInput

def graphTheInput(inputs, numInputs):
    def switch(graphinputs):
        if graphinputs[0] == 2:
            if graphinputs[1] == 1:
                if graphinputs[2] == 0:
                    twoDimensionalScatter(numInputs)
                elif graphinputs[2] == 1:
                    saveTwoDimScatter(numInputs)
            elif graphinputs[1] == 2:
                if graphinputs[2] == 0:
                    twoDimensionalLine(numInputs)
                elif graphinputs[2] == 1:
                    saveTwoDimLine(numInputs)
        elif graphinputs[0] == 3:
            if graphinputs[1] == 1:
                if graphinputs[2] == 0:
                    threeDimensionalScatter(numInputs)
                elif graphinputs[2] == 1:
                    saveThreeDimScatter(numInputs)
            elif graphinputs[1] == 2:
                if graphinputs[2] == 0:
                    threeDimensionalLine(numInputs)
                elif graphinput[2] == 1:
                    saveThreeDimLine(numInputs)
        
    switch(inputs)
#TODO add graphing software to file and complete graphinput().
def twoDimensionalScatter(numInputs):
    fig, ax = plt.subplots(figsize = (12,12))

    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))

    scatterplots = [ax.scatter(xData[j][0], yData[j][0]) for j in range(numInputs)]

    def animate(i):
        for n in range(numInputs):
            scatterplots[n].set_offsets((xData[n][i], yData[n][i]))

        return scatterplots,

    ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=max(len(x) for x in xData), interval=50)

    plt.show()

def saveTwoDimScatter(numInputs):
    fig, ax = plt.subplots(figsize = (12,12))

    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))

    scatterplots = [ax.scatter(xData[j][0], yData[j][0]) for j in range(numInputs)]

    def animate(i):
        for n in range(numInputs):
            scatterplots[n].set_offsets((xData[n][i], yData[n][i]))

        return scatterplots,

    ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=max(len(x) for x in xData), interval=50)

    ani.save('twoDimScatter.mp4', writer=writer) #This line is how we save it.
    plt.show()

def twoDimensionalLine(numInputs):
    fig, ax = plt.subplots(figsize = (12,12))
    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))

    lines = [ax.plot([], [])[0] for _ in range(numInputs)]

    def update(frame):
        for n in range(numInputs):
            lines[n].set_data(xData[n][:frame], yData[n][:frame])
        return lines


    ani = FuncAnimation(fig, update, frames=range(max(len(x) for x in xData)), blit=False)

    plt.show()

def saveTwoDimLine(numInputs):
    fig, ax = plt.subplots(figsize = (12,12))
    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))

    lines = [ax.plot([], [])[0] for _ in range(numInputs)]

    def update(frame):
        for n in range(numInputs):
            lines[n].set_data(xData[n][:frame], yData[n][:frame])
        return lines


    ani = FuncAnimation(fig, update, frames=range(max(len(x) for x in xData)), blit=False)
    
    ani.save('twoDimLine.mp4', writer=writer)
    plt.show()

def threeDimensionalScatter(numInputs):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))
    ax.set_zlim(min(min(z) for z in zData), max(max(z) for z in zData))

    scatters = [ax.scatter(xData[j][0], yData[j][0], zData[j][0]) for j in range(numInputs)]

    def animate(i):
        for n in range(numInputs):
            scatters[n]._offsets3d = (xData[n][i:i + 1], yData[n][i:i + 1], zData[n][i:i + 1])
        return scatters,

    ani = animation.FuncAnimation(fig, animate, repeat=True, frames=max(len(x) for x in xData), interval=50, save_count=len(xData[0]))
    plt.show()

def saveThreeDimScatter(numInputs):
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))
    ax.set_zlim(min(min(z) for z in zData), max(max(z) for z in zData))

    scatters = [ax.scatter(xData[j][0], yData[j][0], zData[j][0]) for j in range(numInputs)]

    def animate(i):
        for n in range(numInputs):
            scatters[n]._offsets3d = (xData[n][i:i + 1], yData[n][i:i + 1], zData[n][i:i + 1])
        return scatters,

    ani = animation.FuncAnimation(fig, animate, repeat=True, frames=max(len(x) for x in xData), interval=50, save_count=len(xData[0]))
    ani.save('threeDimScatter.mp4', writer=writer)
    plt.show()

def threeDimensionalLine(numInputs):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))
    ax.set_zlim(min(min(z) for z in zData), max(max(z) for z in zData))

    lines = [ax.plot([], [], [])[0] for _ in range(numInputs)]

    def update(frame):
        for n in range(numInputs):
            lines[n].set_data(xData[n][:frame], yData[n][:frame])
            lines[n].set_3d_properties(zData[n][:frame])
        return lines

    ani = FuncAnimation(fig, update, frames=range(max(len(x) for x in xData)), blit=False)
    plt.show()

def saveThreeDimLine(numInputs):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlim(min(min(x) for x in xData), max(max(x) for x in xData))
    ax.set_ylim(min(min(y) for y in yData), max(max(y) for y in yData))
    ax.set_zlim(min(min(z) for z in zData), max(max(z) for z in zData))

    lines = [ax.plot([], [], [])[0] for _ in range(numInputs)]

    def update(frame):
        for n in range(numInputs):
            lines[n].set_data(xData[n][:frame], yData[n][:frame])
            lines[n].set_3d_properties(zData[n][:frame])
        return lines

    ani = FuncAnimation(fig, update, frames=range(max(len(x) for x in xData)), blit=False)
    ani.save('threeDimLine.mp4', writer=writer)
    plt.show()

def main():
   
    numInputs = getInput() #Collect Input from user
    graphicalInput = getGraphicalInput() #Collect Information about what kind of graph they'd like
    graphTheInput(graphicalInput, numInputs)

if __name__ == "__main__":
    main()