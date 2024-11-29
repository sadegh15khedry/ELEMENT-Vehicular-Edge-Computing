import pandas as pd
import matplotlib.pyplot as plt

_vehicle_id = "vehicle_id"
_task_id = "task_id"
_execution_location = "execution_location"
_size = "size"
_distance = "distance"
_transfer_rate = "transfer_rate"
_execution_cycles = "execution_cycles"
_start_time = "start_time"
_end_time = "end_time"
_release_time = "release_time"
_response_time = "response_time"
_transmission_time = "transmission_time"
_execution_time = "execution_time"
_execution_energy = "execution_energy"
_transfer_energy = "transfer_energy"
_total_energy = "total_energy"


class scraper():

    def __init__(self,report_path,cars,time_limit=-1):
        self.num_of_cars=cars
        # Load the CSV file into a DataFrame
        self.df = pd.read_csv(report_path)
        self.time_limit = time_limit
        if self.time_limit > 0:
            self.df = self.df[self.df[_end_time] <= self.time_limit]
        print("---------------------------------------------")
        print(report_path)
        if(time_limit<=0): 
            print("No time limit")
        else:
            print("The time limit is: "+str(time_limit))
        print("Header --->")
        print(self.df.head())


    def calc_average_all(self,console=True):
        data_columns=[_response_time,_transmission_time,_execution_time,_execution_energy,_transfer_energy,_total_energy]
        data_column_averages = self.df[data_columns].mean(numeric_only=True)
        
        simulation_param_columns=[_execution_location,_size,_distance,_transfer_rate,_execution_cycles]
        simulation_param_averages=self.df[simulation_param_columns].mean(numeric_only=True)
        if console:
            print("The overall average of our results:")
            print(data_column_averages)
            print("The overall average of simulation specific parameters:")
            print(simulation_param_averages)
        return data_column_averages[[_response_time,_total_energy]]
        

    def calc_average_for_each_car(self):
        
        columns=[_response_time,_transmission_time,_execution_time,_execution_energy,_transfer_energy,_total_energy,_execution_location]

        averaged_grouped_df = self.df.groupby(_vehicle_id)[columns].mean(numeric_only=True)
        print(averaged_grouped_df)

    def calc_sum_for_each_car(self):
        
        columns=[_response_time,_transmission_time,_execution_time,_execution_energy,_transfer_energy,_total_energy,_execution_location]

        averaged_grouped_df = self.df.groupby(_vehicle_id)[columns].sum(numeric_only=True)
        print(averaged_grouped_df)

    
    def calc_average_for_each_end_time(self,console=True,plot=False,plot_title=""):
        columns=[_response_time,_transmission_time,_execution_time,_execution_energy,_transfer_energy,_total_energy,_execution_location]

        averaged_grouped_df = self.df.groupby(_end_time)[columns].mean(numeric_only=True)
        if(console):
            print(averaged_grouped_df)
        
        if(plot):
            self.plot_response_and_energy(averaged_grouped_df,plot_title)
        
    def calc_sum_for_each_end_time(self,console=True,plot=False,plot_title=""):
            columns=[_response_time,_transmission_time,_execution_time,_execution_energy,_transfer_energy,_total_energy,_execution_location]

            averaged_grouped_df = self.df.groupby(_end_time)[columns].sum(numeric_only=True)
            if(console):
                print(averaged_grouped_df)

            if(plot):
                self.plot_response_and_energy(averaged_grouped_df,plot_title)



    def plot_response_and_energy(self,dataframe,title=""):
        axes = dataframe[[_response_time,_total_energy]].plot.line(subplots=True)
            
        axes[0].set_title("Response Time Plot")
        axes[0].set_ylabel("Time (ms)")
        axes[0].grid(True)

        axes[1].set_title("Total Energy Plot")
        axes[1].set_ylabel("Energy (J)")
        axes[1].grid(True)

        plt.suptitle(title, fontsize=16, fontweight='bold')