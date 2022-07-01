import numpy as np
import pandas as pd    

class ClassName(object):
    def __init__(self, *args):
        super(ClassName, self).__init__(*args))
        

class abstract_calculator(object):
    def __init__(self, iterable=(), *kwargs):
        # In case we have arguments that are not expected by the function
        # we can instantiate the class using **kwargs to provide values
        # that will be alocated in self.
        # i.e. by providing {"Key1":"val1","key2":"val2"}
        # you will be able to use  self.key1, self.key2 as an argument
        # for your function, it is good for hardcoded values given by
        # business users
        self.__dict__.update(iterable,**kwargs)       
        
    def horizontal_calculation(self,df:pd.DataFrame,formula:str,column_name:str):
        """
        
        Args:
            df (pd.Dataframe):  Dataframe to perform calculations to            
            formula (str):      Formula to apply using column names and what to apply
                                i.e. (columnA + columnB) / columnC
            column_name (str):  Name of the column where results will be written to

        Returns:
            df: New pd.Dataframe to work on with horizontal calculation applied
        """

        # Build function
        cols = list(df.columns)
        func_vars = ','.join(cols)
        func = f"""def f({func_vars}):\n\tresult = {formula}\n\treturn result"""
        exec(func,globals())

        # Create new column based on formula f, f exists only at runtime
        # based on the provided formula
        df[column_name] = np.vectorize(f)(*[df[col] for col in df.columns])
        return df
 
    def vertical_calcuation(self,df:pd.DataFrame,column_list,calculation_args):
        """_summary_

        Args:
            df (pd.Dataframe):    Dataframe to perform calculations to
            column_list (list):             List of columns to group by
            calculation_args (dict):        Dict with calculations to perform
                                            i.e. {"columnA":"sum,"columnB":["min","max"]}

        Returns:
            pd.Dataframe: Returns a fresh new data frame to be used with vertical calculations applied
        """    
        new_df = df.groupby(column_list).agg(calculation_args)
        return new_df
    
    def weight_distribution(self,df:pd.DataFrame,column_name:str,result_column_name:str):
        """_summary_

        Args:
            df (pd.Dataframe, optional):    Dataframe to perform calculations to        
            column_name (str):              Name of the column to perform weight distribution to
            result_column_name (str):       Name of the column to put weight distribution to

        Returns:
            pd.Dataframe: returns a dataframe with the new distribution column
        """      
        df[result_column_name] = df[column_name]/df[column_name].sum() 
        return df