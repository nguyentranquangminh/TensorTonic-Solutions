import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        return None
    intended_matrix = np.ones(matrix.shape)
    if (norm_type == 'l2'):
        if axis == 0:
            intended_matrix = intended_matrix.T
            for i, col in enumerate(matrix.T):
                s = np.sqrt(np.sum(col**2))      
                if s == 0: 
                    intended_matrix[i] = [0] * intended_matrix.shape[1]
                else:         
                    intended_matrix[i] = col / s
            intended_matrix = intended_matrix.T
            return intended_matrix
        if axis == 1:
            for i, row in enumerate(matrix):
                s = np.sqrt(np.sum(row**2)) 
                if s == 0:
                    intended_matrix[i] = [0] * intended_matrix.shape[1]
                else:              
                    intended_matrix[i] = row / s
            return intended_matrix
        if axis == None:
            s = np.sqrt(np.sum(matrix ** 2))
            if (s == 0):
                return np.zeros(matrix.shape)
            else:
                return matrix / s
            
    if (norm_type == 'l1'):
        if axis == 0:
            intended_matrix = intended_matrix.T
            for i, col in enumerate(matrix.T):
                s = np.sum(np.abs(col))
                if s == 0:
                    intended_matrix[i] = [0] * intended_matrix.shape[1]
                else:              
                    intended_matrix[i] = col / s
            intended_matrix = intended_matrix.T
            return intended_matrix
        if axis == 1:
            for i, row in enumerate(matrix):
                s = np.sum(np.abs(row))
                if s == 0:           
                    intended_matrix[i] = [0] * intended_matrix.shape[1]
                else:
                    intended_matrix[i] = row / s
            return intended_matrix
        if axis == None:
            s = np.sum(np.abs(matrix))
            if s == 0: 
                return np.zeros(matrix.shape)
            return matrix / s
    if (norm_type == 'max'):
        if axis == 0:
            intended_matrix = intended_matrix.T
            for i, col in enumerate(matrix.T):
                s = np.max(np.abs(col))   
                if s == 0:
                    intended_matrix[i] = [0] * intended_matrix.shape[1]
                else:
                    intended_matrix[i] = col / s
            intended_matrix = intended_matrix.T
            return intended_matrix
        if axis == 1:
            for i, row in enumerate(matrix):
                s = np.max(np.abs(row))    
                if s == 0:
                    intended_matrix[i] = [0] * intended_matrix.shape[1]        
                else:   
                    intended_matrix[i] = row / s
            return intended_matrix
        if axis == None:
            s = np.max(np.abs(matrix))
            if (s == 0):
                return np.zeros(matrix.shape)
            return matrix / np.max(np.ans(matrix))
    pass