# performance-monitoring-app
This Python application can be used to monitor the hardware resource consumption of specific programs.
It was realized as the final project for the "Sistemi Centrali" course at University of Catania (teacher: Fabrizio Messina).

# Functionalities
The software offers several features. The most significant ones are:
- **Choice of processes to analyze based on name or PID**: the tool, when started, it provides a list of all active processes, indicating their their names and PIDs. The user can then choose a subset of these processes to analyze, specifying their names/PIDs.
- **Collection of data regarding the CPU and RAM usage of each individual process**: data collection takes place individually for each process, and the duration of the collection depends on the user, who can stop it by pressing a specific combination of keys
- **Analysis of collected data**: for each chosen process it is calculated average CPU and RAM usage. In particular, the tool calculates a simple arithmetic mean on the data regarding the use of these resources
- **Print the results obtained**: the results obtained on each of the processes chosen by the user are shown in output, in two different formats:
      ▪ in text format, on the console, the calculated average consumption, both for CPU and RAM <br>
      ▪ in the form of graphs, the trend is displayed of the use of hardware resources, in order to identify any load peaks
- **Calculation of data aggregated across all processes**: at the end of the collection of data on individual processes, the user can request the calculation of the use Average CPU and RAM of all chosen processes. This information comes then shown on the console.

# Usage
1. Download a Python enviroment, e.g. (Anaconda)[https://www.anaconda.com/products/distribution] or directly from the (official Python site)[https://www.python.org/downloads/]
2. Download "monitoring.py" script
         . **OPTIONAL**: *you can also download "createProcesses.py" script, which allow you to automatically launch several instances of a specific program, in order to stress your CPU and RAM*. In order to specify the program you want to launch, you have to write the **path** of the program (e.g. *C:\Program Files/Blender Foundation/Blender 3.4/blender.exe*) and the number N of instances to launch.
3. Open a shell window, and launch the script with the command ***python monitoring.py***
4. Follow the istructions in the shell
