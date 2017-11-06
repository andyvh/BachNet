import network_model
import statematrix
import output_midi

def main():

    # statematrix.main()
    #time layer #of neurons/ #of timeLayers/ #of noteLayer neurons/ #of noteLayers/ dropout
    model = network_model.choraleModel(True,[300,300],2,[100,50],2,0.5)
    output_midi.main()

if __name__ == '__main__':
    main()
