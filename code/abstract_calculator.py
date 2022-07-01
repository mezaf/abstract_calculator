import numpy as np
import pandas as pd

class abstract_calculator(object):
    def __init__(self, *args):
        super(abstract_calculator, self).__init__(*args)
        
    def horizontal_calculations(df:pd.DataFrame,formula,column_name):
            # Build function
        cols = list(df.columns)
        func_vars = ','.join(cols)
        func = f"""def f({func_vars}):\n\tresult = {formula}\n\treturn result"""
        exec(func,globals())

        # Create new column based on formula
        df[column_name] = np.vectorize(f)(*[df[col] for col in df.columns])
        return df
 