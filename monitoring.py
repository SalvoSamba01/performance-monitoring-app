import psutil
import numpy as np
import matplotlib.pyplot as plt

pressd = "r"

while(pressd == "R" or pressd == "r"):
    input("Premi un tasto qualsiasi per mostrare la lista dei processi disponibili su cui effettuare il calcolo:\n\n ")
   
    process_list = psutil.process_iter()
    for process in process_list:
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
            print("PID: {} - Nome: {}".format(process_info['pid'] , process_info['name']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    c = input("\nVuoi cercare il processo per PID ('p') o per nome ('n'): ")
    while(c != "p" and c != "P" and c != "n" and c != "N"):
        c = input("Input errato, riprova: ")

    if(c == 'p' or  c == 'P'):
        pidString = input("Scrivi i PID separati da spazio:\n\n\n")
        PIDs = []
        for pid in pidString.split(sep=" "):
            PIDs.append(pid)
    
    else:
        nameString = input("Scrivi i nomi dei processi separati da spazio:\n")
        names = []
        for name in nameString.split(sep=" "):
            names.append(name)
            
        process_list = psutil.process_iter() 
        
        PIDs = [] 

        for process in process_list:
            process_info = process.as_dict(attrs=['pid', 'name'])
            for name in names:
                if process_info["name"].find(name) != -1:
                    PIDs.append(process_info["pid"])


    totMeanCPUList = 0.0
    totMeanRAMList = 0.0
    
    for pid in PIDs:
        print("\n\nSto calcolando i dati per il processo di pid = " , pid , " ; premi 'CTRL+C' per fermare la raccolta di dati")
        meanCpu = 0.0
        meanRam = 0.0
        cpuValues = []
        ramValues = []
        countRam = 0
        countCpu = 0
        try:
            while True:
                process_list = psutil.process_iter()    
                for process in process_list:
                    try:
                        process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
                        if str(process_info['pid']) == str(pid):
                            # NB. a volte la percentuale di CPU è oltre il 100
                            # ciò significa che il processo sta eseguendo diversi 
                            # thread su diversi core della CPU
                            # DOC: http://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent
                            if(process_info['cpu_percent']> 100):
                                print("Il processo sta utilizzando più core! \n")
                            # la quantità di cpu utilizzata è divisa per cpu_count(),
                            # cioè per il numero di core (DOC: https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent)
                            meanCpu = meanCpu + (process_info['cpu_percent']/ psutil.cpu_count())
                            cpuValues.append(round(process_info['cpu_percent']/ psutil.cpu_count(),2))
                            countCpu = countCpu + 1
                            meanRam = meanRam + process_info['memory_percent']
                            ramValues.append(round(process_info['memory_percent'],2))
                            countRam = countRam + 1
                                
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        except KeyboardInterrupt:
            pass


        print("----------------------------------------------------------------------------")
        print("Pid processo: {} - CPU media: {} % - RAM media: {} %".format(pid, meanCpu/countCpu, meanRam/countRam))
        print("----------------------------------------------------------------------------")

        totMeanRAMList = totMeanRAMList + (meanRam/countRam)
        totMeanCPUList = totMeanCPUList + (meanCpu/countCpu)

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        x = np.arange(len(cpuValues))
        axs[0].plot(x, cpuValues)
        axs[0].set_title('CPU Usage')
        axs[0].set_ylabel('% CPU')

        x = np.arange(len(ramValues))
        axs[1].plot(x, ramValues)
        axs[1].set_title('RAM Usage')
        axs[1].set_ylabel('% RAM')

        plt.show()

    c = input("\n\nVisualizzare l'utilizzo medio di CPU e RAM? (s/n) : ")
    while(c!='s' and c!='S' and c!='n' and c!='N'):
        c = input("\nValore non riconosciuto. Inserisci S/s se si, N/n se no : ")
    
    if(c=='s' or c=='S'):
        print("\nUso medio di CPU aggregato tra tutti i processi: ", totMeanCPUList/len(PIDs) )
        print("\nUso medio di RAM aggregato tra tutti i processi: ", totMeanRAMList/len(PIDs) )
        
    pressd = input("\n\n\nPremi R/r per effettuare un nuovo calcolo, altrimenti qualsiasi altro tasto per uscire: ")