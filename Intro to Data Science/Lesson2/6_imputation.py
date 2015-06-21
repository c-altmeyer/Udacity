from pandas import *
import numpy

# works

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    
    #YOUR CODE GOES HERE
    value = numpy.mean(baseball.weight)
    print baseball['weight']
    print value
    baseball['weight'] = baseball['weight'].fillna(value)
    print baseball['weight']
    return baseball
#if __name__ == "__main__":
    # read aadharr_data.csv into a pandas frame
#    input_filename =  "Master.csv"
#    output_filename = "output.csv"
#    baseball_weight = imputation(input_filename)
#    baseball_weight.to_csv(output_filename)

wdir = "C:\Users\\altmeyer\Documents\GitHub\Udacity\Intro to Data Science\Lesson2"
file = wdir + '\Master.csv'
imputation(file)